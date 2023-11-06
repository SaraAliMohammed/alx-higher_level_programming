#!/usr/bin/python3
"""This is Rectangle Module """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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

    def area(self):
        """rectangle area"""
        return (self.__width * self.__height)

    def __str__(self):
        """String method of Rectangle"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
