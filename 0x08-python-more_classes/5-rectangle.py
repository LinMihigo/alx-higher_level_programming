#!/usr/bin/python3
"""Defines the Rectangle class"""


class Rectangle:
    """Defines a rectangle

    Attributes:
        width (int): private instance width attribute
        height (int): private instance height attribute

    """
    def __init__(self, width=0, height=0):
        """private instance attributes init

        Args:
            width (int): width of rectangle
            height (int): height of rectangle

        """
        self.height = height
        self.width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """property setter for height

        Args:
            value (int): value to set to __height

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        else:
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """property setter for width

        Args:
            value (int): value to set to __width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        else:
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

    def area(self):  #: Calculates the square area
        return self.__height * self.__width

    def perimeter(self):  #: Calculates the rectangle perimeter
        return 2 * (self.__width + self.__height)

    def __str__(self):  #: Returns string object of the Class object
        if self.__height == 0 and self.__width == 0:
            print("")
            return
        rect = []
        for i in range(self.__height):
            for j in range(self.__width):
                rect.append("#")
            rect.append("\n" if i != self.__height - 1 else "")
        return ("".join(rect))

    def __repr__(self):  #: Canonical string repres. of the Class object.
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):  #: Print a message at instance deletion
        print("Bye rectangle...")
