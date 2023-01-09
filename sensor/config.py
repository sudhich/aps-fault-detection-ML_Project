import pymongo
import pandas as pd
import json
from dataclasses import dataclass
#Provide the mogodb localhost url to connect python to mongodb.
import os

@dataclass
class EnvironmentVariable:
    mongo_db_url:str = os.getenv("MONGO_DB_URL") #os.getenv() method in Python returns the value of the environment variable key if it exists otherwise returns the default value(None).
    aws_access_key_id:str = os.getenv("AWS_ACCESS_KEY_ID")  
    aws_secret_access_key:str=os.getenv("AWS_SECRET_ACCESS_KEY")

env_var = EnvironmentVariable()
mongo_client=pymongo.MongoClient(env_var.mongo_db_url)


