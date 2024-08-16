#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix, rotate it 90 degrees clockwise
    """
    for i, j in enumerate(zip(*reversed(matrix))):
        matrix[i] = list(j)
