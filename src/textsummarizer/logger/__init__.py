import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

directory_path = os.path.join(os.getcwd(),'logs')
os.makedirs(directory_path,exist_ok=True)

complete_file_path = os.path.join(directory_path,LOG_FILE)

logging_format = '%(asctime)s - %(levelname)s - %(message)s'

logging.basicConfig(level= logging.INFO, filename= complete_file_path ,format= logging_format)

