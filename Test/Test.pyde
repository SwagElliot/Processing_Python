GRID_W = 50
GRID_H = 50
 
#Size of cell
#SZ = 18
 
def setup():
    global SZ,cellList
    size(600,600)
    SZ = width // GRID_W 
    cellList = createCellList()
def draw():
    background(255)
    for row in cellList:
        for cell in row:
            cell.display()
class Cell:
    def __init__(self,c,r,state=0):
        self.c = c
        self.r = r
        self.state = state
    def display(self):
        if self.state == 1:
            fill(0)
        else:
            fill(255)
        #noStroke()
        rect(SZ*self.r,SZ*self.c,SZ,SZ)
 
 
       

def createCellList():
    newList=[]
    for j in range(GRID_H):
        newList.append([])
        for i in range(GRID_W):
            newList [j].append(Cell(i,j,0))
    newList [GRID_H//2][GRID_W//2].state = 1
    return newList
