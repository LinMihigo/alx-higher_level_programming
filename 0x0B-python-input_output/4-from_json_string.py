#!/usr/bin/python3
"""Defines a string-to-JSON function."""
import json


def from_json_string(my_str):
    """Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): The JSON string to deserialize.

    Returns:
        any: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
