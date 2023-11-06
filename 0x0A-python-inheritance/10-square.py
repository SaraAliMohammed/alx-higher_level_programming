#!/usr/bin/python3
"""This is Square Module """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """
    Square Class
    """
    def __init__(self, size):
        """Intialize Square instance"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Square area"""
        return (self.__size * self.__size)
