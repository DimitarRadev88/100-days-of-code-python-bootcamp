from state import State


class StatesGame:

    def __init__(self, states):
        self.states = states
        self.guessed_states_names = []
        self.not_guessed_states = []

    def exists_state(self, input_state):\
        return len(self.get_state(input_state)) > 0

    def add_state(self, input_state):
        state = self.get_state(input_state)
        self.guessed_states_names.append(input_state.title())
        State(state, "black")

    def add_not_guessed_states(self):
        self.not_guessed_states = self.states[~self.states.state.isin(self.guessed_states_names)]["state"].to_list()

    def get_state(self, input_state):
        return self.states[self.states.state == input_state.title()]

    def count_of_states(self):
        return len(self.states)

    def correctly_guessed_count(self):
        return len(self.guessed_states_names)

    def display_not_guessed_states(self):
        for state_name in self.not_guessed_states:
            state = self.get_state(state_name)
            State(state, "red")
