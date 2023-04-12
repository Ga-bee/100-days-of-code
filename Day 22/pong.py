from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Score
screen= Screen()
screen.setup(width=800,height=600)
screen.bgcolor('black')

left_paddle = Paddle((-350,0))
right_paddle = Paddle((350,0))
ball = Ball()
score = Score() 

screen.listen()
screen.onkeypress(right_paddle.move_up,"Up")
screen.onkeypress(right_paddle.move_down,"Down")
screen.onkeypress(left_paddle.move_up,"w")
screen.onkeypress(left_paddle.move_down,"s")
# left.multiplayer()

game_is_on = True

l_score = 0
r_score = 0
while game_is_on:
    sleep(ball.move_speed)
    screen.update()
    ball.move()
    

    #Detect collision with the wall
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()
        ball.increase_speed()

    #Detect collision with right paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320 )or (ball.distance(left_paddle) < 50 and ball.xcor() < 320):
        ball.bounce_x()
      
    

    if ball.xcor() <= -390:
        score.left_point()
        ball.move_speed = 0.1
        ball.reset()

    if ball.xcor() >= 390:
        score.right_point()
        ball.move_speed =0.1
        ball.reset()

        
    


# screen.onkey(ball.move, 't')


screen.exitonclick()

