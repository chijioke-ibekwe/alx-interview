#!/usr/bin/python3
"""
0-pascal_triangle
"""


import math


def pascal_triangle(n):
    complete_array = []

    if n <= 0:
        return complete_array

    for row in range(0, n):
        row_array = []
        for element in range(0, row + 1):
            x = math.factorial(row)/(math.factorial(row - element) * math.factorial(element))
            row_array.append(int(x))

        complete_array.append(row_array)

    return complete_array
