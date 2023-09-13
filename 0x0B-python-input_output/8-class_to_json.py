#!/usr/bin/python3
"""This define Python class-to-JSON function"""


def class_to_json(obj):
    """This return dictionary represntation of a simple data structure"""
    return obj.__dict__
