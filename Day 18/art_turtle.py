import turtle as t
import random as r 

t.colormode(255)
bee = t.Turtle()
bee.pensize(20)
bee.penup()
bee.speed(600)
color_tuple = [r.randint(0,255),r.randint(0,255),r.randint(0,255)]

bee.setposition(-500.00,-300.00)

def coloring():
    bee.pencolor(r.randint(0,255),r.randint(0,255),r.randint(0,255))
    bee.pendown()
    bee.forward(1)
    bee.penup()
    bee.forward(40)
    

def forward():
    for i in range(25):
        coloring()

def up_left():
    bee.pendown()
    bee.forward(1)
    bee.left(90)
    bee.penup()
    bee.forward(40)
    bee.left(90)

def up_right():
    bee.pendown()
    bee.forward(1)
    bee.right(90)
    bee.penup()
    bee.forward(40)
    bee.right(90) 

count_up = 0

while count_up < 15:
    forward()
    up_left()
    count_up += 1
    forward()
    up_right()
    count_up += 1
    if count_up == 15:
        break


screen = t.Screen()
screen.exitonclick()