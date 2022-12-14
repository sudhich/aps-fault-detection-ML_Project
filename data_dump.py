import pymongo
import pandas as pd
import json
# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATA_FILE_PATH="/config/workspace/aps_failure_training_set1.csv"
DATABASE_NAME="aps"
COLLECTION_NAME="sensor"


if __name__ == "__main__":
    df=pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and Columns: {df.shape}")

    #Convert dataframe to json so that we can dump these record in mongo db
    df.reset_index(drop=True,inplace=True) #If you set drop = True , reset_index will delete the index instead of inserting it back into the columns of the DataFrame.   #When you set inplace = True , the reset_index method will not create a new DataFrame. Instead, it will directly modify and overwrite your original DataFrame in given data.
    
    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    #Insert converted record to mongo db.
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record) #see go to aps->sensor->document