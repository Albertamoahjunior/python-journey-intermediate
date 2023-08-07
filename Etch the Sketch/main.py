from turtle import Turtle, Screen

tim = Turtle()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def anti_clockwise_turn():
    tim.right(10)

def clockwise_turn():
    tim.left(10)

def clear_screen():
    tim.reset()


screen = Screen()
screen.listen()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=anti_clockwise_turn)
screen.onkey(key="d", fun=clockwise_turn)
screen.onkey(key="x", fun= clear_screen)

screen.mainloop()
