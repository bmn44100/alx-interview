#!/usr/bin/python3

"""
module for island_perimeter
"""


def island_perimeter(grid):
    """
    returns the perimeter of the island described in grid
    """
    perimeter = 0

    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            grid_cell = grid[row][col]
            if grid_cell is 1:
                perimeter += 4
                if row != 0 and grid[row - 1][col] is 1:
                    perimeter -= 1
                if col != 0 and grid[row][col - 1] is 1:
                    perimeter -= 1
                if row + 1 != rows and grid[row + 1][col] is 1:
                    perimeter -= 1
                if col + 1 != cols and grid[row][col + 1] is 1:
                    perimeter -= 1
    
    return perimeter