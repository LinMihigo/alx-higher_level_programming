#!/usr/bin/python3
"""Defining a func that prints text with 2 new lines after '.', '?', and ':'"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after '.', ',' and ':'

    Args:
        text (str): string to process

    Raises:
        TypeError: if text not a string

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    # Skip leading spaces
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")

        if text[c] in "\n.?:":
            if text[c] in ".?:":
                print("\n")
            c += 1

            while c < len(text) and text[c] == ' ':
                c += 1
        else:
            c += 1
