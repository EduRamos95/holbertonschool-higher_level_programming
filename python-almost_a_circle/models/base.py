#!/usr/bin/python3
"""
Module Base
T1: Contains private class __nb_objects, and class constructor __init__

"""


class Base():
	"""
	Class Attributes:
	__nb_objects = 0
	Class constructor:
	def __init__(self, id=None):
	"""
	__nb_objects = 0

	def __init__(self, id=None):
		if id is not None:
			self.id = id
		else:
			Base.__nb_objects += 1
			self.id = Base.__nb_objects
