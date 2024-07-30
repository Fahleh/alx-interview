#!/usr/bin/python3
"""Solving N queens"""

import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    num_of_queens = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    exit(1)

if num_of_queens < 4:
    print("N must be at least 4")
    exit(1)


def nqueens_resolve(num):
    """Solve the nqueens problem"""
    if num == 0:
        return [[]]
    nested = nqueens_resolve(num - 1)
    return [solution + [(num, i + 1)]
            for i in range(num_of_queens)
            for solution in nested
            if nqueen_safe((num, i + 1), solution)]


def nqueen_attack(position, queen):
    """Performs attack on queen"""
    (row1, col1) = position
    (row2, col2) = queen
    return (row1 == row2) or (col1 == col2) or\
        abs(row1 - row2) == abs(col1 - col2)


def nqueen_safe(position, queens):
    """Checks the saftey of the queen"""
    for queen in queens:
        if nqueen_attack(position, queen):
            return False
    return True


for solution in reversed(nqueens_resolve(num_of_queens)):
    result = []
    for e in [list(e) for e in solution]:
        result.append([i - 1 for i in e])
    print(result)
