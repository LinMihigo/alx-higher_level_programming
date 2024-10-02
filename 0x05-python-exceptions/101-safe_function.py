#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """Executes a function safely, handling any exceptions.

    Args:
        fct: A pointer to the function to execute.
        *args: Arguments to pass to the function.

    Returns:
        The result of the function execution if successful, otherwise None.
    """
    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
