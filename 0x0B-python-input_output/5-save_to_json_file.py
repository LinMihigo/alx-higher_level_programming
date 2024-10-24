#!/usr/bin/python3
"""Defining the save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using a JSON representation.

    Args:
        my_obj (any): The object to be serialized to JSON.
        filename (str): The name of the file to write to.
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)
