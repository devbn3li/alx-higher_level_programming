#!/usr/bin/python3
"""Peak finding algorithm"""


def find_peak(list_of_integers):
    """Return the peak in a list of unsorted integers"""
    if list_of_integers == []:
        return None

    x = len(list_of_integers)
    if x == 1:
        return list_of_integers[0]
    elif x == 2:
        return max(list_of_integers)

    mid = int(x / 2)
    peak = list_of_integers[mid]
    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak
    elif peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
