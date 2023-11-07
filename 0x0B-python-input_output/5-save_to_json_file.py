#!/usr/bin/python3
"""This is Save Object to a file Module """
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a
    JSON representation
    Args:
        my_obj: The pbject.
        filename: The name of the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
