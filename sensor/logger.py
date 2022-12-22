import logging
import os
from datetime import datetime
import os

#log file name
LOG_FILE_NAME = f"{datetime.now().strftime('%m%d%Y__%H%M%S')}.log" #print(LOG_FILE_NAME) #output is= 12222022__111813.log


#log directory
LOG_FILE_DIR = os.path.join(os.getcwd(),"logs") #print(LOG_FILE_DIR) #output is= /config/workspace/logs Ex-#import os #goal_dir = os.path.join(os.getcwd(), "../../my_dir") Now, if the current directory is C:/here/I/am/, it joins them as C:/here/I/am/../../my_dir.

#create folder if not available
os.makedirs(LOG_FILE_DIR,exist_ok=True) #print(os.makedirs(LOG_FILE_DIR,exist_ok=True)) # output is= None


#log file path
LOG_FILE_PATH = os.path.join(LOG_FILE_DIR,LOG_FILE_NAME) #print(LOG_FILE_PATH) output is= /config/workspace/logs/12222022__112216.log

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)
# format== [ 2022-12-22 13:25:08,971 ] 6 root - INFO - Starting the test_and_logger_exception