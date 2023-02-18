#!/usr/local/bin/python
"""
Author: Edmund Bennett
Copyright 2023
"""

from os import remove
from os.path import isfile, join, abspath

from ...utils.logger import logger as log


def delete_model(
    directory: str,
    model_name: str,
):
    log.info("Calling delete_model")
    path_to_model = abspath(join(directory, f"{model_name}.joblib"))
    if isfile(path_to_model):
        log.warning(f"Deleting file at: {path_to_model}")
        remove(path_to_model)
