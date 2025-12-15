#now starting the day-20
#Building of the famous snake game!!
#we will be building this game in 7 major steps
# so now start with first step-1
import turtle
from turtle import Turtle,Screen
import time
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My SNAKE Game")
screen.tracer(0)
turtle_list=[]
for i in range(3):
    tim=Turtle("square")
    tim.penup()
    tim.color("white")
    tim.goto(-20*i,0)
    turtle_list.append(tim)
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for tim in range(len(turtle_list)-1,0,-1):
        new_x=turtle_list[tim-1].xcor()
        new_y=turtle_list[tim-1].ycor()
        turtle_list[tim].goto(new_x,new_y)
    turtle_list[0].forward(20)
    turtle_list[0].left(90)



screen.exitonclick()

