from turtle import Turtle, Screen

tim = Turtle()
screen =Screen()

def red():
    tim.pencolor('red')

def green():
    tim.pencolor('green')

def move_forwards():

    tim.forward(10)

def move_left():
    tim.left(90)
    tim.forward(10)

def move_right():
    tim.right(90)
    tim.forward(10)
screen.listen()
screen.onkey(key='space',fun=move_forwards)
screen.onkey(key='a',fun=move_left)
screen.onkey(key='d',fun=move_right)
screen.onkey(key='r',fun=red)
screen.onkey(key='g',fun=green)
screen.exitonclick()