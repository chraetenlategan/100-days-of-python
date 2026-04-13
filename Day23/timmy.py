from turtle import Turtle

class Timmy(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.reset_position(self)
    
    def move_up(self):
        self.setheading(90)
        self.forward(10)

    def move_down(self):
        self.setheading(270)
        self.forward(10)

    def move_left(self):
        self.setheading(180)
        self.forward(10)

    def move_right(self):
        self.setheading(0)
        self.forward(10)
    
    def reset_position(self,screen):
        self.setheading(90)
        self.goto(0,-380)
