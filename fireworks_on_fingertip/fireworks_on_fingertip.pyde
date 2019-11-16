
import random

def setup():
    size(800,600,P2D)
    frameRate(50)
    
def draw():
    background(0,0,0)
    
    for i in range(255):
        noFill()
        noStroke()
        stroke(255-i,255-i,255-i, 60)
        ellipse(mouseX, mouseY, i, i)
    
    x0 = random.randint(-100,100) 
    y0 = random.randint(-100,100) 
    
    noStroke()
    fill(255,255,255)
    ellipse(mouseX+x0, mouseY+y0, 15, 15)
    ellipse(mouseX+x0/1.7, mouseY-y0/0.8, 15, 15)
    ellipse(mouseX-x0, mouseY-y0, 10, 10)
    ellipse(mouseX-x0/2, mouseY+y0/2, 10, 10)
    ellipse(mouseX+x0/2, mouseY-y0/2, 10, 10)
    ellipse(mouseX-x0/1.5, mouseY-y0/2, 10, 10)
    ellipse(mouseX+x0/2, mouseY+y0/1.5, 10, 10)
    stroke(255,255,255)
    strokeWeight(1)
    line(mouseX, mouseY, mouseX+x0, mouseY+y0)
    line(mouseX, mouseY, mouseX-x0/2, mouseY+y0/2)
    line(mouseX, mouseY, mouseX+x0/1.7, mouseY-y0/0.8)
    


    
    
