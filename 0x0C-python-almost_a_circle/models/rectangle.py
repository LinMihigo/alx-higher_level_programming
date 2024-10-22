#!/usr/bin/python3
"""Defining the rectangle Class"""
from models.base import Base
import json


class Rectangle(Base):
    """Represents a Rectangle that inherits from Class Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialises the Rectangle class

        Args:
            width (int): Rectangle width
            height (int): Rectangle height
            x (int): x-coordinate of the rectangle
            y (int): y-coordinate of the rectangle
            id (int): Id of the new Rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        else:
            if value <= 0:
                raise ValueError("width must be > 0")
            else:
                self.__width = value

    @property
    def height(self):
        """Get the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the width of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        else:
            if value <= 0:
                raise ValueError("height must be > 0")
            else:
                self.__height = value

    @property
    def x(self):
        """Get the x coord. of the Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x coord. of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        else:
            if value < 0:
                raise ValueError("x must be >= 0")
            else:
                self.__x = value

    @property
    def y(self):
        """Set the y coord. of the Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y coord. of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        else:
            if value < 0:
                raise ValueError("y must be >= 0")
            else:
                self.__y = value

    def area(self):
        """Returns the area of a Rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints a visual repr. of the Rectangle using the "#" char."""
        for _ in range(self.__y):
            print("")
        for _ in range(self.__height):
            for _ in range(self.__x):
                print(" ", end="")
            for _ in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """Returns the human readable string repr. of the Rectangle object"""
        return (
            f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
            f"{self.__width}/{self.__height}"
        )

    def update(self, *args, **kwargs):
        """Updates the Rectangle

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if len(args) > 1:
            self.id = args[0]
        elif 'id' in kwargs:
            self.id = kwargs['id']

        if len(args) > 1:
            self.__width = args[1]
        elif 'width' in kwargs:
            self.__width = kwargs['width']

        if len(args) > 2:
            self.__height = args[2]
        elif 'height' in kwargs:
            self.__height = kwargs['height']

        if len(args) > 3:
            self.__x = args[3]
        elif 'x' in kwargs:
            self.__x = kwargs['x']

        if len(args) > 4:
            self.__y = args[4]
        elif 'y' in kwargs:
            self.__y = kwargs['y']

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        dict = json.dumps(
            {
                'x': self.x,
                'y': self.y,
                'id': self.id,
                'height': self.height,
                'width': self.width
            })
        return json.loads(dict)
