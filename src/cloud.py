import os 
import requests 
import boto3 
import pandas as pd 

s3 = boto3.client('s3' , aws_access_key_id = "AKIAXBZV5WDLGNUNRQEV" , aws_secret_access_key = "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" ) # leave default region (us-east-1), output-fromat (json)


bucket_mapping = { 
    2 : "hot-storage-buket" , 
    1: "warm-storage-bucket", 
    0 : "cold-storage-bucket" 
}

s3_simulated_data = "../data/s3-simulated-data/csv_files"

api_url = "http://127.0.0.1:5000/predict" 

log_file = "file_upload_storage_tier_map.csv" 
log_data = [] 

for file_name in os.listdir(s3_simulated_data): 
    if file_name.endswith(".csv"): 
        file_path = os.path.join(s3_simulated_data, file_name) 

        with open(file_path, "rb") as file: 
            response = requests.post(api_url, files={"file" : file}) 
            print(f"Response Status: {response.status_code}") 
            print(f"Response Content: {response.json()}")

        # if response.status_code == 200:
            
        #     prediction = response.json().get("prediction", [])
        #     bucket_name = bucket_mapping.get(int(prediction[0])) 

        
        #     if bucket_name: 

        #         s3.upload_file(file_path, bucket_name, file_name) 

        #         log_data.append(
        #             {
        #                 "File Name" : file_name, 
        #                 "Destination Bucket" : bucket_name
        #             }
        #         )

df = pd.DataFrame(log_data) 
df.to_csv(log_file, index=False) 
