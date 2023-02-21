#!/usr/local/bin/python
"""
Author: Edmund Bennett
Copyright 2023
"""

from typing import Dict, List, Any
import pandas as pd
from fastapi import APIRouter, Response
from pydantic import BaseModel

from ..load_models import example_model
from ...utils.return_json import return_json
from ...utils.logger import logger as log


router = APIRouter()


class ExampleModelParameters(BaseModel):
    alcohol: float
    malic_acid: float
    ash: float
    alcalinity_of_ash: float
    magnesium: float
    total_phenols: float
    flavanoids: float
    nonflavanoid_phenols: float
    proanthocyanins: float
    color_intensity: float
    hue: float
    od280_od315_of_diluted_wines: float
    proline: float

    def create_model_dict(self) -> Dict[str, Any]:
        return {
            "alcohol": self.alcohol,
            "malic_acid": self.malic_acid,
            "ash": self.ash,
            "alcalinity_of_ash": self.alcalinity_of_ash,
            "magnesium": self.magnesium,
            "total_phenols": self.total_phenols,
            "flavanoids": self.flavanoids,
            "nonflavanoid_phenols": self.nonflavanoid_phenols,
            "proanthocyanins": self.proanthocyanins,
            "color_intensity": self.color_intensity,
            "hue": self.hue,
            "od280/od315_of_diluted_wines": self.od280_od315_of_diluted_wines,
            "proline": self.proline,
        }


class ExampleModelInputs(BaseModel):
    """
    Pydantic model for example model inputs
    """
    username: str
    data: List[ExampleModelParameters]

    def create_dict(self):
        return {
            "data": [datum.create_model_dict() for datum in self.data],
            "username": self.username,
        }

    def create_df(self) -> pd.DataFrame:
        df = pd.DataFrame([datum.create_model_dict() for datum in self.data])
        return df


@router.post("/api/getExampleModelPrediction")
def get_example_model_prediction(
    model_inputs: ExampleModelInputs,
    response: Response,
):
    """
    Get example model prediction
    """
    log.info("Calling get_example_model_prediction")

    # check inputs

    content = {
        "username": model_inputs.username,
        "data": []
    }

    for model_input in model_inputs.data:
        issues = {}
        make_prediction = True
        if not (10.0 <= model_input.alcohol <= 20.0):
            log.warning(f"Alcohol not within acceptable thresholds.")
            make_prediction = False
            issues.update({"alcohol": [10.0, 20.0]})
        if not (10.0 <= model_input.malic_acid <= 20.0):
            log.warning(f"Malic acid not within acceptable thresholds.")
            make_prediction = False
            issues.update({"malic_acid": [10.0, 20.0]})
        if not (10.0 <= model_input.ash <= 20.0):
            log.warning(f"Ash not within acceptable thresholds.")
            make_prediction = False
            issues.update({"ash": [10.0, 20.0]})
        if not (10.0 <= model_input.alcalinity_of_ash <= 20.0):
            log.warning(f"Alcalinity of Ash not within acceptable thresholds.")
            make_prediction = False
            issues.update({"alcalinity_of_ash": [10.0, 20.0]})
        if not (10.0 <= model_input.magnesium <= 20.0):
            log.warning(f"Magnesium not within acceptable thresholds.")
            make_prediction = False
            issues.update({"magnesium": [10.0, 20.0]})
        if not (10.0 <= model_input.total_phenols <= 20.0):
            log.warning(f"Total Phenols not within acceptable thresholds.")
            make_prediction = False
            issues.update({"total_phenols": [10.0, 20.0]})
        if not (10.0 <= model_input.flavanoids <= 20.0):
            log.warning(f"Flavanoids not within acceptable thresholds.")
            make_prediction = False
            issues.update({"flavanoids": [10.0, 20.0]})
        if not 10.0 <= model_input.nonflavanoid_phenols <= 20.0:
            log.warning(f"Nonflavanoid Phenols not within acceptable thresholds.")
            make_prediction = False
            issues.update({"nonflavanoid_phenols": [10.0, 20.0]})
        if not 10.0 <= model_input.proanthocyanins <= 20.0:
            log.warning(f"Proanthocyanins not within acceptable thresholds.")
            make_prediction = False
            issues.update({"proanthocyanins": [10.0, 20.0]})
        if not 10.0 <= model_input.color_intensity <= 20.0:
            log.warning(f"Color Intensity not within acceptable thresholds.")
            make_prediction = False
            issues.update({"color_intensity": [10.0, 20.0]})
        if not 10.0 <= model_input.hue <= 20.0:
            log.warning(f"Hue not within acceptable thresholds.")
            make_prediction = False
            issues.update({"hue": [10.0, 20.0]})
        if not 10.0 <= model_input.od280_od315_of_diluted_wines <= 20.0:
            log.warning(f"OD280/OD315 of Diluted Wines not within acceptable thresholds.")
            make_prediction = False
            issues.update({"od280_od315_of_diluted_wines": [10.0, 20.0]})
        if not 10.0 <= model_input.proline <= 20.0:
            log.warning(f"Proline not within acceptable thresholds.")
            make_prediction = False
            issues.update({"proline": [10.0, 20.0]})

        this_payload = {
            "inputs": model_input.create_model_dict(),
            "issues": issues,
            "make_prediction": make_prediction,
        }

        if make_prediction:
            input_df = model_inputs.create_df()
            prediction = example_model.predict(input_df)
            this_payload["prediction"] = list(prediction)[0]

        content["data"].append(this_payload)

    return return_json(
        message="Successfully queried model.",
        success=True,
        content=content,
    )
