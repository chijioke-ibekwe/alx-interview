#!/usr/bin/python3
"""
File containing minOperations function
"""


def is_prime(n):
    return all(n%i for i in range(2, int(n**0.5)+1))

def hcf(n):
    if is_prime(n):
        return n

    if n%2 == 0:
        return n/2

    num = 0
    for i in range(3, int(n/2) + 2):
        if n%i == 0:
            num = i
    
    return num

def minOperations(n):
    if n <= 1 or n%1 != 0:
        return 0

    if is_prime(n):
        return n

    num = hcf(n)
    while(num == n/2 and (is_prime(num) is False)):
        num = hcf(num)
    
    return int(num + n/num)
