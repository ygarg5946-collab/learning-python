#day-19 starting
#more about the turtle graphics, even listeners,state & multiple instances
#Turtle Event Listeners
from turtle import Turtle,Screen
timm = Turtle()
screen = Screen()
def move_forward():
    timm.forward(10)
screen.listen()
screen.onkey(key="space",fun=move_forward)
screen.exitonclick()
