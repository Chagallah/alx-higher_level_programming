#!/usr/bin/python3
""" base module """


class Base():
    """ Base class """
    __nb_objects = 0
    id = 0

    def __init__(self, id=None):
        """
        Constructor


        :param id:id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def strict_integer(self, name, value):
        """
        strict integer
        :param name: name of variable
        :param value: value of variable
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    @staticmethod
    def integer_validation(name, value):
        """
        integer validation
        Args:
            name: name of the variable
            value: value of the variable
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer">format(name))

        if value < 0:
            raise ValueError("{} must be >= 0".format(name))
