from pathlib import Path
import os
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')

project_name = "dataproject"

list_of_file = [
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/conponents/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging//__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",    
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    
   "config/config.yaml",
    "schema.yaml",
    "main.py",
    "templates/index.html",
    "params.yaml",
    "app.py",
    "Dockerfile",
    "requirements.txt",  # Fixed typo
    "setup.py",
    "research/trails.ipynb",
    "test.py"
]

for filepath in list_of_file:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    if (not filepath.exists()) or (filepath.stat().st_size == 0):
        filepath.touch()
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")