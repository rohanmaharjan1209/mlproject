import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" #get the log file and time in called format
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE) #get the current working directory and logs 
os.makedirs(logs_path, exist_ok = True) #keep on appending the file even when there is the same file

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,
)

if __name__ == "__main__":
    logging.info("logging has started")