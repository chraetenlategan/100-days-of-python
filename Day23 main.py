from turtle import Turtle,Screen
from car import Car

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=800)
screen.tracer(0)

vroom = Car()
screen.update()


screen.exitonclick()
