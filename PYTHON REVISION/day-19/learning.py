#understading the turtle coordinate system
from turtle import Turtle,Screen
is_on=True
import random
screen=Screen()
screen.setup(800,600)
user_guess=screen.textinput(title="Make Your Bet",prompt="Which turtle will win the race? Enter a color: ")
colors=['red','yellow','blue','green','purple','cyan']
turtles_list=[]
for i in range(0,6):
    timm = Turtle("turtle")
    timm.color(colors[i])
    timm.penup()
    timm.goto(-380,250-50*i)
    turtles_list.append(timm)
while is_on:
    for turtle in turtles_list:
        if turtle.xcor()>380:
            is_on=False
            if turtle.pencolor()==user_guess:
                print(f"You Win!! The correct color was {turtle.pencolor()}")
            else:
                print(f"You Lose! The correct color was {turtle.pencolor()}")
        random_distance=random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()
