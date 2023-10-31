#!/usr/bin/python3
"""print_square Module"""


def print_square(size):
    """
    Prints a square with the character #.
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be a non-negative integer')
    if size == 0:
        return
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
