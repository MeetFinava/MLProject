import sys
from dataclasses import dataclass  

import numpy as np  
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exception import CustomeException
from src.logger import logging

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"preprocessor.pkl")
    
class DataTransformtion:
    def __init__(self):
        self.data_tranformation_congfig=DataTransformationConfig()
        
    def get_data_transformer_object():
        
        '''
        This Function is Responsible for Data Transformation 
        
        '''


        try:
            numerical_colums=["reading_score","writing_score"]
            catagoriacal_colum=[
            "gender",
            "race_ethnicity",
            "parental_level_of_education",
            "lunch",
            "test_preparation_course",
            ]
            
            num_pipline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(statergy="median")),
                    ("Scler",StandardScaler)
                ]
            )
            
            cat_pipline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(statergy="most_frequent")),
                    ("one_hot_encoder",OneHotEncoder()),
                    ("Scaler",StandardScaler())
                ]
            )
            
            logging.info(f"numerical Columns {numerical_colums}")
            
            logging.info(f"Catogorical Columns {catagoriacal_colum}")
            
            preprocessor=ColumnTransformer(
                [
                    ("Num_pipline",num_pipline,numerical_colums),
                    ("Cat_pipline",cat_pipline,catagoriacal_colum)
                ]
            )
            
            return preprocessor
            
        except Exception as e:
            raise CustomeException(e,sys)
        
        
def initiate_data_transformation(self,train_path,test_path):
    try:
        test_df=pd.read_csv(test_path)
        train_df=pd.read_csv(train_path)
        
        logging.info("Read Trian and test Data Completed")
        
        logging.info("Obtaining Preprocessing Object")
        
        preprocessing_obj=self.get_data_transformer_object()
        
        target_column_name="math_score"
        
        numerical_colums=["reading_score","writing_score"]
        
        input_features_train_df=train_df.drop(columns=[target_column_name],axis=1)
        target_features_train_df=train_df[target_column_name]
        
        input_features_test_df=test_df.drop(columns=[target_column_name],axis=1)
        target_features_test_df=test_df[target_column_name]
        
        
        logging.info(
            f"Applying preprocessing on trainDataset and test dataset"
        )
        
        input_features_train_array=preprocessing_obj.fit_transform(input_features_train_df)
        input_features_test_array=preprocessing_obj.transform(input_features_test_df)
        
        
        train_arr=np.c_[
            input_features_train_array,np.array(input_features_train_df)
        ]
        test_arr=np.c_=[
            input_features_test_array,np.array(input_features_test_df)
        ]
        
        logging.info("Saved Preprocessing object")
        
        save_object(
            file_path=self.data_transformation_config.preprocessor_obj_file_path,
            obj=preprocessing_obj
        )

        return(
            train_arr,
            test_arr,
            self.data_transformation_config.preprocessor_obj_file_path,
                
        )
             
    except:
        pass