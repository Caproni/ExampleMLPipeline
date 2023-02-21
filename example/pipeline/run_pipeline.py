#!/usr/local/bin/python
"""
Author: Edmund Bennett
Copyright 2023
"""

from statistics import median

from .data.get_data import get_data
from .feature_engineering.filter_data import filter_data
from .feature_engineering.select_target_variable import select_target_variable
from .feature_engineering.transform_features import transform_features
from .train_validate_test.create_ensemble_model import create_ensemble_model
from .file_manipulation.save_model import save_model
from ..vizualisation.create_histogram import create_histogram
from ..utils.logger import logger as log


def run_pipeline(
    model_directory: str,
):

    data = get_data()

    selected_data = filter_data(data)
    engineered_data = transform_features(selected_data)
    xs, y = select_target_variable(engineered_data, ["target"])

    model, score = create_ensemble_model(
        xs,
        y,
        test_size=0.8,
        n_estimators=100,
        max_depth=None,
        random_state=42,
    )

    save_model(
        directory=model_directory,
        model_name="test",
        model=model,
        overwrite=True,
    )
