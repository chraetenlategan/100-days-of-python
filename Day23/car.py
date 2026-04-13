from turtle import Turtle
import random
class Car(Turtle):

    colors = ["red", "blue", "green", "orange", "purple", "gold", "cyan", "hotpink"]
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(self.colors))
        self.shapesize(stretch_wid = 1, stretch_len =3)
        self.penup()
    
    def spawn(self, screen, index, total_cars):
        margin = 50
        playable_height = screen.window_height() - (margin * 2)
        starting_y = -(screen.window_height() / 2) + margin
        
        spacing = playable_height / total_cars
        
        left_edge = -(screen.window_width() / 2) + margin
        right_edge = (screen.window_width() / 2) - margin

        jitter = random.randint(-15, 15) 
        new_y = starting_y + (index * spacing) + jitter
        random_x = random.choice([left_edge, right_edge])
        
        
        if random_x == right_edge:
            self.setheading(180)
            starting_x = right_edge + random.randint(50, 600) 
        else:
            self.setheading(0)
            starting_x = left_edge - random.randint(50, 600)

        self.goto(x=starting_x, y=new_y)
    
    def return_position(self):
        if self.xcor() > 700:
            current_y = self.ycor()
            self.goto(-550,current_y)
        
        elif self.xcor() < -700:
            current_y = self.ycor()
            self.goto(550,current_y)
        
        else:
            pass

        
