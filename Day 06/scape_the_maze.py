def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if front_is_clear():
        while front_is_clear():
            move()
        if not front_is_clear():
            while not front_is_clear():
                if right_is_clear():
                    turn_right()
                else:
                    turn_left()
    elif not front_is_clear():
        if right_is_clear():
            turn_right()
            move()
        else:
            turn_left()  
    if at_goal():
        break