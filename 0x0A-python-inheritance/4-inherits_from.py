#!/usr/bin/python3
"""Define a inherits_from func"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherited (directly or
    indirectly) from the specified class, but not if the object is an instance
    of the specified class itself.

    Args:
    -----
    obj: Any
        The object to be checked.
    a_class: type
        The class to compare the object's inheritance against.

    Returns:
    --------
    bool
        True if the object is an instance of a class that inherited from the
        specified class, and False if the object is either an instance of the
        specified class or does not inheritfrom it.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
