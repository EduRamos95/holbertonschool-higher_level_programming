#!/usr/bin/python3
"""
Module Square
T10 : Class Square inherits from Rectangle
T10 : Class constructor: def __init__(self, size, x=0, y=0, id=None)
T10 : Modify method __str__ return '[Square] (<id>) <x>/<y> - <size>'
T11 : adding public getter and setter 'size'
T12 : adding the public method 'def update(self, *args, **kwargs)'
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
        @property: size
        @setter: size
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

    @property
    def size(self):
        return (self.width)

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        update attributes in object
        """
        argc = len(args)
        kwargc = len(kwargs)
        list_attr = ['id', 'size', 'x', 'y']
        if argc > 4:
            argc = 4
        if args is not None and len(args) is not 0:
            for i in range(argc):
                if list_attr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)
