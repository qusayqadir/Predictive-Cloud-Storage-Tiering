# build a REST API that can be called on for future files that are about to be pushed onto the cloud 
# can be used to deteremine the storage tier 

#1 use FLASK to create a REST API   

from flask import Flask, request, jsonify
import pandas as pd 
import numpy as np 
import pickle
import json 

from sklearn.preprocessing import StandardScaler, MinMaxScaler

with open("xgboost_model_v6.pkl","rb") as file: 
    xgboost_model = pickle.load(file) 

app = Flask(__name__)

with open("scaler_minmax.pkl","rb") as file: 
    scaler_minmax = pickle.load(file) 

with open("scaler_standard.pkl", "rb") as file: 
    scaler_standard = pickle.load(file)



@app.route("/predict", methods=["POST"]) 

def predict(): 
    try: 
        file = request.files["file"] 
        file_name = file.filename #input data 

            # why is it asking me for a z_score column?? 

        df = pd.read_csv(file) 


        # preprocess if nesessary

        cols = ["Access_Frequency","Frequnecy_of_Access","File_Size","File_Lifecycle_Stage","Modification_Frequency","File_Age"]

        df_preprocessed = df[cols] 
        standardized_data = scaler_standard.transform(df_preprocessed) 
        normalized_data = scaler_minmax.transform(standardized_data) 

        prediction = xgboost_model.predict(normalized_data)

        response = {
            "file_name" : file_name, 
            "prediction" : prediction.tolist()
            }
        
        return jsonify(response)

    except Exception as e: 
        return jsonify({"error":str(e)}) 




if __name__ == "__main__": 
    app.run(debug=True)  