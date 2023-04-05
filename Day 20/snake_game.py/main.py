from turtle import Turtle,Screen
import time
from food import Food
from snake_class import Snake
from scoreboard import Score
screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor('black')
screen.title('My own snake game')
screen.tracer(0)

score = Score()
snake = Snake()
food = Food()
screen.listen()


screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True



while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        if snake.head.distance(food) <= 15:
                food.refresh()
                score.update_score()
                snake.add_new_segments()
                
        if snake.check_head_colision() == False:
                break
        elif snake.check_wall_colision() == False:
                break

print("Congrats! Your score:", score.count)
                

 
screen.exitonclick()