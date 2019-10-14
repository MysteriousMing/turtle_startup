import turtle as t
import random as r
t.speed(0)
t.setup(800,800)
t.pensize(3)
t.bgcolor("#1E90FF")
t.pencolor("#F8F8FF")
for i in range(366):
    t.fd(r.randint(0,200))
    t.goto(0,0)
    t.seth(i)
