from pathlib import Path
import os


CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")
AWS_ACCESS_KEY = os.getenv('TJ_Dataset_AccessID')
AWS_SECRET_KEY  = os.getenv('TJ_Dataset_Secretkey')

