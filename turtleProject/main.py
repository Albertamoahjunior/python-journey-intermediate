from turtle import Turtle, Screen

tim = Turtle()
colors = [0, 0, 0, "red", "blue", "green", "yellow",
          "pink", "gold", "turquoise", "brown", "grey",
          "cyan"]


def draw(sides, colour):
    angle = 180 - (180 * (sides - 2) / sides)
    tim.color(colour)
    for n in range(sides):
        tim.forward(100)
        tim.right(angle)


for n in range(3, 11):
    draw(n, colors[n])

screen = Screen()
screen.mainloop()