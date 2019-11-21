import random

def setup():
    size(800, 600, P2D)
    global a,b,v
    a = width/2
    b = height/2
    v = PVector(5,4)
    
def draw():
    background(255)
    noStroke()
    fill(168, 98, 50)
    global a,b,v
    ellipse(a, b, 50, 50)
    a += v.x
    b += v.y
    
    if a > width - 100 or a < 100:
        v.x = v.x*-1
    
    if b > height - 100 or b < 100:
        v.y = v.y*-1
    
def mousePressed():
    global a,b,v
    if mouseX > a-25 and mouseX < a+25:
        a = random.randint(100,700)
        b = random.randint(100,500)
        v = v * -random.uniform(1,1.04)
        redraw()
        
