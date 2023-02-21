#!/usr/local/bin/python
"""
Author: Edmund Bennett
Copyright 2023
"""

from typing import Union, Dict, Any


def return_json(
    message,
    success: bool = True,
    content: Union[str, bytes, Dict[str, Any]] = None,
):
    """
    Convenience wrapper for ASGI return objects
    """
    resp_dict = {
        "success": success,
        "message": message,
    }

    if content:
        resp_dict.update({"content": content})

    return resp_dict
