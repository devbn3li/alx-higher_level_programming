#!/usr/bin/python3
"""Represent a class Square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Init a new square
        Args:
            size (int): The size of the new square
        """
        self.size = size

    @property
    def size(self):
        """Get/set current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square"""
        return (self.__size ** 2)

    def __eq__(self, other):
        """Represent the == comparision to a Square"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Represent the != comparison to a Square"""
        return self.area() != other.area()

    def __lt__(self, other):
        """Represent the < comparison to a Square"""
        return self.area() < other.area()

    def __le__(self, other):
        """Represent the <= comparison to a Square"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Represent the > comparison to a Square"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Represent the >= compmarison to a Square"""
        return self.area() >= other.area()
