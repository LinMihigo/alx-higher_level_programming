#!/usr/bin/python3
"""Defining the Base Class"""
import json
import os


class Base:
    """

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        with open(f"{cls.__name__}.json", "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                dicts_list = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(dicts_list))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = str(cls.__name__) + ".json"
        if os.path.exists(filename) is False:
            return []
        with open(filename, "r") as file:
            str_list = file.read()
            dicts_list = cls.from_json_string(str_list)
            return [cls.create(**dicts) for dicts in dicts_list]
