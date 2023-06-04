from setuptools import setup, find_packages
from typing import List
import setuptools

with open("README.md" , "r") as f:
    long_description = f.read()

PROJECT_NAME = "CNNClassifier"
VERSION = "0.0.1"
AUTHOR = "Karthik Saran"
HYPHEN_E_DOT = "-e ."
REQUIREMENT_FILE_NAME = "requirements.txt"
AUTHOR_NAME = "Karthiksaran-001"
AUTHOR_EMAIL = "mailmekarthik001@gmail.com"
REPO_NAME = "Tom-Jerry_Classification"

def get_requirements_list()->List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list


setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description= "A Small Package for CNN Classification",
author_email= AUTHOR_EMAIL,
URL = f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
long_description = long_description,
packages=find_packages(where="src"), 
install_requires=get_requirements_list(),
package_dir={"": "src"}
)