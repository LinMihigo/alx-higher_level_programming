#!/usr/bin/python3
"""Defines the Rectangle class"""


class Rectangle:
    """Defines a rectangle

    Attributes:
        width (int): private instance width attribute
        height (int): private instance height attribute
        number_of_instances (int): num of instances
        print_symbol (any): The symbol used for string representation.

    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """private instance attributes init

        Args:
            width (int): width of rectangle
            height (int): height of rectangle

        """
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the greater area.

        Args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle with width and height equal to size.

        Args:
            size (int): The width and height of the new Rectangle.
        """
        return (cls(size, size))

    def __str__(self):  #: Returns string object of the Class object
        if self.__height == 0 and self.__width == 0:
            print("")
            return
        rect = []
        for i in range(self.__height):
            for j in range(self.__width):
                rect.append(str(self.print_symbol))
            rect.append("\n" if i != self.__height - 1 else "")
        return ("".join(rect))

    def __repr__(self):  #: Canonical string repres. of the Class object.
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):  #: Print a message at instance deletion
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
