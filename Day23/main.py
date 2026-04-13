from turtle import Turtle,Screen
from car import Car
from timmy import Timmy
from scoreboard import Scoreboard
import random,time

#Screen Setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=800)
screen.tracer(0)

#Create 8 car
car_1 = [Car() for _ in range(random.randint(6,10))]

for i in range(len(car_1)):
    car_1[i].spawn(screen, i, len(car_1))



tim = Timmy()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(tim.move_up,"w")
screen.onkey(tim.move_down,"s")
screen.onkey(tim.move_left,"a")
screen.onkey(tim.move_right,"d")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for car in car_1:
        car.forward(5)
        car.return_position()
        if car.distance(tim) < 25:
            game_is_on = False
            scoreboard.collision()
    

screen.exitonclick()
