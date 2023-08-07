'''
from turtle import Turtle, Screen

jimmy = Turtle()
print(jimmy)
jimmy.color("red")
jimmy.shape("turtlSe")
jimmy.forward(200)
my_screen = Screen()
my_screen.canvheight = 300
my_screen.canvwidth = 300
my_screen.mainloop()
'''
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["pikachu", "turtle", "Douglas"])
table.add_column("Pokemon Type", ["electric", "water", "earth"])
print(table)