#!/usr/bin/python
"""Defining the rectangle Class"""
from models.base import Base


class Rectangle(Base):
    """"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        """"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        else:
            if value <= 0:
                raise ValueError("width must be > 0")
            else:
                self.__width = value

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        """"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        else:
            if value <= 0:
                raise ValueError("height must be > 0")
            else:
                self.__height = value


    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        """"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        else:
            if value < 0:
                raise ValueError("x must be >= 0")
            else:
                self.__x = value

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        """"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        else:
            if value < 0:
                raise ValueError("y must be >= 0")
            else:
                self.__y = value

    def area(self):
        return self.__width * self.__height
