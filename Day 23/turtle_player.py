from turtle import Turtle

class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape('turtle')
        self.color('green')
        self.penup()
        self.setpos(0,-280)
        self.setheading(90)

    def move(self):
        self.forward(10)
