#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """prints x elements of a list.
    All elements must be printed on the same line followed by a new line.

    Args:
        my_list (list): The list to print elements from.
        x: x represents the number of elements to print.

    Returns:
        The number of elements printed.
    """
    length = 0
    for i in range(x):
        try:
            if length < x:
                print(my_list[i], end="")
            length = length + 1
        except IndexError:
            break
    print()
    return length
