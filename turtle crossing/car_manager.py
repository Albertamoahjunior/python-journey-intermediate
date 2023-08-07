from turtle import Turtle
from random import randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed = STARTING_MOVE_DISTANCE
        self.cars = []
        self.create_cars()
        self.has_crashed = False

    def start(self):
        self.move()

    def increase_speed(self):
        self.speed += MOVE_INCREMENT

    def create_cars(self):
        for n in range(20):
            random_colors = COLORS[randint(0, 5)]
            random_y = randint(-250, 290)
            random_x = randint(-290, 290)
            new_car = Turtle("square")
            new_car.color(random_colors)
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.speed = STARTING_MOVE_DISTANCE
            new_car.right(180)
            new_car.goto(random_x, random_y)
            self.cars.append(new_car)

    def move(self):
        for n in range(20):
            random_y = randint(-250, 280)
            if self.cars[n].xcor() <= -300:
                self.cars[n].goto(300, random_y)
            self.cars[n].forward(STARTING_MOVE_DISTANCE)





