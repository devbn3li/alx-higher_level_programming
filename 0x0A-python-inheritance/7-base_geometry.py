#!/usr/bin/python3
"""Contain defin of 'BaseGeometry' class"""


class BaseGeometry:
    """Definition of `BaseGeometry` class"""
    def area(self):
        """Definition of `area` function."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates an int value"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
