#!/usr/bin/python3
"""Contain defin of 'Rectangle' class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defin of `Rectangle` class"""
    def __init__(self, width, height):
        """Init a Rectangle instance"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
