#!/usr/bin/python3
"""Define base class for geometry"""


class BaseGeometry:
    """Represent base geometry"""

    def area(self):
        """Raise an exception indicating area() is not implemented"""
        raise Exception("area() is not implemented")
