#!/usr/bin/python3
"""Defining the Base Class"""
import json
import os


class Base:
    """
    The Base class is the foundation for all other classes in this project.

    Private Class Attributes:
        __nb_objects (int): Number of instantiated bases.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialise a new Base

        Args:
            id : int
                Unique identifier for each instance. Auto-incremented if not
                provided.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
         Converts a list of dictionaries to its JSON string representation.

         Args:
            list_dictionaries (list): A list of dictionaries
        """
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes a JSON string repr. of a list of dicts to a file.

        Args:
            list_objs (list): A list of inherited instances
        """
        with open(f"{cls.__name__}.json", "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                dicts_list = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(dicts_list))

    @staticmethod
    def from_json_string(json_string):
        """Converts a JSON string repr. to a list of dicts
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates a new instance of the class using a dict of attributes
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Reads from a JSON file and returns a list of class instances
        """
        filename = str(cls.__name__) + ".json"
        if os.path.exists(filename) is False:
            return []
        with open(filename, "r") as file:
            str_list = file.read()
            dicts_list = cls.from_json_string(str_list)
            return [cls.create(**dicts) for dicts in dicts_list]
