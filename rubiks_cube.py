from auxillary_fns import *

cube_pieces = initialize() #change colours as required in auxillary_fns.py (please clear the completed list too if doing so, otherwise changes will not take effect)

#print("\nInitialize the cube using variable = Cube(cube_pieces), Cube methods are:\nprintcube()\nrotate(self,face,opp)\nrotate_cube()\n")
#print("For rotate, face can be str(F or B or U or D or R or L) and opposite should be True if an inverse rotation is required.")

"""
Representation #1 - completed

3D coordinate system to denote each piece's position and colours on each axis

"""

class Cube:
    def __init__(self,cube_pieces):
        self.pieces = cube_pieces #Pieces are a seperate class with their own methods, refer to auxillary_fns

    # Text output print function that prints current state of cube
    def printcube(self):
        print("Taking reference from front-bottom-left corner of cube as (-1,-1,-1)\n")
        
        axis = ("x","y","z")
                
        for i in (-1,1):
            for j in axis:
                row = []
                print("Current face:", j, " = ",i)

                for k in self.pieces:
                    if k.get_coordinate(j) == i:
                        print(k.status_2d(j))
                print("-"*30)

 
    def rotate_x_plane(self,coord):
        """
        Below are the rotation functions to rotate a single slice of the cube (3x3) along a certain plane
        The argument coord is the coordinate of the slice that needs to be rotated along the plane

        i.e. if rotating F (front face), one would call rotate_z_plane(-1), as F is in the Z-plane and is at z = -1.

        Do note that rotation in the opposite direction is equivalent to 3 rotations in the current direction.

        i.e F' == 3*F
        """
        face = list(filter(lambda y: y.get_coordinate("x") == coord,self.pieces))

        for item in face:
            y = item.y
            z = item.z

            if y == 0 and z == 0: #centre
                continue
                
            elif y in [-1,1] and z in [-1,1]: # corners
                if z == -1:
                    if y == -1:
                        item.y,item.z = -1,1
                    else:
                        item.y,item.z = -1,-1
                else:
                    if y == -1:
                        item.y,item.z = 1,1
                    else:
                        item.y,item.z = 1,-1

            else: #edges
                if y == -1 or y == 1:
                    item.y,item.z = item.z,-item.y
                else:
                    item.y,item.z = item.z,item.y

            item.cy,item.cz = item.cz,item.cy
            

    def rotate_y_plane(self,coord):
        face = list(filter(lambda z: z.get_coordinate("y") == coord,self.pieces))

        for item in face:
            x = item.x
            z = item.z

            if x == 0 and z == 0: #centre
                continue
                
            elif x in [-1,1] and z in [-1,1]: # corners
                if z == -1:
                    if x == -1:
                        item.x,item.z = -1,1
                    else:
                        item.x,item.z = -1,-1
                else:
                    if x == -1:
                        item.x,item.z = 1,1
                    else:
                        item.x,item.z = 1,-1

            else: #edges
                if x == -1 or x == 1:
                    item.x,item.z = item.z,-item.x
                else:
                    item.x,item.z = item.z,item.x

            item.cx,item.cz = item.cz,item.cx
        

    def rotate_z_plane(self,coord):
        face = list(filter(lambda x: x.get_coordinate("z") == coord,self.pieces))

        for item in face:
            x = item.x
            y = item.y

            if x == 0 and y == 0: #centre
                continue
                
            elif x in [-1,1] and y in [-1,1]: # corners
                if y == -1:
                    if x == -1:
                        item.x,item.y = -1,1
                    else:
                        item.x,item.y = -1,-1
                else:
                    if x == -1:
                        item.x,item.y = 1,1
                    else:
                        item.x,item.y = 1,-1

            else: #edges
                if x == -1 or x == 1:
                    item.x,item.y = item.y,-item.x
                else:
                    item.x,item.y = item.y,item.x

            item.cx,item.cy = item.cy,item.cx


    def rotate(self,face,opp = False):
        """
        MASTER ROTATE FUNCTION
        """
        
        def F():
            self.rotate_z_plane(-1)

        def R(inverse = False):
            if inverse:
                self.rotate_x_plane(1)

            else:
                self.rotate_x_plane(1)
                self.rotate_x_plane(1)
                self.rotate_x_plane(1)

        def U():
            self.rotate_y_plane(1)

        def D(inverse = False):
            if inverse:
                self.rotate_y_plane(-1)

            else:
                self.rotate_y_plane(-1)
                self.rotate_y_plane(-1)
                self.rotate_y_plane(-1)            

        def L():
            self.rotate_x_plane(-1)

        def B(inverse = False):
            if inverse:
                self.rotate_z_plane(1)

            else:
                self.rotate_z_plane(1)
                self.rotate_z_plane(1)
                self.rotate_z_plane(1)

        if opp and face in ("F","U","L"):
            eval(face + "()")
            eval(face + "()")
            eval(face + "()")

        elif opp:
            eval(face + "(True)")
            
        else:
            eval(face + "()")


    def rotate_cube(self,axis):
        """
        This is to rotate the whole cube
        """
        for i in range(-1,2):
            if axis == "x":
                self.rotate_x_plane(i)

            elif axis == "y":
                self.rotate_y_plane(i)

            else:
                self.rotate_z_plane(i)        
