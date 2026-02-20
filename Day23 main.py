from turtle import Turtle,Screen
from car import Car
from timmy import Timmy
import random,time

#Screen Setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=800)
screen.tracer(0)

#Create 8 cars
cars = [Car() for _ in range(8)]

for i in range(len(cars)):
    cars[i].spawn(screen, i, len(cars))

tim = Timmy()

screen.listen()
screen.onkey(tim.move_up,"w")
screen.onkey(tim.move_down,"s")
screen.onkey(tim.move_left,"a")
screen.onkey(tim.move_right,"d")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for car in cars:
        car.forward(5)



screen.exitonclick()
