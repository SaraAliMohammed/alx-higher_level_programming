#!/usr/bin/python3
"""This is a Rectangle Module"""
from models.base import Base


class Rectangle(Base):
    """
        This is a Rectangle class.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        self.setter_validation("width", value)
        self.__width = value

    @property
    def height(self):
        """Rectangle Height"""
        return self.__height

    @height.setter
    def height(self, value):
        self.setter_validation("height", value)
        self.__height = value

    @property
    def x(self):
        """Rectangle x position"""
        return self.__x

    @x.setter
    def x(self, value):
        self.setter_validation("x", value)
        self.__x = value

    @property
    def y(self):
        """Rectangle y position"""
        return self.__y

    @y.setter
    def y(self, value):
        self.setter_validation("y", value)
        self.__y = value

    def setter_validation(self, attribute, value):
        """Validation method of all setter methods and instantiation"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(attribute))
        if attribute == "height" or attribute == "width":
            if value <= 0:
                raise ValueError("{} must be > 0".format(attribute))
        if attribute == "x" or attribute == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(attribute))
