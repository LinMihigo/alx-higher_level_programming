#!/usr/bin/python3
"""Defines class_to_json function."""


def class_to_json(obj):
    """Returns the dictionary description for JSON serialization of an object.

    Args:
        obj (object): An instance of a class.

    Returns:
        dict: The dictionary description of the object.
    """
    return obj.__dict__
