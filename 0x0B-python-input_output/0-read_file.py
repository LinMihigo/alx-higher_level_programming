#!/usr/bin/python3
"""Define the read_file function"""


def read_file(filename=""):
    """
    Reads a text file and prints it to stdout

    Args:
        filename (string): name of file to read.

    Returns:
        None
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read())
