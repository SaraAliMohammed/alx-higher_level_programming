#!/usr/bin/python3
"""This is Square Module """


class Square(Rectangle):
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
