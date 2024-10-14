#!/usr/bin/python3
""" Defining is_kind_of_class func"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class.
    
    Args:
    -----
    obj: Any
        The object to be checked.
    a_class: type
        The class to compare the type of the object against.

    Returns:
    --------
    bool
        True if the object is an instance of the specified class, or if the 
        object is an instance of a class that inherited from the specified
        class.
        False otherwise.
    """
    return isinstance(obj, a_class)
