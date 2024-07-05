from src.textsummarizer.logger import logging
from src.textsummarizer.exception import CustomException
import sys
import os

# unit test for log
logging.info('A log unit test.')
#unit  test for exception
try:
    a = 1/0

except Exception as e:
    raise CustomException(e,sys)
