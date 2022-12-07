# RubberBandBall.py
import turtle
turtle.bgcolor('black')
t = turtle.Pen()
colors = ['red','yellow','blue','orange', 'green', 'purple']
# vamos escolher o número de lados
sides = 6
for x in range(360):
    t.pencolor(colors[x % sides])
    t.forward(x * 3 / sides + x)
    t.left(360 / sides + 1)
    #t.width(x * sides / 200)
    t.left(90)


