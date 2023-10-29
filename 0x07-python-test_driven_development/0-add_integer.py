#!/usr/bin/python3
""" add_integer Module """


def add_integer(a, b=98):
    """
    Add two numbers.
    This function takes two numbers 'a', and 'b' and return
    their sum.

    Args:
        a: the first integer.
        b: the second integer, default value is 98.

    Raises:
        TypeError: if a, b are not int or float.

    Returns:
        The sum of the two integers.
    """

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile('tests/0-add_integer.txt')
