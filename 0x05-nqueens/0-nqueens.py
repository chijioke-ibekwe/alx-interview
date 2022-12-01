#!/usr/bin/python3
"""
A program that solves the N queens problem. The N queens puzzle is the challenge of placing N 
non-attacking queens on an NxN chessboard.
"""
import sys

if len(sys.argv) > 2:
    print("Usage: nqueens N")
    sys.exit(1)

argument = sys.argv[1]

if float(argument) % 1 != 0:
    print("N must be a number")
    sys.exit(1)

if float(argument) < 4:
    print("N must be at least 4")
    sys.exit(1)

def solve_nqueens(n):
    '''self descriptive'''
    if n == 0:
        return [[]]
    inner_solution = solve_nqueens(n - 1)
    return [solution + [(n, i + 1)]
            for i in range(argument)
            for solution in inner_solution
            if safe_queen((n, i + 1), solution)]


def attack_queen(square, queen):
    '''self descriptive'''
    (row1, col1) = square
    (row2, col2) = queen
    return (row1 == row2) or (col1 == col2) or\
        abs(row1 - row2) == abs(col1 - col2)


def safe_queen(sqr, queens):
    '''self descriptive'''
    for queen in queens:
        if attack_queen(sqr, queen):
            return False
    return True


for answer in reversed(solve_nqueens(argument)):
    result = []
    for p in [list(p) for p in answer]:
        result.append([i - 1 for i in p])
    print(result)  