from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("dark green")
screen.title("My Snake Game")
screen.tracer(0)

food = Food()
snake = Snake()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.turn_left, key="Left")
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.turn_right, key="Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.update_score()
        snake.extend_snake()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        #is_game_on = False
        scoreboard.reset()
        snake.reset()

    # detect collision with tail
    for segement in snake.segements[1:]:
       # if segement == snake.head:
        #    pass
        if segement.distance(snake.head) < 10 :
            #is_game_on = False
            scoreboard.reset()
            snake.reset()





screen.mainloop()
