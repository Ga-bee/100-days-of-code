from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from time import sleep
screen= Screen()
screen.setup(width=800,height=600)
screen.bgcolor('black')

left = Paddle((-350,0))
right = Paddle((350,0))
ball = Ball()


screen.listen()
screen.onkeypress(right.move_up,"Up")
screen.onkeypress(right.move_down,"Down")
screen.onkeypress(left.move_up,"w")
screen.onkeypress(left.move_down,"s")
# left.multiplayer()
game_is_on = True

while game_is_on:
    sleep(0.1)
    screen.update()
    ball.move()
    if not game_is_on:
        break
    


screen.onkey(ball.move, 't')


screen.exitonclick()