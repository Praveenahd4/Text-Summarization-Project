import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "textSummarization"

list_of_files =[
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constant/__init__.py", 
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"      
]

for filepaths in list_of_files:
    filepaths = Path(filepaths)
    filedir, filename = os.path.split(filepaths)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file: {filename}")

    if(not os.path.exists(filepaths)) or (os.path.getsize(filepaths) == 0):
        with open(filepaths, "w") as f:
            pass
        logging.info(f"Created file: {filepaths}")
    
    else:
        logging.info(f"File: {filepaths} already exists")
