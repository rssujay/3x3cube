# 3x3cubebuilder
This project is coded in Python 3.6+.
A simple first project inspired by the well-known 3x3 Rubik's Cube.

How to open: Open rubiks_cube.py with auxillary_fns.py in the same folder.

The aim of this project is to build an appropriate representation for the Rubik's Cube such that further extensions,
such as a solver AI or GUIs, can be made for the purposes of learning or trying out cubing on the computer. As this
is a beginner project, there will be minimal use of imported modules which may be helpful (such as numPy arrays). This project makes use of functional and object-oriented programming.

The currently coded functions/classes are:
1) An initializer function which either initializes the default 3x3 cube, or generates a custom 3x3 cube with non-standard stickers 
using user input.

2) A piece creator function which outputs strictly valid pieces (i.e. the resultant cube must be solvable) based on input colours. This
is used as a guide inside the initialization function when generating any non-default cube.

3) Some other auxillary functions to assist in the execution of the above two functions.

4) A piece class which represents a single cube piece (either a corner,edge or centre) and keeps track of the piece's location 
using XYZ coordinates and the stickers on each of its axis.

5) A cube class and a colour class (for the different representations detailed below).

6) Basic printcube methods which output a text-based representation of the current state of the cube.

7) A fully working coordinate system based representation of a rubik's cube with face rotation and perspective rotation support!

Further improvements/ideas:

1) Complete the alternative 2D array representation (rubiks_cube_alternative.py).

2) Additional functionalities - graphics, cube randomizer (using random module), cube solver

Thank you for reading and have a nice day! criticism/suggestions/pull requests are welcome.
