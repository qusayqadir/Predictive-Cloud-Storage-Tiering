import os 
import csv
import random 

def createTrainCSV(): 


    headers_s3 = ["Access_Frequency", "Frequnecy_of_Access","File_Size", "File_Lifecycle_Stage","Modification_Frequency","File_Age"]


    storageTier_weights =  { 

        "Hot" : {
            "Access_Frequency" : 35 , 
            "Frequnecy_of_Access" : 30, 
            "File_Size" : 0 , 
            "File_Lifecycle_Stage" : 0 , 
            "Modification_Frequency" : 30 ,
            "File_Age" : 5 , 
        },

        "Cold" : { 
            "Access_Frequency" : 30 , 
            "Frequnecy_of_Access" : 25 , 
            "File_Size" : 15 , 
            "File_Lifecycle_Stage" : 10, 
            "Modification_Frequency" : 10 ,
            "File_Age" : 10, 

        }, 

        "Warm" : { 
            "Access_Frequency" : 20, 
            "Frequnecy_of_Access" : 10 , 
            "File_Size" : 30, 
            "File_Lifecycle_Stage" : 20, 
            "Modification_Frequency" : 20,
            "File_Age" : 0, 
        }

    }

    num_file = 1000 


    random.seed(1)
    
    for i in range(1, num_file + 1): 
        tier_choice = random.choice(list(storageTier_weights.keys())) 
        # Keys: Hot, Cold, Warm 

        weighted_score = 0 

        AccessF_score = round(storageTier_weights[tier_choice]["Access_Frequency"] * random.uniform(0.1,0.99), 4) # "Access_Frequency"
        FrequencyA_score = round(storageTier_weights[tier_choice]["Frequnecy_of_Access"] * random.uniform(0.1,0.99) , 4 ) #    "Frequnecy_of_Access"
        FileS_score =  round ( storageTier_weights[tier_choice]["File_Size"] * random.uniform(0.1,0.99) , 4 ) # "File_Size"
        FileLS_score = round( storageTier_weights[tier_choice][ "File_Lifecycle_Stage"] * random.uniform(0.1,0.99) , 4) #   "File_Lifecycle_Stage" 
        ModF_score = round( storageTier_weights[tier_choice][ "Modification_Frequency" ] * random.uniform(0.1,0.99), 4 ) #  "Modification_Frequency"
        FileA_score = round ( storageTier_weights[tier_choice]["File_Age"] * random.uniform(0.1,0.99) , 4 )   #  "File_Age"

        weighted_score = AccessF_score + FrequencyA_score + FileS_score + FileLS_score + ModF_score + FileA_score 



        row_s3 = {
            "Access_Frequency" : AccessF_score, 
            "Frequnecy_of_Access" : FrequencyA_score, 
            "File_Size" : FileS_score, 
            "File_Lifecycle_Stage" : FileLS_score, 
            "Modification_Frequency" : ModF_score,
            "File_Age" : FileA_score
        }


        with open(file=f"csv_files/File_{i}.csv", mode="w", newline="") as file: 
            writer = csv.DictWriter(file, fieldnames=headers_s3) 
            writer.writeheader() 
            writer.writerow(row_s3)





if __name__ == "__main__": 
    createTrainCSV() 