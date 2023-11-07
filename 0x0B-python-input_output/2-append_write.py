#!/usr/bin/python3
"""This is Append to a file Module """


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8).
    Args:
        filename: The name of the file.
        text: Text to be written.
    Returns: the number of characters written
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
