#!/usr/bin/python3
"""Defining a func that prints a string containing first and last name"""


def say_my_name(first_name, last_name=""):
    """
    Prints a string containing first and last names

    Args:
        first_name (string): first name string
        last_name (string): last name string

    Raises:
        TypeError:
            - if first_name is not a string
            - if last_name is not a string
    Returns:
        string: a sentence containing first and last names
    """
    if isinstance(first_name, str) and (isinstance(last_name, str)):
        print(f"My name is {first_name} {last_name}")
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
