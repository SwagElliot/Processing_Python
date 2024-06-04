from random import choice

WHITE = color(255)
BROWN = color(102,51,0)
RED = color(255,150,150)
GREEN = color(0,102,0)
YELLOW = color(255,255,120)
PURPLE = color(220,160,255)
ORANGE = color(255,202,14)
GREY = color(50,50,50)
LIME = color(150,232,150)

colorList = [WHITE, RED, YELLOW, PURPLE, ORANGE, LIME]

class Sheep:
    def __init__(self,x,y, col):
        self.x = x
        self.y = y
        self.sz = 15
        self.energy = 20
        self.energyValue = 10
        self.col = col

        
    def update(self):
        move = 2
        viewDistance = 100
        runSpeed = 10
        if self.col == LIME:
            viewDistance = 200
        if self.col == PURPLE:
            move = 2.3
            runSpeed = 1.2
        if self.col == YELLOW:
            self.energy -= 0.125
        else: self.energy -= 0.15
        if self.energy <= 0:
            sheepList.remove(self)
        if self.col == RED:
            if self.energy >= 40:
                self.energy -= 20
                if random(100) < 5:
                    sheepList.append(Sheep(self.x,self.y,choice(colorList)))
                else: sheepList.append(Sheep(self.x,self.y,self.col))
        if self.energy >= 50:
            self.energy -= 30
            if random(100) < 5:
                sheepList.append(Sheep(self.x,self.y,choice(colorList)))
            else: sheepList.append(Sheep(self.x,self.y,self.col))
        if self.x > width:
            self.x %= width
        if self.y > height:
            self.y %= height
        if self.x < 0:
            self.x += width
        if self.y < 0:
            self.y += height
        xscl = int(self.x/patchSize)
        yscl = int(self.y/patchSize)
        grass = grassList[xscl * rows_of_grass + yscl]
        if not grass.eaten:
            self.energy += grass.energyValue
            grass.eaten = True
        fill(self.col)
        ellipse(self.x, self.y, self.sz, self.sz)
        for wolf in wolfList:
            try:
                if abs(self.x - wolf.x) < killDist and abs(self.y - wolf.y) < killDist:
                    sheepList.remove(self)
                    if self.col == ORANGE:
                        if random(100) < 20:
                            wolfList.remove(wolf)
                    wolf.energy += self.energyValue
            except:
                continue
        
        
        
        for wolf in wolfList:
            if sqrt(pow((self.x - wolf.x), 2) + pow((self.y - wolf.y), 2)) < viewDistance:
                self.x += runSpeed * cos(self.x - wolf.x)
                self.y += runSpeed * sin(self.y - wolf.y)
                break
            else:
                self.x += random(-move,move)
                self.y += random(-move, move)
                break
            
        
        
        
        
class Grass:
    def __init__(self, x, y, sz):
        self.x = x
        self.y = y
        self.energyValue = 5
        self.eaten = False
        self.sz = sz
    def update(self):
        if self.eaten:
            if random(100) < 0.5:
                self.eaten = False
            else:
                fill(BROWN)
        else:
            fill(GREEN)
        rect(self.x, self.y, self.sz, self.sz)

class Wolf:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sz = 20
        self.energy = 30
        self.hasTarget = False
    def update(self):
        move = 3
        self.energy -= 0.25
        if self.energy <= 0:
            wolfList.remove(self)
        if self.energy >= 70:
            self.energy -= 40
            wolfList.append(Wolf(self.x,self.y))
            
        #Moving
        if self.hasTarget == True:
            if self.x > self.xTarget:
                self.x -= 1.4
            if self.x < self.xTarget:
                self.x += 1.4
            if self.y > self.yTarget:
                self.y -= 1.4
            if self.y < self.yTarget:
                self.y += 1.4
            if abs(self.x - self.xTarget) < 5 and abs(self.y - self.yTarget) < 5:
                self.hasTarget = False
                
        else:
            self.x += random(-move,move)
            self.y += random(-move, move)
            for sheep in sheepList:
                if sqrt(pow(self.x - sheep.x,2) + pow(self.y - sheep.y,2)) < targetDistance:
                    self.xTarget = sheep.x
                    self.yTarget = sheep.y
                    self.hasTarget = True
                    break
            
            
        if self.x > width:
            self.x %= width
        if self.y > height:
            self.y %= height
        if self.x < 0:
            self.x += width
        if self.y < 0:
            self.y += height
        fill(GREY)
        ellipse(self.x, self.y, self.sz, self.sz)
        
        # #Colission
        # for wolf in wolfList:
        #     if abs(self.x - wolf.x) < 8 and abs(self.y - wolf.y) < 8:
        #             if self.x > wolf.x:
        #                 self.x += 5
        #             if self.x < wolf.x:
        #                 self.x -= 5
        #             if self.y > wolf.y:
        #                 self.y += 5
        #             if self.y < wolf.y:
        #                 self.y -= 5
                
        

sheepList = []
grassList = []
wolfList = []
patchSize = 6
killDist = 10
targetDistance = 50

def setup():
    global patchSize, rows_of_grass
    size(600,600)
    rows_of_grass = height/patchSize
    noStroke()
#    for i in range (10):
 #       wolfList.append(Wolf(random(width),
  #                           random(height)))
    for i in range (50):
        sheepList.append(Sheep(random(width),
                               random(height),
                               choice(colorList)))
    for x in range (0, width, patchSize):
        for y in range(0, height, patchSize):
            grassList.append(Grass(x,y,patchSize))
    
def draw():
    background(255)
    for grass in grassList:
        grass.update()
    for wolf in wolfList:
        wolf.update()
    for sheep in sheepList:
        sheep.update()


def mouseClicked():
    wolfList.append(Wolf(mouseX,
                             mouseY))
