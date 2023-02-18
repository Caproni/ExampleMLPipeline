#!/usr/local/bin/python
"""
Author: Edmund Bennett
Copyright 2023
"""

from joblib import load
from os.path import join, isfile, abspath

from ...utils.logger import logger as log


def load_model(
    directory: str,
    model_name: str,
):
    log.info("Calling load_model")
    path_to_model = abspath(join(directory, f"{model_name}.joblib"))
    if isfile(path_to_model):
        log.warning(f"Loading model at: {path_to_model}")
        with open(path_to_model, "rb") as model_file:
            return load(model_file)
