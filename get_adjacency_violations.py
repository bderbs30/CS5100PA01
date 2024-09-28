import numpy as np


def get_adjacency_violations(grid):  # written by AI
    # Assuming grid is a 2D NumPy array
    violations = 0

    # Shift grid to the right (align with left neighbor)
    right_shifted = np.roll(grid, -1, axis=1)
    right_shifted[:, -1] = -1  # Set last column to -1 to avoid wrapping
    right_conflicts = (grid == right_shifted) & (grid != -1)
    violations += np.sum(right_conflicts)

    # Shift grid down (align with upper neighbor)
    down_shifted = np.roll(grid, -1, axis=0)
    down_shifted[-1, :] = -1  # Set last row to -1 to avoid wrapping
    down_conflicts = (grid == down_shifted) & (grid != -1)
    violations += np.sum(down_conflicts)

    return violations
