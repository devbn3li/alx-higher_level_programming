#!/usr/bin/python3
"""Define subclass or child list class MyList"""


class MyList(list):
    """This class is a subclass of the built-in list class"""

    def print_sorted(self):
        """This print sorted list in an ascending order"""
        print(sorted(self))
