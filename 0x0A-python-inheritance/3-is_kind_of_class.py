#!/usr/bin/python3
"""This is Same class or inherit from Module """


def is_kind_of_class(obj, a_class):
    """
    Checks type of object
    Args:
        obj: object to be checks.
        a_class: The class.
    Returns:
        True if the object is an instance of,
        or if the object is an instance of a class that inherited from,
        the specified class ; otherwise False.
    """
    return (isinstance(obj, a_class))
