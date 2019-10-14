import turtle as t
t.bgcolor("black")
t.speed(0)
colorset = ["black","#FA8072","black","#FF6347","black"]

def ptr(angle,side,limit):
    rvsdire = 80
    t.fd(side)

    if side%(rvsdire*2) == 0:
        angle = angle + 2
    elif side%rvsdire == 0:
        angle = angle - 2

    t.left(angle)
    side +=1
    t.pensize(1+pow(side,0.5)/10)
    t.pencolor(colorset[side%5])
    if side < limit:
        ptr(angle,side,limit)

angle = 71
side = 0
limit = 320
ptr(angle,side,limit)

t.done()
