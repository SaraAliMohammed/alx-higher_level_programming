#!/usr/bin/python3
"""This is To JSON string Module """
import json


def from_json_string(my_str):
    """
   Converts Python data struc.ture.
    Args:
        my_str: The pbject.
    Returns: An object (Python data structure) represented by
    a JSON string.
    """
    return (json.loads(my_str))
