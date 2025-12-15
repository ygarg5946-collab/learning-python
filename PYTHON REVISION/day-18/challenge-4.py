from turtle import Turtle,Screen
import turtle as t
timmy=Turtle()
t.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return random_color
screen=Screen()
# colours=['red','green','blue','yellow','magenta','cyan']
directions=[0,90,180,270]
import random
timmy.pensize(15)
timmy.speed("fastest")
for i in range(500):
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(random.choice(directions))
screen.exitonclick()