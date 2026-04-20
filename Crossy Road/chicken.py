from turtle import Turtle

class Chicken(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.hideturtle()
        self.goto(x=0,y=-400)
        self.showturtle()

    def move_forward(self):
        self.setheading(90)
        self.forward(10)

    def move_right(self):
        self.setheading(0)
        self.forward(10)

    def move_left(self):
        self.setheading(180)
        self.forward(10)

    def move_down(self):
        self.setheading(270)
        self.forward(10)

    



