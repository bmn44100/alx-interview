#!/usr/bin/python3

"""
module for a function that rotates a 2D matrix 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """ rotates a 2D matrix 90 degrees clockwise. """
    n = [row[:] for row in matrix]
    n.reverse()

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[j][i] = n[i][j]
