from gridgame import *
import numpy as np


def generate_neighbor(shapePos, currentShapeIndex, currentColorIndex, grid):

    


   

    


def get_valid_moves(shapePos, grid_size, current_shape_index):
    valid_moves = []
    x, y = shapePos
    shape_dims = shapesDims[current_shape_index]
    # Dimensions of the current shape (width, height)
    shape_width, shape_height = shape_dims

    # Check if moving up is possible
    if y > 0:
        valid_moves.append("up")
    # Check if moving down is possible (considering shape height)
    if y + shape_height < grid_size:
        valid_moves.append("down")
    # Check if moving left is possible
    if x > 0:
        valid_moves.append("left")
    # Check if moving right is possible (considering shape width)
    if x + shape_width < grid_size:
        valid_moves.append("right")
    return valid_moves
