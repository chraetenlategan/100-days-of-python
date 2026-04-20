from turtle import Turtle,Screen
from chicken import Chicken
from finishline import Finish
from car import Car
from scoreboard import Scoreboard
import random,time


screen = Screen()
scoreboard = Scoreboard()
screen.setup(height=1000,width = 1000)
screen.tracer(0)
chicken = Chicken()
finish =  Finish()


#spawn cars

cars = []
directions = [1,-1]
speed = 1
level = 1

def spawn_cars():
    starty = -350
    for i in range(10):
        new_car = Car()
        direction = random.choice(directions)
        if direction == -1:
            new_car.setheading(180)
        cars.append(new_car)
        new_car.goto(x=-450*direction + random.randint(-200,200),y=starty)
        starty += 80
    screen.ontimer(spawn_cars, 5000)

screen.listen()
screen.onkey(chicken.move_forward,"w")
screen.onkey(chicken.move_left,"a")
screen.onkey(chicken.move_down,"s")
screen.onkey(chicken.move_right,"d")

game_is_on = True

spawn_cars()
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    scoreboard.update_scoreboard()
    for car in cars:
        if car.distance(chicken) <= 25:
            game_is_on =  False
        car.forward(random.randint(1*speed,3*speed))

screen.exitonclick()
