import numpy as np
from get_adjacency_violations import *


def energy(grid):

    energy = 0
    violations = get_adjacency_violations(grid)
    colored_cells = count_colored_cells(grid)

    if violations > 0:
        energy = float("inf")

    energy = energy - colored_cells
    return energy


def count_colored_cells(grid):
    return np.count_nonzero(grid != -1)
