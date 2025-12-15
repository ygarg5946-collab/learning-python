# #first we will learn about the import module
# import turtle
# tim=turtle.Turtle()


# #we can also do like this
# from turtle import Turtle
# # here from the module turtle we have imported the class Turtle



# we can also use like from turtle import * here * represent all the
#classes but this way is not good like you can direct use forward(100)
# but instead we use like this tim.forward() which specifies something

# alias modules: import turtle as t like that


#installing modules
#like if i want to install the hero module
#heroes
#i just know how to install...

#so mujhe iska solution dekhna pada bahut ajeb solution hai
# but very creative and easy
from turtle import Turtle, Screen
tim=Turtle()
tim.shape("turtle")
for i in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
screen=Screen()
screen.exitonclick()