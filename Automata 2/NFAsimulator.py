__author__ = 'ddubby'

#-*- coding: utf-8 -*-
class NFA(object):
    class Transition(object):
        def __init__(self, curr_state, input_character, next_state):
            self.curr_state = curr_state
            self.input_character = input_character
            self.next_state = next_state
    def __init__(self, states, input_symbols, transition_table, start_state, final_state):
        self.states = states
        self.input_symbols = input_symbols
        self.transition_table = transition_table
        self.start_state = start_state
        self.final_state = final_state

    def transit(self, state, symbol):
        next_state_list = []
        for t in self.transition_table:
            if t.curr_state == state  and t.input_character == symbol:
                next_state_list.append(t.next_state)
        return next_state_list

