#!/usr/bin/python3
"""Defining the Base Class"""
import json


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

    def from_json_string(json_string):
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)
