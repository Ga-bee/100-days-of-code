from turtle import Turtle
from random import randint, choice
MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
COLORS = ['purple','blue','green' ,'yellow','orange','red']

class Cars():
    def __init__(self) -> None:
        self.allcars = []
        
        
    def create_car(self):
        dice = randint(1,7)
        if dice == 1:
            speed = randint(1,5)
            car = Turtle('square')
            car.hideturtle()
            car.penup()
            car.color(choice(COLORS))
            car.shapesize(stretch_len=2,stretch_wid=0.8)
            car.goto(350,randint(-250,250))
            car.speed(speed)
            car.showturtle()
            self.allcars.append(car)

    def move(self):
        for car in self.allcars:
            car.backward(MOVE_DISTANCE)
        
