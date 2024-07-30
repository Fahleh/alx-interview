#!/usr/bin/python3
"""Solving N Queens Problem using backtracking"""
import sys


def show_result(board, n):
    """Prints the result of the algorithm"""
    result = []

    for r in range(n):
        for c in range(n):
            if c == board[r]:
                result.append([r, c])
    print(result)


def queen_safe(board, r, c, row):
    """
    Checks if the queen is safe in the current position
    """
    return board[r] in (c, c - r + row, r - row + c)


def find_positions(board, row, n):
    """
    Finds spaces where the queen can be allocated
    """
    if row == n:
        show_result(board, n)

    else:
        for c in range(n):
            is_free = True
            for r in range(row):
                if queen_safe(board, r, c, row):
                    is_free = False
            if is_free:
                board[row] = c
                find_positions(board, row + 1, n)


def initialize_board(size):
    """Initializes a new board"""
    return [0 * size for i in range(size)]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    N = int(sys.argv[1])
    board = initialize_board(N)
    solutions = find_positions(board, 0, N)
