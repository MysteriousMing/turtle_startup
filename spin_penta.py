import turtle as t
t.bgcolor("black")
t.speed(0)
Colorset = ["#008080","#2E8B57","#00FF7F","#98FB98","#FF7F50"]
t.pensize(3)
for i in range(300):
    t.pencolor(Colorset[i%5])
    t.width(i/100+1)
    t.fd(i)
    t.left(71)
t.done()
