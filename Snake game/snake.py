from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.segements = []
        self.head = ()
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segement(position)

    def add_segement(self, position):
        new_segement = Turtle("square")
        new_segement.color("white")
        new_segement.penup()
        new_segement.goto(position)
        self.segements.append(new_segement)

    def extend_snake(self):
        self.add_segement(self.segements[-1].position())

    def move(self):
        for seg_num in range(len(self.segements)-1, 0, -1):
            new_x = self.segements[seg_num - 1].xcor()
            new_y = self.segements[seg_num - 1].ycor()
            self.segements[seg_num].goto(new_x, new_y)

        self.head = self.segements[0]
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for seg in self.segements:
            seg.goto(1000, 1000)
        self.segements.clear()
        self.create_snake()
        self.head = self.segements[0]

    def turn_left(self):
        self.head.setheading(-180)

    def turn_right(self):
        self.head.setheading(360)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)
