import turtle as t
t.bgcolor("black")
t.speed(0)
colorset = ["#800000","#CD5C5C","#B22222","#DC143C","#FA8072"]

def ptr(angle,side,limit):
    rvsdire = 100
    t.circle(-side,36)

    if side%(rvsdire*2) == 0:
        angle = angle + 2
    elif side%rvsdire == 0:
        angle = angle - 2

    t.right(angle-36)
    side +=1
    t.pensize(1+pow(side,0.5)/10)
    t.pencolor(colorset[side%5])
    if side < limit:
        ptr(angle,side,limit)

angle = 71
side = 0
limit = 300
ptr(angle,side,limit)

t.done()
