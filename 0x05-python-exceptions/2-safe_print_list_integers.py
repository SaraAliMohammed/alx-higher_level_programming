#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """prints the first x elements of a list and only integers.
    All elements must be printed on the same line followed by a new line.

    Args:
        my_list (list): The list to print elements from.
        x: The number of elements to access in my_list.

    Returns:
        The real number of integers printed
    """
    length = 0
    for i in range(x):
        try:
            if length < x:
                print("{:d}".format(my_list[i]), end="")
                length = length + 1
        except (TypeError, ValueError):
            continue
    print()
    return length
