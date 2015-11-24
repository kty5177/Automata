#-*- coding: utf-8 -*-
##Automata Project
##2015 9.22 Start

from DFAsimulator import *

##Make a DFA
#Set of States
f = open("Input/Set_of_states.txt","r")
line = f.readline()
state_list = []
while line:
    s = line.strip()
    state_list.append(s)
    line = f.readline()
f.close()

#Input Symbols
f = open("Input/Input_symbols.txt","r")
line = f.readline()
input_symbols = []
while line:
    s = line.strip()
    input_symbols.append(s)
    line = f.readline()
f.close()

#Transition Table
f = open("Input/Transition_table.txt","r")
line = f.readline()
transition_table = []
while line:
    x = line.split()
    assert (x[0] in state_list and x[2] in state_list and x[1] in input_symbols), "Input error in transition_table "+ x[0]+ " + " + x[1]+ " = " + x[2]
    s = DFA.Transition(x[0],x[1],x[2])
    transition_table.append(s)
    line = f.readline()
f.close()

#Start State
f = open("Input/Start_state.txt","r")
line = f.readline()
s = line.strip()
assert (s in state_list), "Input error in start_state : " + s
start_state = s
f.close()

#Final State
f = open("Input/Final_state.txt","r")
line = f.readline()
final_states = []
while line:
    s = line.strip()
    assert (s in state_list), "Input error in final_state : " + s
    final_states.append(s)
    line = f.readline()
f.close()

print '##DFA Simulator##'
DFA1 = DFA(state_list, input_symbols, transition_table, start_state, final_states)

print 'A DFA is successfully made!'
while True :
    print 'Input the string or "EXIT" to Exit'
    s = raw_input()
    if s == 'EXIT':
        print 'Good Bye!!'
        break
    else :
        if DFA1.simulate(s):
            print "네"
        else :
            print "아니오"




