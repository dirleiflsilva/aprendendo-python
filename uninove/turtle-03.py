# Relembrando LOGO
# obrigado Prof. Papert

from turtle import *
# movimentando a tartaruga
title("TARTARUGA TOUCHE!") # coloca o título na janela
bgcolor("lightyellow") # coloca a cor de fundo da janela em amarelo claro 
pensize(4)  # define a espessura do traço
color("blue") # cor da tartaruga e do traço
shape("turtle") # coloca o formato da tartaruga
delay(50)
for cont in range(4):
    forward(200) # anda para frente 100 pixels
    right(90)   # vira 90 graus para direita
