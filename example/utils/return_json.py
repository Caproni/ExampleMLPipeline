#!/usr/local/bin/python
"""
Author: Edmund Bennett
Copyright 2023
"""

from typing import Union


def return_json(
    message,
    success: bool = True,
    response_code: int = 200,
    content: Union[str, bytes] = None,
):
    """
    Convenience wrapper for ASGI return objects
    """
    resp_dict = {
        "success": success,
        "message": message,
        "response_code": response_code,
    }

    if content:
        resp_dict.update({"content": content})

    return resp_dict
