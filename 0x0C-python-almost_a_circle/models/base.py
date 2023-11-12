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

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string
        representation.
        Args:
            json_string: A string representing a list of dictionaries.
        """
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation
        of list_objs to a file.
        Args:
            cls: The class name.
            list_objs: A list of instances who inherits of Base.
        """
        file_name = "{}.json".format(cls.__name__)
        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all
        attributes already set
        Args:
            cls: The class name.
            dictionary: A double pointer to a dictionary.
        """
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            instance = Rectangle(1, 1)
        elif cls is Square:
            instance = Square(1)
        else:
            instance = None
        instance.update(**dictionary)
        return instance
