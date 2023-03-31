from turtle import Turtle, Screen

bee = Turtle()

# for i in range(4):
#     bee.forward(100)
#     bee.left()

# for i in range(15):
#     bee.pendown()
#     bee.forward(10)
#     bee.penup()
#     bee.forward(10)
# colors = ['cyan','thistle','forest green','lime','purple','violet','medium purple','rebecca purple','gold']
colors = ['thistle', 'plum', 'orchid','medium orchid', 'dark orchid','dark violet', 'blue violet']
bee.shape("turtle")
bee.color("forest green")

def draw(num_sides):
    degree = 360/num_sides
    for i in range(num_sides):
        bee.forward(100)
        bee.left(degree)

# for i in range(3):
#     bee.forward(100)
#     bee.left(360/3)

# for i in range(4):
#     bee.forward(100)
#     bee.left(360/4)

# for i in range(5):
#     bee.forward(100)
#     bee.left(360/5)

# for i in range(6):
#     bee.forward(100)
#     bee.left(360/6)

# for i in range(7):
#     bee.forward(100)
#     bee.left(360/7)

# for i in range(8):
#     bee.forward(100)
#     bee.left(360/8)

# for i in range(9):
#     bee.forward(100)
#     bee.left(360/9)

# for i in range(10):
#     bee.forward(100)
#     bee.left(360/10)

for c in range (3,11):
    bee.pencolor(colors[c-3])
    draw(c)
screen = Screen()

screen.exitonclick()
