#!/usr/bin/python3
"""This is Class to JSON Module """


def class_to_json(obj):
    """
    Args:
        obj: An instance of a Class.
    Returns:
        the dictionary description with simple data structure
        (list, dictionary, string, integer and boolean)
        for JSON serialization of an object
    """
    return obj.__dict__
