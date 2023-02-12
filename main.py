#!/usr/local/bin/python
"""
Author: Edmund Bennett
Copyright 2023
"""

import uvicorn

import example.controllers.bootstrap as bootstrap


app = bootstrap.server


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=bootstrap.host,
        port=bootstrap.port,
        reload=True,
    )
