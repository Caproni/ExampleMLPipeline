#!/usr/local/bin/python
"""
Author: Edmund Bennett
Copyright 2023
"""

from typing import Any
from joblib import dump
from os.path import isfile, join, abspath

from .delete_model import delete_model
from ...utils.logger import logger as log


def save_model(
    directory: str,
    model_name: str,
    model: Any,
    overwrite: bool = False,
):
    log.info("Calling save_model")
    path_to_model = abspath(join(directory, f"{model_name}.joblib"))

    if overwrite and isfile(path_to_model):
        delete_model(directory, model_name)

    if not isfile(path_to_model):
        with open(path_to_model, "wb") as model_file:
            dump(model, model_file, compress=9)
    else:
        log.warning(f"Model not saved. An existing model was found at: {path_to_model}")
