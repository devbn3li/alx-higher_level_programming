#!/usr/bin/python3
"""Represent a class Square"""


class Square:
    """Represent a square"""

    def __init__(self, size):
        """Init a new square
        Args:
            size (int): size of new square
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
        """Return current area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """Print the square with the # char"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
