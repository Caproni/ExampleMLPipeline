#!/usr/local/bin/python
"""
Author: Edmund Bennett
Copyright 2023
"""

from ..pipeline.file_manipulation.load_model import load_model
from ..utils.logger import logger as log


try:
    example_model = load_model(
        directory="./staging",
        model_name="test",
    )
except IOError as e:
    log.critical(f"Model was not available. Error: {e}")
