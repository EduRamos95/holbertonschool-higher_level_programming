#!/usr/bin/python3
"""
Module Square
T1 : Class Square inherits from Rectangle
T1 : Class constructor: def __init__(self, size, x=0, y=0, id=None)
T1 : Modify method __str__ return '[Square] (<id>) <x>/<y> - <size>'
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square; inherits from class Rectangle
    Inherited Attributes:
        id __width __height __x __y
    Inherted Methods:
        Base.init(self, id=None)
        validate_parameter_int(self, value, param)
        Rectangle.init(self, width, height, x=0, y=0, id=None)
        @property: width. height, x, y
        @setter: width, height, x, y
        area(self)
        display(self)
        __str__(self)
        update(self, *args, **kwargs)
    Methods:
        __init__(self, size, x=0, y=0, id=None)
        __str__
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        str_square = "[Square] "
        str_id = "({:d}) ".format(self.id)
        str_xy = "{}/{} ".format(self.x, self.y)
        str_sep = "- "
        str_size = "{:d}".format(self.width)
        return (str_square + str_id + str_xy + str_sep + str_size)
