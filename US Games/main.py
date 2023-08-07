from turtle import Turtle, Screen
import pandas

states_data = pandas.read_csv("50_states.csv")
state_names = states_data.state
state_names = state_names.to_list()
state_locations = []
correct_states = []
states_to_learn = []
count = 0
for state in state_names:
    pos_x = int(states_data[states_data.state == state].x)
    pos_y = int(states_data[states_data.state == state].y)
    place = (pos_x, pos_y)
    state_locations.append(place)

game_is_on = True
locator = Turtle()
locator.hideturtle()
screen = Screen()
screen.title("Name Of States")
screen.setup(800, 600)
screen.bgpic("blank_states_img.gif")
while game_is_on:
    input_state = screen.textinput(f"{count}/{len(state_names)} guesses correct", "What is the name of another state")

    for state in state_names:
        if state == input_state:
            locator.penup()
            locator.goto(state_locations[state_names.index(input_state)])
            locator.write(input_state, align="center", font=("courier", 9, "normal"))
            correct_states.append(input_state)
            count += 1

    if input_state == "exit" or count > len(state_names):
        game_is_on = False
for incorrect in state_names:
    if incorrect not in correct_states:
        states_to_learn.append(incorrect)

unlearnt_dict = {
    "states": states_to_learn
}
unlearnt_data = pandas.DataFrame(unlearnt_dict)

unlearnt_data.to_csv("States to learn.csv")
