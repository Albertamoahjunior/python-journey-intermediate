import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()
screen.bgcolor("white")
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    #moving cars
    car.start()

    #detect collision
    for n in range(20):
        if car.cars[n].distance(player) < 15:
            scoreboard.game_over()
            game_is_on = False

    #next level update
    if player.ycor() >= 280:
        player.next_level()
        car.increase_speed()
        scoreboard.update_scoreboard()
        scoreboard.game_over()

screen.mainloop()
