import turtle

import pandas

from states_game import StatesGame

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data_frame = pandas.read_csv("50_states.csv")

game = StatesGame(states_data_frame)
input_state = screen.textinput(title="Guess The State: ", prompt="What is another state's name?: ").title()

while input_state != "End":
    if not game.guessed_states_names.__contains__(input_state) and game.exists_state(input_state):
        game.add_state(input_state)
    input_state = screen.textinput(title=f"{game.correctly_guessed_count()}/{game.count_of_states()} States Correct",
                                   prompt="What is another state's name?: ").title()

game.add_not_guessed_states()

game.display_not_guessed_states()

state = game.states[~game.states.state.isin(game.guessed_states_names)]["state"].to_csv("states_to_learn.csv")

screen.exitonclick()
