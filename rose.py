import turtle as t
import random as r
t.setup(900,900)
t.speed(0)
t.bgcolor("#FFFAFA")
t.pencolor("#BC8F8F")
t.pensize(1)

def shape(angle,side,limit):
    rvsdire = 200
    t.fd(side)

    if side%(rvsdire*2) == 0:
        angle = angle + 2
    elif side%rvsdire == 0:
        angle = angle - 2

    t.right(angle)
    side +=2
    t.pensize(1+pow(side,0.5)/10)
    if side < limit:
        shape(angle,side,limit)

angle = 119
side = 0
limit = 600
shape(angle,side,limit)

t.done()
