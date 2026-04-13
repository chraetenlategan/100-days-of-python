# LEARN REEBORG'S WORLD JUMPING HURDLES WITH FUNCTIONS Hurdle 1

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump_hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for i in range(1,7):   
    jump_hurdle()

#Hurdle 3

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump_hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
while not at_goal():
    while front_is_clear() and not at_goal:
        move()
    else:
        jump_hurdle()
