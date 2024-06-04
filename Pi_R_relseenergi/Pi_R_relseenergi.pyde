class Cube:
    def __init__ (self, mass, velocity, x):
        self.mass = mass
        self.velocity = velocity
        self.sz = 50
        self.y = height/2
        self.x = x

        
    def update(self):
        global collisions, velMult
        self.x += self.velocity * velMult
        
        #Bounce
        if self.x <= wallPos:
            self. velocity = self.velocity * (-1)
            collisions += 1
            self.x = wallPos
            
        self.render()
    
    def render(self):
        fill(255)
        self.y = (height-50) - self.sz
        rect(self.x, self.y,self.sz, self.sz)

        
        
cubeList = []
collisions = 0
wallPos = 50
velMult = 1.0

def setup():
    size(800,600)
    cubeList.append(Cube(1.0, 0.0, wallPos + 200))
    cubeList.append(Cube(pow(100.0,2), -1.0, width-150)) #Massan måste vara 100^x

def draw():
    backdrop()
    fill(255)
    textSize(25)
    text('Collisions: ' + str(collisions), wallPos+25, 25)
    text('Velocity Multiplier: ' + str(velMult), wallPos+25, 75)

    for cube in cubeList:
        cube.update()
    
    coll = False
    for cube1 in cubeList:
        for cube2 in cubeList:
            if cube1 is not cube2:
                coll = collisioncheck(cube1,cube2)
                if coll == True:
                    break
        if coll == True:
            break
        
        
        
def collisioncheck(cube1,cube2):
    global collisions
    
    if cube1.x <= cube2.x + cube2.sz and cube1.x > cube2.x or cube1.x + cube1.sz >= cube2.x and cube1.x < cube2.x:
        velocity1 = ((cube1.mass - cube2.mass)/(cube1.mass + cube2.mass))*cube1.velocity + (2*cube2.mass/(cube1.mass + cube2.mass))*cube2.velocity
        velocity2 = ((cube2.mass - cube1.mass)/(cube2.mass + cube1.mass))*cube2.velocity + (2*cube1.mass/(cube2.mass + cube1.mass))*cube1.velocity
        
        collisions += 1

        cube1.velocity = velocity1
        cube2.velocity = velocity2
        
        return True
    else:
        return False
        
        
def backdrop():
    background(0)
    fill(100)
    rect(0,0,wallPos,height)
    rect(0,height-50,width,50)
    
    
def keyPressed():
    global velMult
    if key == 'w':
        velMult = velMult *10
    if key == 's':
        velMult = velMult * 0.1
