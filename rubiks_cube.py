from auxillary_fns import *

cube_pieces = initialize() #change colours as required in auxillary_fns.py

"""
Representation #1 - work in progress

3D coordinate system to denote each piece's position and colours on each axis
"""

class Cube:
    def __init__(self,cube_pieces):
        self.pieces = cube_pieces


    def printcube(self):
        print("Taking reference from front-bottom-left corner of cube as (-1,-1,-1)\n")
        
        faces = []
        axis = ("x","y","z")
                
        for i in (-1,1):
            for j in axis:
                row = []
                print("Current face:", j, " = ",i)

                for k in self.pieces:
                    if k.get_coordinate(j) == i:
                        print(k.status_2d(j))
                print("-"*30)
        
    def rotate(self,direction):
        pass

                    



    
