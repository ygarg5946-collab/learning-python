from turtle import Turtle
class Snake():
    def __init__(self):
        self.turtle_list=[]
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            tim = Turtle("square")
            tim.penup()
            tim.color("white")
            tim.goto(-20 * i, 0)
            self.turtle_list.append(tim)
    def move(self):
        for tim in range(len(self.turtle_list) - 1, 0, -1):
            new_x = self.turtle_list[tim - 1].xcor()
            new_y = self.turtle_list[tim - 1].ycor()
            self.turtle_list[tim].goto(new_x, new_y)
        self.turtle_list[0].forward(20)

