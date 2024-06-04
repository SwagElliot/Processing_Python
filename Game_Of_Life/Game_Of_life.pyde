from random import choice

GRID_W = 59
GRID_H = 59

play = False;

SZ= 20

generation = 0

def setup():
    #noStroke()
    global SZ,cellList
    size(700, 700)
    SZ = width // GRID_W +1
    cellList = createCellList()
    
def draw():
    global generation, cellList
    frameRate(5)
    if play == True:
        cellList = update(cellList)
    for row in cellList:
        for cell in row:
            cell.display()
        
def update(cellList):
    newList = []
    for r,row in enumerate (cellList):
        newList.append([])
        for c,cell in enumerate(row):
            newList[r].append(Cell(c,r,cell.checkNeighbors()))
    return newList [::]

def createCellList():
    newList=[]
    for j in range(GRID_H):
        newList.append([])
        for i in range(GRID_W):
          #  newList [j].append(Cell(i,j, choice([0,1])))
            newList [j].append(Cell(i,j))
    return newList
        
class Cell:
    def __init__(self, c, r, state = 0):
        self.c = c
        self.r = r
        self.state = state
    def display(self):
        if self.state == 1:
            fill(0)
        else:
            fill (255)
        rect(SZ*self.r, SZ * self.c, SZ, SZ)
    def checkNeighbors(self):
        neighbs = 0
        for dr, dc in [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]:
            try:
                if cellList[self.r + dr][self.c + dc].state == 1:
                    neighbs += 1
            except IndexError:
                continue
        if self.state == 1:
            if neighbs in [2,3]:
                return 1
            return 0
        if neighbs == 3:
            return 1
        return 0
    def mouseOn(self):
        if SZ*self.r < mouseX < SZ*self.r + SZ and SZ*self.c < mouseY < SZ*self.c + SZ:
            if self.state == 0:
                self.state = 1
            else: self.state = 0
        return 0
        
    
def keyPressed():
    global play
    if key == ' ':
        if play == True:
            play = False
        elif play == False:
            play = True
            
def mousePressed():
    global cellList, state
    for row in cellList:
        for cell in row:
            cell.mouseOn()

    
