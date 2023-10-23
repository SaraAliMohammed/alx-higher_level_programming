#!/usr/bin/python3

def safe_print_integer_err(value):
    """prints an integer with "{:d}".format().

    Args:
        value: Integer number that will be printed.

    Returns: True if value has been correctly printed
        Otherwise, returns False in TypeError or ValueError
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
