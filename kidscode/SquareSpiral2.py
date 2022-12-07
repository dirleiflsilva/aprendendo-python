# SquareSpiral2.py - Desenha uma espiral quadrangular
import turtle
t = turtle.Pen()
for x in range(100):
    t.forward(x)
    #t.left(91) #ainda um quadrado
    #t.left(46) #octogono
    #t.left(61) #hexagono
    t.left(121) #triangulo
