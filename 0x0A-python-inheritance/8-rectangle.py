#!/usr/bin/python3
"""This is Rectangle Module """


class Rectangle(BaseGeometry):
    """
    Rectangle Class
    """
    def __init__(self, width, height):
        """Intialize Rectangle instance"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
