#!/usr/bin/python3
"""This is a Base Module"""
import json


class Base:
    """
        This class will be the “base” of all other classes.
        The goal of it is to manage id attribute in all your future
        classes and to avoid duplicating the same code
        (by extension, same bugs)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if (id):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Dictionary to JSON string
        Args:
            list_dictionaries: A list of dictionaries.
        Returns:
            The JSON string representation of list_dictionaries,
            "[]" If list_dictionaries is None or empty,
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
