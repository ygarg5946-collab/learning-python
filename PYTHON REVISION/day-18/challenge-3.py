#in this challenge i am drawing triangle square pentagon, hexagon
# heptagon, octagon, nonagon, and decagon
from turtle import Turtle,Screen
tim=Turtle()
colours=["red","blue","green","yellow","cyan","magenta","cyan"]
import random
N=10
for i in range(N):
    random_colour = random.choice(colours)
    tim.color(random_colour)
    for j in range(i+3):
        tim.forward(100)
        tim.left(360/(i+3))
screen=Screen()
screen.exitonclick()