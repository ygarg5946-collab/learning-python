from turtle import Turtle,Screen
timmy=Turtle()
screen = Screen()
timmy.speed("fastest")
screen.listen()
def forward():
    timmy.forward(100)
def backward():
    timmy.backward(100)
def clockwise():
    timmy.right(10)
def anticlockwise():
    timmy.left(10)
def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()
screen.onkey(key="W",fun=forward)
screen.onkey(key="S",fun=backward)
screen.onkey(key="A",fun=anticlockwise)
screen.onkey(key="D",fun=clockwise)
screen.onkey(key="C",fun=clear)
screen.exitonclick()

