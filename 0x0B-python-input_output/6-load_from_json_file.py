#!/usr/bin/python3
"""Defining the load_from_json_file function"""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        any: The object created from the JSON file.
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        return json.load(file)
