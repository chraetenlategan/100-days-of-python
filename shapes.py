from turtle import Turtle, Screen
import colorsys
import time
import math

# Your full list
shape_names = [
     "Quadrilateral", "Pentagon", "Hexagon", "Heptagon", 
    "Octagon", "Nonagon", "Decagon", "Hendecagon", "Dodecagon", 
    "Tridecagon", "Tetradecagon", "Pentadecagon", "Hexadecagon", 
    "Heptadecagon", "Octadecagon", "Enneadecagon", "Icosagon", 
    "Icosihenagon", "Icosidigagon", "Icositrigagon", "Icositetragon", 
    "Icosipentagon", "Icosihexagon", "Icosiheptagon", "Icosioctagon", 
    "Icosienneagon", "Triacontagon", "Triacontahenagon", "Triacontadigagon", 
    "Triacontatrigagon", "Triacontatetragon", "Triacontapentagon", 
    "Triacontahexagon", "Triacontaheptagon", "Triacontaoctagon", 
    "Triacontaenneagon", "Tetracontagon", "Tetracontahenagon", 
    "Tetracontadigagon", "Tetracontatrigagon", "Tetracontatetragon", 
    "Tetracontapentagon", "Tetracontahexagon", "Tetracontaheptagon", 
    "Tetracontaoctagon", "Tetracontaenneagon", "Pentacontagon"
]

# Setup
screen = Screen()
screen.bgcolor("#020202") 
screen.setup(width=1000, height=1000)
screen.tracer(0) 

tim = Turtle()
tim.hideturtle()
tim.pensize(3)

writer = Turtle()
writer.hideturtle()
writer.penup()

# --- START SCREEN LOGIC ---
writer.goto(0, 0)
writer.pencolor("white")
writer.write("RAINBOW GEOMETRY\n\nClick anywhere to begin", align="center", font=("Arial", 30, "bold"))
screen.update()

def start_program(x, y):
    writer.clear()
    screen.onclick(None) # Disable click so it doesn't restart
    run_animation()

def run_animation():
    side_length = 200 
    global_hue = 0

    for i, name in enumerate(shape_names):
        sides = i + 4 
        
        # 1. GEOMETRY & ZOOM
        angle_rad = math.radians(180 / sides)
        apothem = side_length / (2 * math.tan(angle_rad))
        
        # Increased padding slightly to give the text even more room
        padding = apothem * 2.0
        screen.setworldcoordinates(-padding, -padding, padding, padding)
        
        # 2. LABELS (Moved Lower: from 0.82 to 0.75)
        writer.clear()
        writer.goto(0, padding * 0.75) 
        
        # Dynamic Color for Text
        text_rgb = colorsys.hsv_to_rgb(global_hue % 1.0, 0.6, 1)
        writer.pencolor(text_rgb)
        writer.write(f"{sides}-sided: {name}", align="center", font=("Arial", 26, "bold"))
        
        # 3. POSITION
        tim.penup()
        tim.goto(-side_length / 2, -apothem) 
        tim.setheading(0) 
        tim.pendown()
        
        # 4. DRAWING LOOP
        angle = 360 / sides
        for step in range(sides):
            # Advanced Color spectrum
            # Saturation cycles to prevent boring color repeats
            dynamic_sat = 0.6 + 0.4 * math.sin(global_hue * 5)
            color = colorsys.hsv_to_rgb(global_hue % 1.0, dynamic_sat, 1)
            tim.pencolor(color)
            
            tim.forward(side_length)
            tim.left(angle)
            
            global_hue += 0.003 # Hue crawls across the spectrum
            
            screen.update()
            # SLOWER SPEED: Adjust this for how fast you want the lines to draw
            time.sleep(0.02) 
        
        # Pause after each shape finishes
        time.sleep(0.4)

# Tell the screen to listen for the click
screen.onclick(start_program)
screen.listen()
screen.mainloop()
