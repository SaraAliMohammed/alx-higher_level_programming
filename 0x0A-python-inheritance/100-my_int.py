#!/usr/bin/python3
"""This is MyInt Module """


class MyInt(int):
    """
    MyInt Class.
    rebel version of an integer class
    """
    def __new__(cls, *args, **kwargs):
        """creates a new instance of MyInt class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, value):
        """!= which is opposite of =="""
        return int(self) != value

    def __ne__(self, value):
        """== which is opposite of !="""
        return int(self) == value
