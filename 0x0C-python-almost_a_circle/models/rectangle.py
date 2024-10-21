#!/usr/bin/python
"""Defining the rectangle Class"""
from models.base import Base
import json


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

	def display(self):
		for k in range(self.__y):
			print("")
		for i in range(self.__height):
			for l in range(self.__x):
				print(" ", end="")
			for j in range(self.__width):
				print("#", end="")
			print("")

	def __str__(self):
		return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height})"
	
	def update(self, *args, **kwargs):
		if len(args) > 0:
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
		dict = json.dumps(
			{
				'x': self.x,
				'y': self.y,
				'id': self.id,
				'height': self.height,
				'width': self.width
			})
		return json.loads(dict)
