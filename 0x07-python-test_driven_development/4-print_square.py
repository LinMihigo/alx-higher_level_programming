#!/usr/bin/python3
"""Define a func that prints a square with # """


def print_square(size):
    """
    Prints a square with #

    Args:
        size (int): the length of a square

    Raises:
        TypeError:
            - If size is not an integer
            - If size is a float and less than 0
        ValueError: if size is less 0

    Returns:
        None
    """
    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
