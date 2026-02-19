from turtle import Turtle,Screen
from car import Car
import random

#Screen Setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=800)
screen.tracer(0)

#Create 8 cars
cars = [Car() for _ in range(8)]
# The possible fix position for cars
car_positions = [
    (-500, -400), 
    (-500, -300), 
    (-500, -200), 
    (-500, -100), 
    (-500, 0), 
    (-500, 100), 
    (-500, 200), 
    (-500, 300), 
    (-500, 400)
]


for i in range (len(cars)):
    car.goto(car_positions[i-1])





screen.update()
screen.exitonclick()
