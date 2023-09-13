#!/usr/bin/python3
"""Contain definition of 'MyInt' class."""


class MyInt(int):
    """Definition of `MyInt` class"""
    def __eq__(self, value):
        """Inverts == operators"""
        return int.__ne__(self, value)

    def __ne__(self, value):
        """Inverts != operators"""
        return int.__eq__(self, value)
