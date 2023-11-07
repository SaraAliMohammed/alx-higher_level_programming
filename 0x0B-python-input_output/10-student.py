#!/usr/bin/python3
"""This is Student to JSON Module """


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
        for k, v in self.__dict__:
            if k in attrs:
                att_dict[k] = v
        return att_dict
