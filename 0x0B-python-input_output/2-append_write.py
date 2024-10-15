#!/usr/bin/python3
"""Defining the append_write function"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and returns the number
    of characters added.

    If the file doesn't exist, it will be created.

    Args:
        filename (str): The name of the file to append to. Default is an empty
        string.
        text (str): The text to append to the file. Default is an empty string.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
