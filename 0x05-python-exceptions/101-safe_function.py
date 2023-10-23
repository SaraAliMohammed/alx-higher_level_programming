#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """Executes a function safely.

    Args:
        fct: A pointer to a function

    Returns:
        The result of the function
        otherwise None if something happens during the function
        and prints in stderr the error precede by Exception:
    """
    try:
        result = fct(*args)
        return (result)
    except Exception:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
