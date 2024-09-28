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


