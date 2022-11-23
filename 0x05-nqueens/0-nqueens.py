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

all_solutions = []
starting_point = 0
columns_used = set()
positive_diags_used = set()
negative_diags_used = set()

positions = []

def find_solution():
    global starting_point
    global columns_used
    global positive_diags_used
    global negative_diags_used
    global positions
    global all_solutions

    for row in range(int(argument)):
        start = 0
        if row == 0:
            start = starting_point

        for column in range(int(argument))[start:]:
            if column not in columns_used and (row + column) not in positive_diags_used and (row - column) not in negative_diags_used:
                positions.append([row, column])
                columns_used.add(column)
                positive_diags_used.add(row + column)
                negative_diags_used.add(row - column)
                break
            else:
                continue

    if len(positions) == int(argument):
        all_solutions.append(positions)

    positions = []
    columns_used = set()
    positive_diags_used = set()
    negative_diags_used = set()
    starting_point += 1

while starting_point < int(argument):
    find_solution()

for ans in all_solutions:
    print(ans)
    