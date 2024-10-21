#!/usr/bin/python3
from models.rectangle import Rectangle
import json


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
    
    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
    
    @property
    def size(self):
        return self.width
    
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
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
        dict = json.dumps(
            {
                'id': self.id,
                'x': self.x,
                'size': self.size,
                'y': self.y
            })
        return json.loads(dict)
