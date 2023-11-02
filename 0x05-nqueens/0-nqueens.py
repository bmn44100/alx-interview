#!/usr/bin/python3
"""
module for N queens puzzle
"""

import sys


def moves(final, row, column):
    """
    Checks if a queen can be placed in a given position
    """
    rows = []
    columns = []
    left = []
    right = []

    for nums in final:
        rows.append(nums[0])
        columns.append(nums[1])
        left.append(nums[1] - nums[0])
        right.append(nums[0] + nums[1])

    if row in rows or column in columns:
        return False
    if column - row in left or row + column in right:
        return False

    return True


def nqueens(final, column, chess_board=[]):
    """
    The main recursive program
    """
    for item in range(n):
        if moves(final, item, column):
            final.append([item, column])
            if column == n - 1:
                chess_board.append(final.copy())
                del final[-1]
            else:
                nqueens(final, column + 1)

    if len(final) > 0:
        del final[-1]
    return chess_board

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except(TypeError):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    final = []
    final = nqueens(final, 0)

    for nums in final:
        print(nums)
