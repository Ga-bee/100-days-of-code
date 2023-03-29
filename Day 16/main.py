# from turtle import Turtle, Screen
# import prettytable
# tinny = Turtle()
# tinny.shape("turtle")
# tinny.color("cyan")


# print(tinny)
# my_screen = Screen()
# print(my_screen.canvheight)
# tinny.forward(100)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon name", ["Pikachu","Squirtle","charmander"])

print(table)


