#!/usr/bin/python3
"""This is Exact same object Module """


def is_same_class(obj, a_class):
    """
    Checks type of object
    Args:
        obj: object to be checks.
        a_class: The class.
    Returns:
        True if the object is exactly an instance of the specified class
        otherwise False.
    """
    return (type(obj) == a_class)
