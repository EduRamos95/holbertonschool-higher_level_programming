#!/usr/bin/python3
"""
Module rectangle
T2 : Class Rectangle inherits from Base
T2 : Private instance attributes,
     each with its own public getter and setter
     (__width,__height,__x,__y)
T2 : Class constructor __init__
T3 : adding validation of all setter methods and instantiation
"""
from models.base import Base


class Rectangle(Base):
    """
    class Rectangle, inherits from class Base
    Inherited Attributes:
        id
    Class Attributes:
        __width __height __x __y
    Methods:
        validate_parameter_int(self, value, param)
        __init__(self, width, height, x=0, y=0, id=None)
        @property: width. height, x, y
        @setter: width, height, x, y
    """

    def validate_parameter_int(self, value, param):
        """
        Validate parameter
        """

        if type(value) is not int:
            raise TypeError(param + ' must be an integer')
        if value <= 0 and param in ('width', 'height'):
            raise ValueError(param + ' must be > 0')
        if value < 0 and param in ('x', 'y'):
            raise ValueError(param + ' must be >= 0')

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
        self.validate_parameter_int(value, 'width')
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        self.validate_parameter_int(value, 'height')
        self.__height = value

    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, value):
        self.validate_parameter_int(value, 'x')
        self.__x = value

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, value):
        self.validate_parameter_int(value, 'y')
        self.__y = value
