#!/usr/bin/python3
"""Defines the Student class"""


class Student:
    """Defines a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes the Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        Args:
            attrs (list, optional): A list of attribute names to retrieve.
            If None, all attributes are retrieved.

        Returns:
            dict: The dictionary representation of the student.
        """
        if attrs is None:
            return self.__dict__

        return {attr: self.__dict__[attr]
                for attr in attrs
                if attr in self.__dict__}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with values from a
        dictionary.

        Args:
            json (dict): A dictionary containing attribute names and values.
        """
        for key, value in json.items():
            setattr(self, key, value)
