#!/usr/bin/python3
"""This is Square Module """
Rectangle = __import__('9-rectangle').Rectangle


class Square(BaseGeometry):
    """
    Square Class
    """
    def __init__(self, size):
        """Intialize Square instance"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Square area"""
        return (self.__size ** 2)

    def __str__(self):
        return ("[Square] " + str(self.__width) + "/" + str(self.__height))
