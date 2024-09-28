import time
import numpy as np
import math
from gridgame import *
from get_adjacency_violations import *
from generate_neighbor import *
from calculate_cost import *


##############################################################################################################################

# You can visualize what your code is doing by setting the GUI argument in the following line to true.
# The render_delay_sec argument allows you to slow down the animation, to be able to see each step more clearly.

# For your final submission, please set the GUI option to False.

# The gs argument controls the grid size. You should experiment with various sizes to ensure your code generalizes.

##############################################################################################################################

setup(GUI=False, render_delay_sec=0.01, gs=10)


##############################################################################################################################

# Initialization

# shapePos is the current position of the brush.

# currentShapeIndex is the index of the current brush type being placed (order specified in gridgame.py, and assignment instructions).

# currentColorIndex is the index of the current color being placed (order specified in gridgame.py, and assignment instructions).

# grid represents the current state of the board.

# -1 indicates an empty cell
# 0 indicates a cell colored in the first color (indigo by default)
# 1 indicates a cell colored in the second color (taupe by default)
# 2 indicates a cell colored in the third color (veridian by default)
# 3 indicates a cell colored in the fourth color (peach by default)

# placedShapes is a list of shapes that have currently been placed on the board.

# Each shape is represented as a list containing three elements: a) the brush type (number between 0-8),
# b) the location of the shape (coordinates of top-left cell of the shape) and c) color of the shape (number between 0-3)

# For instance [0, (0,0), 2] represents a shape spanning a single cell in the color 2=veridian, placed at the top left cell in the grid.

# done is a Boolean that represents whether coloring constraints are satisfied. Updated by the gridgames.py file.

##############################################################################################################################

shapePos, currentShapeIndex, currentColorIndex, grid, placedShapes, done = execute(
    "export"
)

# input()   # <-- workaround to prevent PyGame window from closing after execute() is called, for when GUI set to True. Uncomment to enable.
print(shapePos, currentShapeIndex, currentColorIndex, grid, placedShapes, done)


####################################################
# Timing your code's execution for the leaderboard.8
####################################################

start = time.time()  # <- do not modify this.


##########################################
# Write all your code in the area below.
##########################################

# implement simulated annealing algorithm

# T = 1000
# d = 0.82

# while not done:

#     neighbor = generate_neighbor(shapePos, currentShapeIndex, currentColorIndex, grid)

#     if neighbor == None:
#         continue

#     # if the neighbor is better than the current state
#     if energy(neighbor["gridState"]) <= energy(grid):
#         execute(neighbor["move"])

#         if random(0, 1) <= math.exp((energy(grid) - energy(neighbor["gridState"])) / T):
#             execute(neighbor["move"])
#         else:
#             continue
#     T = T * d

grid_size = len(grid)

for y in range(grid_size):
    if y % 2 == 0:
        # Even row: move right
        for x in range(grid_size - 1):
            execute("switchcolor")  # Change color
            execute("place")  # Place shape
            execute("right")
            shapePos, _, _, _, _, _ = execute("export")
    else:
        # Odd row: move left
        for x in range(grid_size - 1):
            execute("switchcolor")  # Change color
            execute("place")  # Place shape
            execute("left")
            shapePos, _, _, _, _, _ = execute("export")
    # At the end of each row, move down if not at the last row
    if y < grid_size - 1:
        execute("switchcolor")  # Change color
        execute("place")  # Place shape
        execute("down")
        shapePos, _, _, _, _, _ = execute("export")


########################################

# Do not modify any of the code below.

########################################

end = time.time()

np.savetxt("grid.txt", grid, fmt="%d")
with open("shapes.txt", "w") as outfile:
    outfile.write(str(placedShapes))
with open("time.txt", "w") as outfile:
    outfile.write(str(end - start))
