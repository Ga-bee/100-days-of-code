import turtle as t
from  random import randint,choice
bee = t.Turtle()
t.colormode(255)

positions = ['f','l', 'r']

colors = ['thistle', 'plum', 'orchid','medium orchid', 'dark orchid','dark violet', 'blue violet','yellow','green','gold', 'dark green', 'blue', 'magenta', 'black','cyan','brown','pink','red','orange','gold','silver', 'aquamarine', 'green','lime green','spring green','navy', 'medium spring green', 'royal blue' ]


for i in range(2000):
    bee.pensize(i/8)
    bee.speed(randint(3,789))
    color_tuple =(randint(0,255),randint(0,255),randint(0,255))
    bee.color(color_tuple)
    position = choice(positions)
    if position == 'f':
        bee.forward(50)
    elif position == 'l':
        bee.left(90)
        bee.forward(50)
    elif position == 'r':
        bee.right(90)
        bee.forward(50)


# for i in range(20):
#     bee.pensize(i)
#     bee.forward(20)
#     bee.left(90)



screen = t.Screen()

screen.exitonclick()