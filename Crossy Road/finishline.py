from turtle import Turtle

class Finish(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=-500,y=400)
        self.setheading(0)
        self.pendown()
        self.forward(1000)