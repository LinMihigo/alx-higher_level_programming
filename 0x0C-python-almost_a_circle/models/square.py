#!/usr/bin/python3
"""Defines the Square Class"""
from models.rectangle import Rectangle
import json


class Square(Rectangle):
    """Represents a square, inheriting from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialises a new Square

        Args:
            size (int): size of the new Square
            x (int): x-coordinate of the rectangle
            y (int): y-coordinate of the rectangle
            id (int): Id of the new Rectangle
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get square size"""
        return self.width

    @size.setter
    def size(self, value):
        """Set square size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the Square

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if len(args) > 0:
            self.id = args[0]
        elif 'id' in kwargs:
            self.id = kwargs['id']

        if len(args) > 1:
            self.width = args[1]
            self.height = args[1]
        elif 'size' in kwargs:
            self.width = kwargs['size']
            self.height = kwargs['size']

        if len(args) > 2:
            self.x = args[2]
        elif 'x' in kwargs:
            self.x = kwargs['x']

        if len(args) > 3:
            self.y = args[3]
        elif 'y' in kwargs:
            self.y = kwargs['y']

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        dict = json.dumps(
            {
                'id': self.id,
                'x': self.x,
                'size': self.size,
                'y': self.y
            })
        return json.loads(dict)

    def __str__(self):
        """Returns the human readable string repr. of the Square object"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
