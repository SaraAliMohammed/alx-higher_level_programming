#!/usr/bin/python3
"""This is a Square Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        This is a Square class.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of a square"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}")

    @property
    def size(self):
        '''Square Size.'''
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def updateByArgs(self, id=None, size=None, x=None, y=None):
        """Update attributes from args"""
        if id:
            self.id = id
        if size:
            self.size = size
        if x:
            self.x = x
        if y:
            self.y = y

    def update(self, *args, **kwargs):
        """Assigns a key/value argument to each attribute"""
        if (args):
            self.updateByArgs(*args)
        elif (kwargs):
            self.updateByArgs(**kwargs)

    def to_dictionary(self):
        """The dictionary representation of a Square"""
        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}
