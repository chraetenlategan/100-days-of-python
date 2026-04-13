from turtle import Turtle,Screen
import random
colours = ["red", "blue", "green", "yellow", "purple", "orange"]

screen = Screen()
screen.setup(width=500,height=400)
user_bet =screen.textinput(title="Make your bet",prompt="Which turtle will win the race. Enter a color").lower()


#make a finish line
finish = Turtle()
finish.penup()
finish.goto(x=200,y=160)
finish.pendown()
finish.pensize(5)
finish.goto(x=200,y=-160)


h = 150
all_turtles=[]


#This is a parallel list
for i in colours:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(i)
    new_turtle.goto(x=-230,y= h)
    h-=50
    all_turtles.append(new_turtle)

finished = False
while not finished:
    for racer in all_turtles:
        racer.forward(random.randint(20,100))
        if racer.xcor() >= 200:
            finished = True
            winning_color = racer.pencolor()

            if user_bet == winning_color:
                msg = f"Winner: {winning_color}! You won!"
            else:
                msg = f"Winner: {winning_color}! You lost."

            racer.write(msg, align="center", font=("Courier", 20, "bold"))
            break

screen.exitonclick()
