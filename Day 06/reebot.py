def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_right()
    move()
    turn_right()
    move()
       
while at_goal() == False:
    while front_is_clear():
        move()
    if wall_in_front():
        turn_left()
        while not right_is_clear():
            if not front_is_clear():
                turn_left()
            if wall_in_front():
                turn_left()
            if front_is_clear:
                move()
            if at_goal():
                break
            
            elif not front_is_clear:
                turn_left()
            if right_is_clear():
                jump()