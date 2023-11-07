#!/usr/bin/python3
"""This is To JSON string Module """
import json


def to_json_string(my_obj):
    """
   Converts object to JSON.
    Args:
        my_obj: The pbject.
    Returns: The JSON representation of an object (string).
    """
    return (json.dumps(my_obj))
