#!/usr/local/bin/python
"""
Author: Edmund Bennett
Copyright 2023
"""

from typing import Optional, Tuple
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from ...utils.logger import logger as log


def create_ensemble_model(
    xs: pd.DataFrame,
    y: pd.DataFrame,
    test_size: float,
    n_estimators: int,
    max_depth: Optional[int],
    random_state: int,
) -> Tuple[object, float]:
    log.info("Calling create_ensemble_model")

    xs_train, xs_test, y_train, y_test = train_test_split(
        xs,
        y,
        test_size=test_size,
        random_state=random_state,
    )

    rfc = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        random_state=random_state,
    )

    rfc_fitted = rfc.fit(
        xs_train,
        y_train.values.ravel(),
        sample_weight=None,
    )

    score = rfc_fitted.score(xs_test, y_test)

    return rfc_fitted, score
