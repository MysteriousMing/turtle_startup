
import random

def setup():
    size(800,600,P2D)
    frameRate(80)
    
def draw():
    background(0,0,0)
    
    for i in range(255):
        noFill()
        noStroke()
        stroke(255-i,255-i,255-i, 60)
        ellipse(mouseX, mouseY, i, i)
    
    x0 = random.randint(-100,100) 
    y0 = random.randint(-100,100)
    a = 6
    b = 5
    
    noStroke()
    fill(255,242,204)
    ellipse(mouseX+x0, mouseY+y0, a, a)
    ellipse(mouseX+x0/1.7, mouseY-y0/0.8, a, a)
    ellipse(mouseX-x0, mouseY-y0, b, b)
    ellipse(mouseX-x0/2, mouseY+y0/2, b, b)
    ellipse(mouseX+x0/2, mouseY-y0/2, b, b)
    ellipse(mouseX-x0/1.5, mouseY-y0/2, b, b)
    ellipse(mouseX+x0/2, mouseY+y0/1.5, b, b)
    
    stroke(255,255,255)
    strokeWeight(1)
    line(mouseX, mouseY, mouseX+x0, mouseY+y0)
    line(mouseX, mouseY, mouseX-x0/2, mouseY+y0/2)
    line(mouseX, mouseY, mouseX+x0/1.7, mouseY-y0/0.8)
    
    for i in range(5):
        line(mouseX+x0, mouseY+y0, mouseX+x0+random.randint(-15,15), mouseY+y0+random.randint(-15,15))
        line(mouseX+x0, mouseY+y0, mouseX+x0+random.randint(-15,15), mouseY+y0+random.randint(-15,15))
    
    for j in range(8):
        line(mouseX+x0/1.7, mouseY-y0/0.8, mouseX+x0/1.7+random.randint(-25,25), mouseY-y0/0.8+random.randint(-25,25))
        line(mouseX+x0/1.7, mouseY-y0/0.8, mouseX+x0/1.7+random.randint(-25,25), mouseY-y0/0.8+random.randint(-25,25))
