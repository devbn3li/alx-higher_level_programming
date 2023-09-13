#!/usr/bin/python3
"""This define a Rectangle subclass Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This represent square"""

    def __init__(self, size):
        """This init new square
        Args:
            size (int): This size of the new square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
