from turtle import Turtle, Screen
from random import Random

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="make your bet", prompt="Which turtle will win the race? Choose a color: ")
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
y_position = [-60, -30, -0, 30, 60, 90]
all_turtles = []
for color in range(0, 6):
    tim = Turtle("turtle")
    tim.speed(1)
    tim.color(colors[color])
    tim.penup()
    tim.goto(x=-230, y=y_position[color])
    all_turtles.append(tim)
if user_bet:
     is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() == 250:
            is_race_on = False
            if turtle.pencolor() == user_bet:
                print(f"The color is {turtle.pencolor()} you won")
            else:
                print(f"The color is {turtle.pencolor()} you loose")

        random_distance = Random().randint(0, 10)
        turtle.forward(random_distance)

screen.mainloop()
