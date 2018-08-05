"""
Representation #2 - work in progress

3x3 2D array representation (for each of the six faces)

enumerate(issues):
1) Lack of standardized reference for the 9 slots for each face
2) rotation is incorrect as faces are not synced properly (rotation in succession would lead to wrong state)

"""

class Colour:
    def __init__(self,name,opp,left,right,top,btm):
        self.name = name
        self.opp = opp
        self.left = left
        self.right = right
        self.top = top
        self.btm = btm

class Face:
    def __init__(self,colour,opp,left,right,top,btm):
        self.array = [[colour + "1",colour + "2",colour + "3"],[colour + "4",colour +"5",colour + "6"],[colour + "7",colour + "8",colour + "9"]]
        self.top = top
        self.btm = btm
        self.left = left
        self.right = right
        self.opp = opp

    def is_solved(self):
        colours = []
        for i in self.array:
            for j in i:
                if j not in colours:
                    colours.append(j)

        return len(colours) == 1
    

class Cube:
    def __init__(self,pairs):
        self.colours = []
        self.faces = {}
        
        for a in pairs:
            self.colours.append(Colour(*a))
            
        for i in self.colours:
            self.faces[i.name] = Face(i.name,i.opp,i.left,i.right,i.top,i.btm)

    def printcube(self):
        for i in self.faces:
            print("Current face = " + i + "\n")
            for j in self.faces[i].array:
                print(j,"\n")


    def rotate(self,facename):
        temp = self.faces[facename]
        m,left,right,top,btm = temp.array,temp.left,temp.right,temp.top,temp.btm
        
        rows = len(m)
        cols = len(m[0])
        new = [[0] * cols for x in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                new[j][rows - 1 - i] = m[i][j]
        
        self.faces[facename].array = new.copy()

        for k in [left,right,top,btm]:
            if k == top:
                #shift = self.faces[top].array[0]
                self.faces[top].array[0] = self.faces[left].array[0]

            elif k == right:
                #shift = self.faces[right].array[0]
                self.faces[right].array[0] = self.faces[top].array[2]

            elif k == btm:
                #shift = self.faces[btm].array[0]
                self.faces[btm].array[0] = self.faces[right].array[0]

            else:
                #shift = self.faces[left].array[0]
                self.faces[left].array[0] = self.faces[btm].array[2]
    
#The standard colour pairs of the rubik's cube, formatted as (name of colour, opposite side, left, right, top , bottom)
pairs = (("w","y","b","g","r","o"),
         ("y","w","g","b","r","o"),
         ("r","o","b","g","y","w"),
         ("o","r","g","b","y","w"),
         ("g","b","w","y","r","o"),
         ("b","g","y","w","r","o"))
