#!/usr/bin/python3
"""This is Read file Module """


def read_file(filename=""):
    """
    reads a text file (UTF8) and prints it to stdout.
    Args:
        filename: The name of the file.
    """
    with open(filename, 'r') as file:
        data = file.read()
    print(data)
