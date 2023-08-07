from turtle import Turtle

DIRECTIONS_X = [0.32, -0.32, -0.32, 0.32]
DIRECTIONS_Y = [0.25, -0.25, 0.25, -0.25]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.shapesize(1, 1)
        self.penup()
        self.goto(0, 0)
        self.x_direction = 10
        self.y_direction = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_direction
        new_y = self.ycor() + self.y_direction
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_direction *= -1

    def bounce_x(self):
        self.x_direction *= -1
        self.move_speed *= 0.9

    def restart(self):
        self.move_speed = 0.1
        self.goto(0, 0)
        self.x_direction *= -1
        self.y_direction *= -1
        self.move()
