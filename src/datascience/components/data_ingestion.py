import urllib.request as request
from src.datascience.entity.config_entity import DataIngestionConfig
from src.datascience import logger
import zipfile
import os



class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                self.config.source_URL, self.config.local_data_file
            )
            logger.info(f"File downloaded successfully: {filename}")
        else:
            logger.info(f"File already exists: {self.config.local_data_file}")

    def extract_zip_file(self):


        unzip_dir = self.config.unzip_dir
        if not os.path.exists(unzip_dir):
            os.makedirs(unzip_dir)
            logger.info(f"Directory created: {unzip_dir}")
            
        if os.path.exists(self.config.local_data_file):
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(self.config.unzip_dir)
            logger.info(f"File extracted successfully to: {self.config.unzip_dir}")
        else:
            logger.error(f"File does not exist: {self.config.local_data_file}")