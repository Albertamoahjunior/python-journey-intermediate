from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right = (-350, 0)
left = (350, 0)
right_paddle = Paddle(right)
left_paddle = Paddle(left)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=left_paddle.move_up, key="Up")
screen.onkey(fun=left_paddle.move_down, key="Down")
screen.onkey(fun=right_paddle.move_up, key="w")
screen.onkey(fun=right_paddle.move_down, key="s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    #collision with wall and bounce
    if ball.ycor() <= -280 or ball.ycor() > 280:
        ball.bounce_y()
    else:
        pass

    #collision with paddle
    if ball.distance(left_paddle) < 50 and ball.xcor() > 325 or ball.distance(right_paddle) < 50 and ball.xcor() < -325:
        ball.bounce_x()

    #detect off bounds
    if ball.distance(left_paddle) > 50 and ball.xcor() > 390:
        scoreboard.l_score += 1
        scoreboard.update_scoreboard()
        ball.restart()
    elif ball.distance(right_paddle) > 50 and ball.xcor() < -390:
        scoreboard.r_score += 1
        scoreboard.update_scoreboard()
        ball.restart()
screen.mainloop()
