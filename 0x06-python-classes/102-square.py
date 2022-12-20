#!/usr/bin/python3
"""class Square"""


class Square:
    """class square"""
    def __init__(self, size=0):
        """square initialization"""
        self.size = size

    @property
    def size(self):
        """returns current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """area of square"""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """== comparison to another square"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define != comparison"""
        return self.area() != other.area()

    def __lt__(self, other):
        """define < comparison"""
        return self.area() < other.area()

    def __le__(self, other):
        """<= comparison"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """> comparison"""
        return self.area() > other.area()

    def __ge__(self, other):
        """>= comparison"""
        return self.area() >= other.area()
