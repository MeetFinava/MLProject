import os
import sys
import dill
sys.path.append('D:\\MLPROJECT\\src')
 
import numpy as np
import pandas as pd

from exception import CustomeException

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        
        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)
        
    except Exception as e:
        raise CustomeException(e,sys)