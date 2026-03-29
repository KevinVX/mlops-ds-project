import urllib.request as request
from src.datascience.entity.config_entity import DataValidationConfig
from src.datascience import logger
import zipfile
import os
import pandas as pd



class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
    
    def validate_all_columns(self) -> bool:
        try:
            validation_status = True
            data = pd.read_csv(self.config.unzip_data_dir)
            
            for column in self.config.all_schema.keys():
                if column not in data.columns:
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Column {column} is not present in the data")
                    validation_status = False

            if validation_status:
                with open(self.config.STATUS_FILE, "w") as f:
                    f.write("Data validation: True")
            return validation_status
        
        except Exception as e:
            logger.exception(e)
            raise e