from turtle import Turtle, Screen
from turtle_race_append import *
from random import randint

screen = Screen()
screen.setup(width=500,height=400)

colors = ['purple','blue','green' ,'yellow','orange','red' ]
list_of_turtles =[]

def turtles():
    pos_y = 90
    for turtle in range(0,6):
        new_turtle = Turtle(shape='turtle')
        new_turtle.penup()
        new_turtle.color(colors[turtle])
        new_turtle.goto(x=-230,y=pos_y)
        pos_y -= 30
        list_of_turtles.append(new_turtle)


turtles()

bet = screen.textinput(title="Make your bet",prompt="Wich turtle will win the race?")



def walk():
    while True:
        for turtle in list_of_turtles:
            
            turtle.speed(randint(10,40))
            turtle.forward(randint(0,10))
            if turtle.xcor()>=230:
                winner = turtle.pencolor()
                return winner
                



winner = walk()

print(f"The winner was {winner}", end = ' ')
if bet == winner:
    print('You win')

else:
    print('You loose')

screen.exitonclick()