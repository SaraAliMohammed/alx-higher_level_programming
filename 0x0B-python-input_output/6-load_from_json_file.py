#!/usr/bin/python3
"""This is  Create object from a JSON file Module """
import json


def load_from_json_file(filename):
    """
    Creates an Object from a "JSON file".
    Args:
        filename: The name of the file.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
