#!/usr/bin/python3
"""This is Lookup Module"""


def lookup(obj):
    """
    Looks up attributes and methods
    of an object
    Args:
        obj: The object to look up.
    Returns: The list of available attributes
        and methods of an object.
    """
    return (dir(obj))
