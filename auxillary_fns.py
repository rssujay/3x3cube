# Change colours here --> format as (colour, colour on opposite side)
pairs = (("white","yellow"),
         ("yellow","white"),
         ("red","orange"),
         ("orange","red"),
         ("green","blue"),
         ("blue","green"))
# Make sure there are 6 logically valid pairs

class Piece:
    def __init__(self,x,y,z,cx,cy,cz):
        self.x = x
        self.y = y
        self.z = z

        self.cx = cx
        self.cy = cy
        self.cz = cz

    def status(self):
        return (self.x, self.y, self.z, self.cx, self.cy, self.cz)

    def status_2d(self,axis):
        if axis == "x":
            return (self.cx, "y = " + str(self.y), "z = " + str(self.z))            
        elif axis == "y":
            return (self.cy, "x = " + str(self.x), "z = " + str(self.z))           
        else:
            return (self.cz, "x = " + str(self.x), "y = " + str(self.y))
        

    def get_coordinate(self,axis):
        if axis == "x":
            coord = self.x            
        elif axis == "y":
            coord = self.y            
        else:
            coord = self.z
        return coord

    def get_colour(self,axis):
        if axis == "x":
            colour = self.cx            
        elif axis == "y":
            colour = self.cy            
        else:
            colour = self.cz
        return colour

        
            

#use completed pieces for default cube, if you wish to re-generate using new colours, clear the list, i.e. completed_pieces = []
# do note that this will require your input in assembling the cube piece by piece
completed_pieces = [Piece(-1,-1,-1,'red','blue','white'),
                    Piece(-1,-1,0,'red','blue',None),
                    Piece(-1,-1,1,'red','blue','yellow'),
                    Piece(-1,0,-1,'red',None,'white'),
                    Piece(-1,0,0,'red',None,None),
                    Piece(-1,0,1,'red',None,'yellow'),
                    Piece(-1,1,-1,'red','green','white'),
                    Piece(-1,1,0,'red','green',None),
                    Piece(-1,1,1,'red','green','yellow'),
                    Piece(0,-1,-1,None,'blue','white'),
                    Piece(0,-1,0,None,'blue',None),
                    Piece(0,-1,1,None,'blue','yellow'),
                    Piece(0,0,-1,None,None,'white'),
                    Piece(0,0,1,None,None,'yellow'),
                    Piece(0,1,-1,None,'green','white'),
                    Piece(0,1,0,None,'green',None),
                    Piece(0,1,1,None,'green','yellow'),
                    Piece(1,-1,-1,'orange','blue','white'),
                    Piece(1,-1,0,'orange','blue',None),
                    Piece(1,-1,1,'orange','blue','yellow'),
                    Piece(1,0,-1,'orange',None,'white'),
                    Piece(1,0,0,'orange',None,None),
                    Piece(1,0,1,'orange',None,'yellow'),
                    Piece(1,1,-1,'orange','green','white'),
                    Piece(1,1,0,'orange','green',None),
                    Piece(1,1,1,'orange','green','yellow')]

def check_duplicate(tup1,tup2):
    return sorted(tup1) == sorted(tup2)

def create_pieces(pairs):
    """
    generates the 26 possible cubes in a standard 3x3 rubik's cube,
    given 6 pairs of colours in the following format:

    (colour, colour on opposite side)

    returns a dictionary with the following 3 keys: "centres", "sides", "corners"
    """
    class Colour:
        def __init__(self,name,opposite):
            self.name = name
            self.opposite = opposite

    def generate_colours(pairs):
        def remove_duplicates(tup):
            new = []
            for i in tup:
                if i not in new:
                    new.append(i)
            return new
        
        base = []
        colourdict = {}    
        colours = {'centres':[],'sides':[],'corners':[]}
        
        for a in pairs:
            base.append(Colour(*a))

        for b in base:
            colourdict[b.name] = b
            
        #generating all possible pieces
        combinations = list(map(lambda x: [x],colourdict.keys()))
        current = list(colourdict.keys())
        colours['centres'] = combinations.copy()
            
        for i in current:
            for j in current:
                if (colourdict[i].name != j) and (colourdict[i].opposite != j):
                    combinations.append((i,) + (j,))

        combinations = list(filter(lambda x: len(x) == 2,combinations))
        colours['sides'] = remove_duplicates(list(map(sorted,combinations)))

        temp = []
        for side in combinations:
            face1,face2 = side
            for col in current:
                if not((col == face1 or col == colourdict[face1].opposite) or (col == face2 or col == colourdict[face2].opposite)):
                    temp.append(side + (col,))                    

        combinations = list(filter(lambda x: len(x) == 3,temp))
        colours['corners'] = remove_duplicates(list(map(sorted,combinations)))

        return colours
    return generate_colours(pairs)

def generate_positions():
    lst = []
    pieces = []
    
    for i in range(-1,2):
        for j in range(-1,2):
            for k in range(-1,2):
                if k == 0 and j == 0 and i == 0:
                    continue
                else:
                    lst.append([i,j,k])

    for j in lst:
        pieces.append(Piece(*j,None,None,None))

    return pieces
        

def initialize():
    """
    can probably be made better,
    without requiring manual user input
    """
    if completed_pieces:
        print("Using pre-assembled default cube pieces!\nYou can call the cube pieces using the variable 'cube_pieces'")
        return completed_pieces

    else:
        print("Colours unrecognized! \nPlease assist me in building the cube manually \n(A solved cube may come in handy here)")
        valid_combinations = create_pieces(pairs)
        combis = []
        
        for key in valid_combinations:
            for combination in valid_combinations[key]:
                combis.append(sorted(combination))
        
        pieces = generate_positions()
        assembled = []

        for p in pieces:
            ans = []

            while not sorted(list(filter(lambda x: x != "None",ans))) in combis:
                print(sorted(list(filter(lambda x: x != "None",ans))))

                print("You will need to try again if you enter an invalid combination! Enter 'None' if that axis has no visible colour sticker \n\n")
                ans = []

                print("You can choose from the following valid combinations \n\n",combis,"\n")
                
                print("x:",p.x,"y:",p.y,"z:",p.z)
                ans.append(input("Enter x axis colour"))
                ans.append(input("Enter y axis colour"))
                ans.append(input("Enter z axis colour"))

            p.cx,p.cy,p.cz = map(lambda x: None if x == "None" else x,ans)
            assembled.append(p)
            print(ans)
            combis.remove(sorted(list(filter(lambda x: x != "None",ans))))
            print("Successful! The piece has been added to the cube")

        return assembled
            
        
        

                
        
        
        
