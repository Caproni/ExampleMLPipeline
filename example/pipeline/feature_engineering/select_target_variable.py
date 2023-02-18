#!/usr/local/bin/python
"""
Author: Edmund Bennett
Copyright 2023
"""

from typing import List, Tuple
import pandas as pd

from ...utils.logger import logger as log


def select_target_variable(input_data: pd.DataFrame, targets: List[str]) -> Tuple[pd.DataFrame, pd.DataFrame]:
    log.info("Calling select_target_variable")
    return input_data.drop(targets, axis=1, inplace=False), input_data[targets]
