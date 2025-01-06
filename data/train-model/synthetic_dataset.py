import os 
import csv
import random 

def createTrainCSV(): 

    headers = [ "File_ID", "Access_Frequency","Frequnecy_of_Access","File_Size","File_Lifecycle_Stage","Modification_Frequency",
        "File_Age","Storage_Tier" ]
    
    train_csv_file_path = "../../data/train-model/train-file-metadata.csv"  #output file path

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

    rows = [ ] 
    num_rows = 2000 

    random.seed(1)
    
    for i in range(num_rows): 
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

        Storage_Tier = " " 

        if weighted_score > 70 and weighted_score <= 100: 
            Storage_Tier = "Hot" 
        elif weighted_score <= 70 and weighted_score >=40: 
            Storage_Tier = "Warm" 
        else: 
            Storage_Tier = "Cold"

        row = { 
            "File_ID" : f"File_{i+1}", 
            "Access_Frequency" : AccessF_score,
            "Frequnecy_of_Access" : FrequencyA_score, 
            "File_Size" : FileS_score, 
            "File_Lifecycle_Stage":  FileLS_score , 
            "Modification_Frequency" : ModF_score , 
            "File_Age" : FileA_score, 
            "Storage_Tier" : Storage_Tier 
        }

        rows.append(row) 


    with open(file=train_csv_file_path, mode="w", newline="") as file: 
        writer = csv.DictWriter(file, fieldnames=headers) 
        writer.writeheader() 
        writer.writerows(rows)




if __name__ == "__main__": 
    createTrainCSV() 