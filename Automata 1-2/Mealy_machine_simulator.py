__author__ = 'ddubby'

#-*- coding: utf-8 -*-
class Me(object):
    class Transition(object):
        def __init__(self, curr_state, input_character, next_state):
            self.curr_state = curr_state
            self.input_character = input_character
            self.next_state = next_state

    class making_output(object):
        def __init__(self, curr_state, input_character, output_symbol):
            self.curr_state = curr_state
            self.input_character = input_character
            self.output_symbol = output_symbol

    def __init__(self, states, input_symbols, output_symbols, transition_table, output_table, start_state):
        self.states = states
        self.input_symbols = input_symbols
        self.output_symbols =  output_symbols
        self.transition_table = transition_table
        self.output_table = output_table
        self.start_state = start_state

    def transit(self, state, symbol):
        for t in self.transition_table:
            if t.curr_state == state  and t.input_character == symbol:
                return t.next_state

    def make_output(self, state, symbol):
        for t in self.output_table:
            if t.curr_state == state  and t.input_character == symbol:
                return t.output_symbol

    def simulate(self, word):
        check_state = self.start_state
        k = ""
        for c in word:
            h = self.make_output(check_state, c)
            if h != None:
                k = k + h
            check_state = self.transit(check_state,c)
        return k

