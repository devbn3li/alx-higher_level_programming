#!/usr/bin/python3
"""This define Pascal's Triangle function"""


def pascal_triangle(n):
    """This represents Pascal's Triangle of size n
    Returns a list of lists of integers representing the triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        tri = triangle[-1]
        temp = [1]
        for i in range(len(tri) - 1):
            temp.append(tri[i] + tri[i + 1])
        temp.append(1)
        triangle.append(temp)
    return triangle
