from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update_scoreboard()
    
    
    def update_scoreboard(self):
        self.clear()
        self.goto(0,350)
        self.write("Level", align = "center",font=("Arial",25,"normal"))

    def collision(self):
        self.clear()
        self.goto(0,0)
        self.write("You have collided", align = "center",font=("Arial",50,"normal"))
