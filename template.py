import os 
import logging  
from pathlib import Path 


logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s: ")

list_of_files = [
    "src/__init__.py" , 
    "src/prompt.py" , 
    "src/helper.py" , 
    ".env" ,
    "app.py",
    "setup.py" ,
    "data/" 
    "research/trial.ipynb"
] 

for filepath in list_of_files: 
    filepath = Path(filepath) 
    filedir , filename = os.path.split(filepath)

    if filedir !="": 
        os.makedirs(filedir , exist_ok=True) 
        logging.info(f"folder created :{filedir} for file {filename}") 

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0): 
        with open(filepath , "w") as f:
            pass 
            logging.info(f"creating empty file : {filepath}") 

    else: 
        logging.info(f"{filepath} already exists...!")
