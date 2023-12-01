#!/usr/bin/python3
"""Peak finding algorithm"""


def find_peak(list_of_integers):
    """a function that finds a peak in a list of unsorted integers."""
    if list_of_integers is None or list_of_integers == []:
        return None
    if len(list_of_integers) == 0:
        return None

    if len(list_of_integers) == 1:
        return list_of_integers[0]

    mid = len(list_of_integers) // 2
    if list_of_integers[mid] >= list_of_integers[mid - 1] and\
       list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]

    if list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])

    else:
        return find_peak(list_of_integers[mid+1:])
