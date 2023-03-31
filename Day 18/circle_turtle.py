import turtle as t

bee = t.Turtle()
bee.speed(799)
for i in range(90):
    bee.pencolor('violet')
    bee.circle(50)
    bee.right(2)
    bee.pencolor('aquamarine')
    bee.circle(50)
    bee.right(2)

screen = t.Screen()

screen.exitonclick()
