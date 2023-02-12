#!/usr/local/bin/python
"""
Author: Edmund Bennett
Copyright 2023
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from example.controllers.example_model import example_model_controller

port = 4646
host = "localhost"

server = FastAPI()

server.include_router(example_model_controller.router, tags=["Example Model"])


origins = [
    "http://localhost",
    "https://localhost:443",
    "http://localhost:4200",
]

server.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
