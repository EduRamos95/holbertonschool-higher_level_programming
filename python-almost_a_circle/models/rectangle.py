#!/usr/bin/python3
"""
Module rectangle
T2 : Class Rectangle inherits from Base
T2 : Private instance attributes,
     each with its own public getter and setter
     (__width,__height,__x,__y)
T2 : Class constructor __init__
"""


class Rectangle(Base):
    """
    class Rectangle, inherits from class Base
    Inherited Attributes:
        id
    Class Attributes:
        __width __height __x __y
    Methods:
        __init__(self, width, height, x=0, y=0, id=None)
        @property: width. height, x, y
        @setter: width, height, x, y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, value):
        self.__y = value
