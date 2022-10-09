#!/usr/bin/python3
"""
Module rectangle
T2 : Class Rectangle inherits from Base
T2 : Private instance attributes,
     each with its own public getter and setter
     (__width,__height,__x,__y)
T2 : Class constructor __init__
T3 : adding validation of all setter methods and instantiation
T4 : adding public method 'def area(self)'
T5 : adding public mehtod 'def display(self)'
T6 : modify method __str__ '[Rectangle] (<id>) <x>/<y> - <width>/<height>'
T7 : improving public mehod 'def display(self)'
T8 : adding public method 'def update(self, *args)'
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
        area(self)
        display(self)
        __str__(self)
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

    def area(self):
        """
        rectangle area
        """
        return (self.width * self.height)

    def display(self):
        """
        graphical representation
        """
        rectangle = ""
        rectangle += self.y * '\n'
        for i in range(self.height):
            rectangle += (" " * self.x)
            rectangle += ("#" * self.width) + '\n'
        print(rectangle, end='')

    def __str__(self):
        str_rectangle = "[Rectangle] "
        str_id = "({:d}) ".format(self.id)
        str_xy = "{:d}/{:d} ".format(self.x, self.y)
        str_sep = "- "
        str_wh = "{:d}/{:d}".format(self.width, self.height)
        return (str_rectangle + str_id + str_xy + str_sep + str_wh)

    def update(self, *args):
        """
        update attributes in object
        """
        list_attr = ['id', 'width', 'height', 'x', 'y']
        for i in range(len(args)):
            setattr(self, list_attr[i], args[i])
