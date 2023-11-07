#!/usr/bin/python3
"""This is Write to a file Module """


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8).
    Args:
        filename: The name of the file.
        text: Text to be written.
    Returns: the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
    return(len(text))
