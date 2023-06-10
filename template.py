
'''
This File Help to Create a Project Structure Using Python

Author : Karthik Saran
Date : 2023 - 06 -04
'''

import os
import logging
from pathlib import Path


logging.basicConfig(level=logging.INFO , format='[%(asctime)s]:  %(message)s: ')


ListOfFiles =[
    ".github/workflows/.gitkeep",
    f"src/{ProjectName}/__init__.py",
    f"src/{ProjectName}/components/__init__.py",
    f"src/{ProjectName}/utils/__init__.py",
    f"src/{ProjectName}/config/configuration.py",
    f"src/{ProjectName}/pipeline/__init__.py",
    f"src/{ProjectName}/entity/__init__.py",
    f"src/{ProjectName}/constant/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "README.md",
    'setup.py',
    'requirements.txt',
    'research/test.ipynb',
    "templates/index.html",
]

for file_path in ListOfFiles:
    file_path = Path(file_path)
    file_dir , file = os.path.split(file_path)
    if file_dir != "":
        os.makedirs(file_dir , exist_ok=True)
        logging.info(f"\t\t\t Created Directory : {file_dir} \n")

    if not(os.path.exists(file_path))  or (os.path.getsize(file_path) == 0):
        with open(file_path , "w") as f:
            pass
        logging.info(f"\t\t\t Created empty File : {file_path} \n")

    else:
        logging.info(f"\t\t\t File already exists : {file_path} \n")

