from turtle import Turtle
STARTING_POSITIONS = [(-350, 0), (350, 0)]


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.create_paddle()

    def create_paddle(self):
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(4, 1)
        self.goto(self.position)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
