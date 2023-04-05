from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position) -> None:
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        self.paddle = Turtle(shape='square')
        self.paddle.setheading(90)
        self.paddle.shapesize(stretch_len=5)
        self.paddle.penup()
        self.paddle.setpos(position)
        self.paddle.color('white')

    def move_up(self):
        self.paddle.forward(10)
        

    def move_down(self):
        self.paddle.backward(10)

    def single_player(self):
        pass
        
