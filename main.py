from sensor.logger import logging
from sensor.exception import SensorException
from sensor.utils import get_collection_as_dataframe
import sys,os



if __name__=="__main__":
    try:
        get_collection_as_dataframe(database_name="aps",collection_name="sensor")
    except Exception as e:
        print(e)



























#def test_looger_and_exception():
#    try:
#        logging.info("Starting the test_and_logger_exception")
#        result=3/0
#        print(result) #main.py \n Error occurred python script name [main.py] line number [6] error message [division by zero]
#        logging.info("Stopping the test_and_logger_exception")
#    except Exception as e:
#        logging.debug("Stopping deb the test_and_logger_exception")
#        raise SensorException(e,sys)

#if __name__=="__main__":
#    try:
#        test_looger_and_exception()
#    except Exception as e:
#        print(e)


























#import pymongo

# Provide the mongodb localhost url to connect python to mongodb.
#client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")  #print(client) # output=MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True)

# Database Name
#dataBase = client["neurolabDB"]  #print(dataBase) #output= Database(MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True), 'neurolabDB')
# Collection  Name
#collection = dataBase['Products'] #print(collection) #output= Collection(Database(MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True), 'neurolabDB'), 'Products')
# Sample data
#d = {'companyName': 'iNeuron',
#     'product': 'Affordable AI',
#     'courseOffered': 'Machine Learning with Deployment'}

# Insert above records in the collection
#rec = collection.insert_one(d)  #print(rec) #output= <pymongo.results.InsertOneResult object at 0x7fa682693130>
# Lets Verify all the record at once present in the record with all the fields
#all_record = collection.find()  #print(all_record) #potput= <pymongo.cursor.Cursor object at 0x7f9204b1f1c0>
# Printing all records present in the collection
#for idx, record in enumerate(all_record):
#     print(f"{idx}: {record}") 
                              #print(f"{idx}: {record}") output= 0: {'_id': ObjectId('63a3f904d9ff161fe395fe27'), 'companyName': 'iNeuron', 'product': 'Affordable AI', 'courseOffered': 'Machine Learning with Deployment'}
                              #1: {'_id': ObjectId('63a3f94d06db823920308bf1'), 'companyName': 'iNeuron', 'product': 'Affordable AI', 'courseOffered': 'Machine Learning with Deployment'}
                              #2: {'_id': ObjectId('63a3f98d4cc0a7ed9d4b5dc5'), 'companyName': 'iNeuron', 'product': 'Affordable AI', 'courseOffered': 'Machine Learning with Deployment'}
