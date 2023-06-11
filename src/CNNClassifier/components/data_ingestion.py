import os
from CNNClassifier import logger
import zipfile
import boto3
from pathlib import Path
from CNNClassifier.utils.common import get_size
from CNNClassifier.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            s3_client = boto3.client('s3', aws_access_key_id= self.config.aws_access_key,
                         aws_secret_access_key=self.config.aws_secret_key)
            s3_client.download_file(self.config.bucket_name, self.config.bucket_filename,  self.config.local_data_file)
            logger.info(f"{self.config.local_data_file} download from S3 ! with following bucket: {self.config.bucket_name}")            
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")  

            
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path , exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            logger.info("Extracting the Zip Files and stores inside the Artifcats Folder")
        