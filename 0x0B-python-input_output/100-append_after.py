#!/usr/bin/python3
"""This is Search and update Module """


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after
    each line containing a specific string.
    Args:
        filename: The file name.
        search_string: The string to search.
        new_string: The new string will be added.
    """
    with open(filename, "r", encoding="utf-8") as file:
        lines = []
        for line in file:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)
    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(lines)
