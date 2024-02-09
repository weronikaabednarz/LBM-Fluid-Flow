# LBM Fluid Flow

Imitation of the movement of substance molecules.

Project description:

Modification of the initialize_matrix function by setting the
the input and output concentration values for the 9 directions.
The walk function is responsible for simulating the movement of the squares on the board according to the rules of cellular automata. Leaving the execution of the streaming operation and, 
if it encounters a wall, rebounding depending on its alignment. Adding a speed limit to avoid negative values for large density differences. Applying calculations according to the formulas 𝑏 = 8 𝜏 = 1.

"Direction" defines the directions of movement for squares (𝑐1).
"Weight" defines the value added for each direction of movement for the squares.

Technologies used in the project: Python with libraries:
- numpy - a library for scientific calculations, operations on multidimensional arrays and matrices,
- pygame - a set of Python modules designed for writing video games. Pygame adds functionality on top of the excellent SDL library,
- random - a built-in module that you can use to make random numbers,
- PIL - a module for image handling.

Start picture:

![1](https://github.com/weronikaabednarz/LBM-Fluid-Flow/blob/main/images/frame0.bmp)

Continued picture:

![2](https://github.com/weronikaabednarz/LBM-Fluid-Flow/blob/main/images/frame8.bmp)

Continued picture:

![3](https://github.com/weronikaabednarz/LBM-Fluid-Flow/blob/main/images/frame35.bmp)

Continued picture:

![4](https://github.com/weronikaabednarz/LBM-Fluid-Flow/blob/main/images/frame165.bmp)

Continued picture:

![5](https://github.com/weronikaabednarz/LBM-Fluid-Flow/blob/main/images/frame543.bmp)

Continued picture:

![6](https://github.com/weronikaabednarz/LBM-Fluid-Flow/blob/main/images/frame646.bmp)

Final picture:

![7](https://github.com/weronikaabednarz/LBM-Fluid-Flow/blob/main/images/frame2071.bmp)
