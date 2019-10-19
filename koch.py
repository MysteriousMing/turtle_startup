import turtle as t
import random
t.setup(1000,1000)
t.colormode(255)
t.speed(0)
def koch(size,n):
    if n == 0:
        t.fd(size)
    else:
        for angle in [0,60,-120,60]:
            t.left(angle)
            koch(size/3,n-1)

for i in range(100):
    t.bgcolor(2*i+55,2*i+52,2*i+52)
    t.pencolor(2*i,255-2*i,255-i)
    koch(i*2,int(i**0.3))
    t.right(120)
