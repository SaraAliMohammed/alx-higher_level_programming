#!/usr/bin/python3
"""Square Module"""


class Square:
    """Defines Square class

    Args:
        size: Private instance attribute,
        size must be an intege and greater than 0.
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
