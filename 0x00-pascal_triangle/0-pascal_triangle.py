#!/usr/bin/python3
"""
0-pascal_triangle
"""


def factorial(n):  
    answer = 1    
    if n < 0:
        return None    
    elif n == 0:
        return 1    
    else:
        for i in range(1, n + 1):
            answer = answer * i    
    return answer 


def pascal_triangle(n):
    """
    This function prints a pascals triangle of n rows
    """
    complete_array = []

    if n <= 0:
        return complete_array

    for row in range(0, n):
        row_array = []
        for element in range(0, row + 1):
            x = factorial(row)/(factorial(row - element) * factorial(element))
            row_array.append(int(x))

        complete_array.append(row_array)

    return complete_array
