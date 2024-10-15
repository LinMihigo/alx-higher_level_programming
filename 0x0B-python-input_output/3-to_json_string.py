#!/usr/bin/python3
"""Defines the to_json_string function."""
import json


def to_json_string(my_obj):
    """
    Gives the JSON representation of an object (string).

    Args:
        my_obj (any): The object to be serialized into JSON format.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
