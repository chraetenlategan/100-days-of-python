from turtle import Turtle
import random
class Car(Turtle):

    colors = ["red", "blue", "green", "orange", "purple", "gold", "cyan", "hotpink"]
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(self.colors))
        self.shapesize(stretch_wid = 1, stretch_len =3)
