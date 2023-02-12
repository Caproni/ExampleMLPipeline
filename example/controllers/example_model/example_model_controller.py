#!/usr/local/bin/python
"""
Author: Edmund Bennett
Copyright 2023
"""

from fastapi import APIRouter
from pydantic import BaseModel

from example.utils.return_json import return_json
from example.utils.logger import logger as log


router = APIRouter()


class ExampleModelInputs(BaseModel):
    """
    Pydantic model for example model inputs
    """
    ...


@router.get("/api/getExampleModelPrediction")
def get_example_model_prediction(
    model_inputs: ExampleModelInputs,
):
    """
    Get example model prediction
    """
    log.info("Calling get_example_model_prediction")

    try:
        ...

        if ...:
            return return_json(
                message="Successfully selected family-tree person data.",
                success=True,
                content=...,
            )
    except Exception as e:
        log.critical(f"Failed to get model response. Error: {e}")
        return return_json(
            message="Failed to get model response.",
            success=False,
            response_code=500,
        )

    log.critical(f"Failed to get model response. Check logs for details.")
    return return_json(
        message="Failed to get model response.",
        success=False,
        response_code=500,
    )
