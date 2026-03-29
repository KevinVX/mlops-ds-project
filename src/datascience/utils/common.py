import os
from pathlib import Path
import yaml
from src.datascience import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from typing import Any
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(file_path: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its contents as a ConfigBox object.

    Args:
        file_path (str): The path to the YAML file.
    Returns:
        ConfigBox: The contents of the YAML file as a ConfigBox object.
    """
    try:
        with open(file_path, 'r') as yaml_file:
            yaml_content = yaml.safe_load(yaml_file)
            return ConfigBox(yaml_content)
    except BoxValueError as e:
        logger.exception(f"Error reading YAML file: {e}")
        raise
    except Exception as e:
        logger.exception(f"Unexpected error occurred: {e}")
        raise

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict) -> None:
    """
    Saves data to a JSON file.

    Args:
        path (str): The path to the JSON file.
        data (Any): The data to be saved in JSON format.
    """
    try:
        with open(path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
            logger.info(f"Data successfully saved to {path}")
    except Exception as e:
        logger.exception(f"Error saving JSON file: {e}")
        raise

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Loads data from a JSON file.

    Args:
        path (str): The path to the JSON file.
    Returns:
        ConfigBox: The data loaded from the JSON file.
    """
    try:
        with open(path, 'r') as json_file:
            data = json.load(json_file)
            logger.info(f"Data successfully loaded from {path}")
            return ConfigBox(data)
    except Exception as e:
        logger.exception(f"Error loading JSON file: {e}")
        raise

@ensure_annotations
def save_bin(data: Any, path: Path) -> None:
    """
    Saves data to a binary file using joblib.

    Args:
        data (Any): The data to be saved.
        path (str): The path to the binary file.
    """
    try:
        joblib.dump(data, path)
        logger.info(f"Data successfully saved to {path}")
    except Exception as e:
        logger.exception(f"Error saving binary file: {e}")
        raise