Our goal is to color the grid so that no adjacent tiles have the same color.

We want to minimize the number of shapes that we use

We start with an initial state and then consider some various neighbor states

Neighbor states are generated via switching the three variables.

1. The shape index
2. The color
3. The position of the brush

We want to be changing the position of the brush for every generation of neighbor state

We'll also likely want to change the color since if we move the brush one tile then there still might be conflicts

State generation considerations

we want to be moving for each neighbor state
tho for the movement we want to suggest moves that make sense based on the current shape selection and brush position

So the generate neighbor needs to be fixed cause its scuffed

So for the generate neighbor we can do three things: change the shape, color or position of the brush

We most likely want to change the position of the brush for each neighbor state

- However there was a problem where if we wanted to move the brush and place as well we got stuck in an area (this was because we evaluated the grid for conflicts or if the piece could be done. but if the current position is surrounded by colored cells then it can't just move to any position and try to place because thats not possilbe (I said that if its not possible to place then we would return None and none would be evaluateed as a skip in the loop/iteration this led to an infinite loop where the pos got stuck))

- So we do want neighbor states that just propose moving the brush and not placing a piece. We will have a list of moves for a neighbor state. It could just be a pos move or it could be a combination of pos and place moves or change color moves. If we accept this neighbor then we'll iterate through the move list and execute them.

getAvailableColor

- can be used for the color picking

# Utility function to get a random color that is not adjacent to the current position

def getAvailableColor(grid, x, y):
