#!/usr/bin/python3
"""Square Module"""


class Square:
    """Defines Square class

    Args:
        size: Private instance attribute,
        size must be an intege and greater than 0.

    methods:
        area: gets the square area.
        size setter and getter.
        my_print: Print the square with the # character.
    """
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Print the square with the # character."""
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
