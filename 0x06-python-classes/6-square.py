#!/usr/bin/python3
"""Square Module"""


class Square:
    """Defines Square class

    Args:
        size: Private instance attribute,
        size must be an intege and greater than 0.
        position (int, int): The position of the new square.

    methods:
        area: gets the square area.
        size setter and getter.
        my_print: Print the square with the # character.
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(position, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size ** 2

    def my_print(self):
        """Print the square with the # character."""
        for i in range(self.__position[1]):
            print("")
        for i in range(self.size):
            for k in range(self.__position[0]):
                print("_", end="")
            for j in range(self.size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
