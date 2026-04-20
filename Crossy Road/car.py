from turtle import Turtle
import random

colors = [
    "Red", "Blue", "Yellow",
    "Green", "Orange", "Purple",
    "Pink", "Magenta", "Cyan", "Teal", "Indigo", "Maroon", "Navy",
]


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(colors))
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=3)


