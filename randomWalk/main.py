from turtle import Turtle, Screen
from random import Random

choose = Random()

tim = Turtle()
tim.speed(18)
tim.pensize(5)
colors = ["red", "blue", "green", "yellow", "pink", "gold", "turquoise", "brown", "grey", "cyan"]
directions = [90, 180, 270, 360]

for n in range(1, 200):
    tim.color(choose.choice(colors))
    tim.forward(15)
    tim.right(choose.choice(directions))


screen = Screen()
screen.exitonclick()