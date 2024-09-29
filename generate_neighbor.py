from gridgame import *
import numpy as np


# --------------------------------------------------- generate_neighbor function ------------------
def generate_neighbor(
    shapePos, currentShapeIndex, currentColorIndex, grid, exponent, fill_threshold
):  # partially written by AI - mainly the weighting parts

    if grid is None:
        raise ValueError("The grid should not be None")
    neighbor_grid = np.copy(grid)

    # ---------------------------------------------------
    # Set up shape selection probabilities
    # ---------------------------------------------------
    num_shapes = len(shapes)

    # ---------------------------------------------------
    # Compute shape areas
    # ---------------------------------------------------
    shape_areas = []
    for dims in shapesDims:
        shape_width, shape_height = dims  # Ensure correct order
        area = shape_width * shape_height
        shape_areas.append(area)

    # ---------------------------------------------------
    # Assign probabilities based on areas
    # ---------------------------------------------------
    probabilities = [(area**exponent) for area in shape_areas]
    total_prob = sum(probabilities)
    probabilities = [prob / total_prob for prob in probabilities]

    # ---------------------------------------------------
    # Select a new shape index using weighted random selection
    # ---------------------------------------------------
    fill_level = get_fill_level(neighbor_grid)

    # If the grid is almost full, select the shape with the smallest area
    if fill_level >= fill_threshold:
        currentShapeIndex = np.argmin(shape_areas)
    else:
        currentShapeIndex = np.random.choice(range(num_shapes), p=probabilities)

    # ---------------------------------------------------
    # Get valid moves and their weights
    # ---------------------------------------------------
    valid_moves = get_valid_moves(
        shapePos, len(neighbor_grid), currentShapeIndex, neighbor_grid
    )

    # Extract moves and movement weights
    moves, movement_weights = zip(*valid_moves)

    # Normalize movement_weights to create a probability distribution
    total_weight = sum(movement_weights)
    if total_weight == 0:
        # Assign equal probability to all moves
        probabilities = [1 / len(movement_weights)] * len(movement_weights)
    else:
        probabilities = [weight / total_weight for weight in movement_weights]

    # ---------------------------------------------------
    # Select a move based on the weighted probabilities
    # ---------------------------------------------------
    pos_move = np.random.choice(moves, p=probabilities)

    # ---------------------------------------------------
    # Update the shape position based on the move
    # ---------------------------------------------------
    new_shapePos = update_shapePos(
        shapePos, pos_move, len(neighbor_grid), len(neighbor_grid)
    )

    # ---------------------------------------------------
    # Get an available color at the new position
    # ---------------------------------------------------
    new_color_index = getAvailableColor(neighbor_grid, new_shapePos[0], new_shapePos[1])

    # ---------------------------------------------------
    # Update the grid if the shape can be placed
    # ---------------------------------------------------
    if canPlace(neighbor_grid, shapes[currentShapeIndex], new_shapePos):
        placeShape(
            neighbor_grid, shapes[currentShapeIndex], new_shapePos, new_color_index
        )

    # ---------------------------------------------------
    # Construct the neighbor dictionary to return
    # ---------------------------------------------------
    neighbor = {
        "gridState": neighbor_grid,
        "posMove": pos_move,
        "neighborColorIndex": new_color_index,
        "neighborShapeIndex": currentShapeIndex,
    }

    return neighbor


# --------------------------------------------------- get_valid_moves function ------------------
def get_valid_moves(
    shapePos, grid_size, current_shape_index, grid, lookahead=5
):  # written by AI
    valid_moves = []
    x, y = shapePos
    shape_dims = shapesDims[current_shape_index]
    shape_width, shape_height = shape_dims

    # ---------------------------------------------------
    # Define function to calculate weight for a direction
    # ---------------------------------------------------
    def calculate_weight(x, y, dx, dy, grid, grid_size):
        for step in range(1, grid_size):
            look_x = x + dx * step
            look_y = y + dy * step
            if 0 <= look_x < grid_size and 0 <= look_y < grid_size:
                if grid[look_y, look_x] == -1:
                    # Return inverse of distance as weight
                    return 1 / step
            else:
                break  # Out of bounds
        return 0  # No uncolored cell found in this direction

    # Check if moving up is possible
    if y > 0:
        weight = calculate_weight(x, y, 0, -1, grid, grid_size)
        valid_moves.append(("up", weight))
    # Check if moving down is possible (considering shape height)
    if y + shape_height < grid_size:
        weight = calculate_weight(x, y, 0, 1, grid, grid_size)
        valid_moves.append(("down", weight))
    # Check if moving left is possible
    if x > 0:
        weight = calculate_weight(x, y, -1, 0, grid, grid_size)
        valid_moves.append(("left", weight))
    # Check if moving right is possible (considering shape width)
    if x + shape_width < grid_size:
        weight = calculate_weight(x, y, 1, 0, grid, grid_size)
        valid_moves.append(("right", weight))

    return valid_moves


# --------------------------------------------------- update_shapePos function ------------------
def update_shapePos(shapePos, move, grid_width, grid_height):
    x, y = shapePos

    # ---------------------------------------------------
    # Update position based on move
    # ---------------------------------------------------
    if move == "up":
        if y > 0:
            y -= 1  # Moving up decreases the y-coordinate
    elif move == "down":
        if y < grid_height - 1:
            y += 1  # Moving down increases the y-coordinate
    elif move == "left":
        if x > 0:
            x -= 1  # Moving left decreases the x-coordinate
    elif move == "right":
        if x < grid_width - 1:
            x += 1  # Moving right increases the x-coordinate
    else:
        print(f"Invalid move command: {move}")

    return [x, y]


def get_fill_level(grid):

    total_cells = grid.size
    filled_cells = np.count_nonzero(grid != -1)
    fill_level = filled_cells / total_cells
    return fill_level
