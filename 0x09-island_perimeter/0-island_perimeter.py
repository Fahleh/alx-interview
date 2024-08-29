#!/usr/bin/python3
"""Module for the Island Perimeter Problem
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.
    """
    if not grid or not grid[0]:
        return 0

    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:

                perimeter += 4

                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2

                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2

    return perimeter
