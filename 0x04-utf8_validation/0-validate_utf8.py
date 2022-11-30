#!/usr/bin/python3
"""
Write a method that determines if a given data set represents 
a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
     a method that determines if if a given data set represents a valid UTF-8 encoding.
    :param data:
    :returns: True or False
    """
    n_bytes = 0

    for num in data:
        binary = format(num, "#010b")[-8:]
        if n_bytes == 0:
            for bit in binary:
                if bit == '0':
                    break
                n_bytes += 1
            if n_bytes == 0:
                continue
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            if binary[0] != '1' or binary[1] != '0':
                return False

        n_bytes -= 1
    return n_bytes == 0