import os
import sys
sys.path.append('D:\\MLPROJECT\\src')
from exception import CustomeException
from logger import logging
import pandas as pd
 
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    raw_data_path: str=os.path.join('artifacts',"raw.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method of componet")
        try:
            df=pd.read_csv('notebook\data\stud.csv')
            logging.info('read The dataset as dataframe')
        except:
            pass