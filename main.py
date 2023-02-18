#!/usr/local/bin/python
"""
Author: Edmund Bennett
Copyright 2023
"""

import uvicorn

import example.controllers.bootstrap as bootstrap
from example.pipeline.run_pipeline import run_pipeline


app = bootstrap.server


if __name__ == "__main__":

    run_pipeline(
        model_directory=bootstrap.model_directory,
    )

    uvicorn.run(
        "main:app",
        host=bootstrap.host,
        port=bootstrap.port,
        reload=True,
    )
