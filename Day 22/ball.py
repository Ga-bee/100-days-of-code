from turtle import Turtle
from random import randint, choice

class Ball(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.create_ball()

    def create_ball(self):
        self.ball = Turtle(shape='circle')
        self.ball.penup()
        self.ball.setpos(0,0)
        self.ball.setheading(45)
        self.ball.color('white')
    
    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.ball.goto(new_x,new_y)
        # self.ball.forward(500)
        
    
    