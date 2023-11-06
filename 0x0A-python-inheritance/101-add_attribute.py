#!/usr/bin/python3
"""This is Can I? Module """


def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object if it’s possible.
    Args:
        obj: The object to add attribute to.
        name: Attribute name.
        value: The new attribute value.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
