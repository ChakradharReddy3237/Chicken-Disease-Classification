import os
import box.exceptions import BoxValueError
import yaml
import cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import Box, ConfigBox
from pathlib import Path
from typing import Any, Union, List, Dict
import base64

@ensure_annotations
def create_directories(path_to_directories: List[Union[str, Path]], verbose: bool = True) -> None:
    """
    Create multiple directories if they don't exist.

    Args:
        path_to_directories (List[str | Path]): List of directory paths to create.
        verbose (bool): If True, logs directory creation.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")

@ensure_annotations
def save_json(path: Union[str, Path], data: Dict) -> None:
    """
    Save a Python dictionary to a JSON file.

    Args:
        path (str | Path): Path to the JSON file.
        data (dict): Dictionary to save.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"JSON file saved at: {path}")

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> dict:
    """Reads a YAML file and returns its content as a regular Python dict.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty.
        Exception: If there's any other issue with reading the file.

    Returns:
        dict: Parsed YAML data.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            if content is None:
                raise ValueError(f"YAML file is empty: {path_to_yaml}")
            logger.info(f"YAML file loaded successfully: {path_to_yaml}")
            return content

    except Exception as e:
        logger.error(f"Error reading YAML file: {e}")
        raise e

def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImage(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read()).decode('utf-8')
