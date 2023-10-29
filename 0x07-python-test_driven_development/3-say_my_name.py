#!/usr/bin/python3
""" Say_my_name Module """


def say_my_name(first_name, last_name=""):
    """
    Say my name.
    This function takes two parameters 'first_name', and
    'last_name' and prints My name is <first name> <last name>

    Args:
        first_name: the first name.
        last_name: the last name.

    Raises:
        TypeError: with message first_name must be a string
        or last_name must be a string.
    """

    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print("My name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile('tests/3-say_my_name.txt')
