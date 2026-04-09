from src.CapstonMLPro.logger import logging
from src.CapstonMLPro.exception import CustomException
from src.CapstonMLPro.components.data_ingestion import DataIngestion
from src.CapstonMLPro.components.data_ingestion import DataIngestionConfig


import sys

if __name__ =="__main__":
    logging.info("The execution has started")
    
try:
   #dataIngestionConfig = DataIngestionConfig()
    dataIngestion =DataIngestion()  
    print(dir(dataIngestion)) 
    dataIngestion.initiate_data_ingestion()

except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e, sys)