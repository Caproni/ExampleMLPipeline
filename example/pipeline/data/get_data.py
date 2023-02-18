#!/usr/local/bin/python
"""
Author: Edmund Bennett
Copyright 2023
"""

import numpy as np
import pandas as pd
from sklearn.datasets import load_wine

from ...utils.logger import logger as log


def get_data() -> pd.DataFrame:
    log.info("Calling get_data")
    data = load_wine(as_frame=True)
    return pd.DataFrame(
        np.concatenate((data.data, np.array([data.target]).T), axis=1),
        columns=data.feature_names + ["target"],
    )
