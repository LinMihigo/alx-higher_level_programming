#!/usr/bin/python3
"""Defining is_same_class func"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of a specified class.
    
    Args:
    -----
    obj: Any
        The object to be checked.
    a_class: type
        The class to compare the type of the object against.

    Returns:
    --------
    bool
        True if the object is exactly an instance of the specified class
        False otherwise.
    """
    return type(obj) is a_class
