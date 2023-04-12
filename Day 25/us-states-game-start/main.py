import pandas as pd
import turtle
screen = turtle.Screen()
screen.title("U.S States Game")
img = "./blank_states_img.gif"
screen.addshape(img)

turtle.shape(img)










states = pd.read_csv('./50_states.csv')

correct = []
all_states = states["state"]

print(all_states)


while len(correct) <50:

    answer_state = screen.textinput(title=f"{len(correct)}/50 States Correct", prompt= "What's another state name?").title()
    filtered = states[states["state"] == answer_state]

    if answer_state == "Exit":
        missed = [item for item in all_states if item not in correct]
        with open('Missed_states', mode = 'w' ) as w:
            w.write(missed)
        break

    if len(states[states["state"] == answer_state])> 0:
        st = turtle.Turtle()
        st.penup()
        st.hideturtle()
        st.setpos(int(filtered.x),int(filtered.y))
        st.write(answer_state)
        
        if answer_state in correct:
            pass
        else:
            correct.append(answer_state)
        if len(correct) == 50:
            print('You win. Ther are all the 50 states of US')






def get_mouse_click_coor(x,y):
    print(x,y)

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()


# screen.exitonclick()