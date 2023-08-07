import turtle
from turtle import Turtle, Screen
from random import Random
turtle.colormode(255)

tim = Turtle()
choose = Random()
rgb_list = [(249, 245, 233), (244, 246, 251), (252, 244, 249), (242, 251, 247), (185, 154, 128), (133, 86, 68), (46, 25, 17), (20, 22, 47), (141, 161, 190), (225, 218, 123)]

tim.speed(10)
tim.penup()
tim.setx(-150)


for n in range(10):
    for n in range(10):
        tim.pendown()
        tim.dot(15, choose.choice(rgb_list))
        tim.penup()
        tim.forward(25)
    tim.penup()
    tim.backward(250)
    tim.right(270)
    tim.forward(20)
    tim.right(90)





screen = Screen()
screen.mainloop()







