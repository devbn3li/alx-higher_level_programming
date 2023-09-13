#!/usr/bin/python3
"""This define a string-to-JSON function"""
import json


def to_json_string(my_obj):
    """This return JSON representation of a string object"""
    return json.dumps(my_obj)
