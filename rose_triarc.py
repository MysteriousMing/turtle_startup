import turtle as t
import random as r
t.setup(900,900)
t.speed(0)
t.bgcolor("#FFFAFA")
t.pencolor("#BC8F8F")
t.pensize(1)

def shape(angle,side,limit):
    rvsdire = 100
    t.circle(-side,60)

    if side%(rvsdire*2) == 0:
        angle = angle + 2
    elif side%rvsdire == 0:
        angle = angle - 2

    t.right(angle-60)
    side +=1
    t.pensize(1+pow(side,0.5)/100)
    if side < limit:
        shape(angle,side,limit)

angle = 119
side = 0
limit = 300
shape(angle,side,limit)

t.done()
