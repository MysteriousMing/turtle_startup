import turtle as t
t.setup(640,640)
t.bgcolor("black")
t.pensize(4)
t.speed(0)
Colorset = ["#FFF8DC","#FFFAF0","#F5DEB3","#FDF5E6","#FFE4C4","#FFFFF0"]
for i in range (180):
    t.pencolor(Colorset[i%6])
    t.seth(60*i)
    t.circle(30,30+2*i)
    t.circle(-60,45+2*i)
    t.goto(0,0)
t.done()
