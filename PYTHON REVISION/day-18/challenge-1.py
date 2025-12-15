#use turtle and make a square on the screen
from turtle import Turtle,Screen
tim=Turtle()
screen=Screen()
tim.color("red")
tim.shape("turtle")
# timmy_my_turtle.forward(100)
# timmy_my_turtle.left(90)
# timmy_my_turtle.forward(100)
# timmy_my_turtle.left(90)
# timmy_my_turtle.forward(100)
# timmy_my_turtle.left(90)
# timmy_my_turtle.forward(100)
# timmy_my_turtle.left(90)
for i in range(4):
    tim.forward(100)
    tim.left(90)
screen.exitonclick()
