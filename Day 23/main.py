from turtle import  Turtle, Screen
from turtle_player import Player
from scoreboard import Score
from cars import Cars
import time

turtle = Player()
screen = Screen()
score = Score()
car = Cars()

screen.setup(600,600)
screen.tracer(0)
screen.title("Turtle crossing")
screen.listen()

screen.onkeypress(turtle.move,'Up')

game_is_on = True
scoreboard = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()

    for cars in car.allcars:
        if cars.distance(turtle) < 20:
            score = Turtle()
            score.hideturtle()
            score.write(arg='GAME OVER',font=('Comic Sans',24,'bold'))
            score.setpos(-100,-50)
            game_is_on = False

    #when turtle hits the top edge
    if turtle.ycor() >= 280:
    #clear screen and next level and increase score
        turtle.setpos(0,-280)
        scoreboard += 1
        score.increase_score(scoreboard)




screen.exitonclick()