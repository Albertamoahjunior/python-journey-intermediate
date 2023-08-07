import turtle
from turtle import Turtle,Screen
from random import Random

turtle.colormode(255)
choose = Random()
tim = Turtle()
tim.speed(30)


def random_colors():
    r = choose.randint(0,255)
    g = choose.randint(0, 255)
    b = choose.randint(0, 255)
    random_color = (r, g, b)
    return random_color


for n in range(0, 50):
    tim.color(random_colors())
    tim.circle(100)
    tim.left(10)

screen = Screen()
screen.exitonclick()
