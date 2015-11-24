#-*- coding: utf-8 -*-
##Automata Project
##2015 9.22 Start

from Mealy_machine_simulator import *

##Make a Mealy_machine
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

#Output_symbols
f = open("Input/Output_symbols.txt","r")
line = f.readline()
output_symbols = []
while line:
    s = line.strip()
    output_symbols.append(s)
    line = f.readline()
f.close()


#Transition Table
f = open("Input/Transition_table.txt","r")
line = f.readline()
transition_table = []
while line:
    x = line.split()
    assert (x[0] in state_list and x[2] in state_list and x[1] in input_symbols), "Input error in transition_table "+ x[0]+ " + " + x[1]+ " = " + x[2]
    s = Me.Transition(x[0],x[1],x[2])
    transition_table.append(s)
    line = f.readline()
f.close()

#Output Table
f = open("Input/Output_table.txt","r")
line = f.readline()
output_table = []
while line:
    x = line.split()
    assert (x[0] in state_list and x[2] in output_symbols and x[1] in input_symbols), "Input error in output_table "+ x[0]+ " + " + x[1]+ " = " + x[2]
    s = Me.making_output(x[0],x[1],x[2])
    output_table.append(s)
    line = f.readline()
f.close()



#Start State
f = open("Input/Start_state.txt","r")
line = f.readline()
s = line.strip()
assert (s in state_list), "Input error in start_state : " + s
start_state = s
f.close()

"""
print state_list
print input_symbols
print output_symbols
for i in transition_table:
    print i.curr_state, i.input_character, i.next_state
for i in output_table:
    print i.curr_state, i.input_character, i.output_symbol

print start_state
"""

print '##Mealy Machine Simulator##'
Me1 = Me(state_list, input_symbols, output_symbols, transition_table, output_table, start_state)

print 'A Mealy Machine is successfully made!'

while True :
    print 'Input the string or "EXIT" to Exit'
    s = raw_input()
    if s == 'EXIT':
        print 'Good Bye!!'
        break
    else :
        k =  Me1.simulate(s)
        print k



