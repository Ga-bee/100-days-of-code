from turtle import Turtle
from random import randint, choice

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()

        self.move_speed = 0.1
        
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
        
            
            
    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
    
    def reset(self):                 
        self.hideturtle()
        self.goto(0,0)
        self.showturtle()
        self.x_move*= -1

    def increase_speed(self):
        self.move_speed *= 0.9
