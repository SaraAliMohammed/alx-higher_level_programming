#!/usr/bin/python3
"""This is Student to disk and reload Module """


class Student:
    """Student Class"""
    def __init__(self, first_name, last_name, age):
        """Constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        att_dict = dict()
        for k, v in self.__dict__.items():
            if k in attrs:
                att_dict[k] = v
        return att_dict

    def reload_from_json(self, json):
        """ Replaces all attributes of the Student instance"""
        for k, v in json.items():
            if k in self.__dict__:
                self.__dict__[k] = v
