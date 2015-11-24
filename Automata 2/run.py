__author__ = 'ddubby'
#-*- coding: utf-8 -*-#
import ply.lex as lex
import ply.yacc as yacc
from sets import Set
from DFAsimulator import *
from NFAsimulator import *

#Automata project 2
#15-11-21 start
#Kim Tae Yeon


class eclosure(object):
    def __init__(self, state_name, set_of_states):
        self.state_name = state_name
        self.set_of_states = set_of_states


class MyLexer(object):
    tokens = (
       'CHAR',
       'PLUS',
       'STAR',
       'LPAREN',
       'RPAREN',
    )

    # Regular expression rules for simple tokens
    t_CHAR = r'[a-zA-Z0-9_]'
    t_PLUS    = r'\+'
    t_STAR   = r'\*'
    t_LPAREN  = r'\('
    t_RPAREN  = r'\)'

    # Define a rule so we can track line numbers
    def t_newline(self,t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # A string containing ignored characters (spaces and tabs)
    t_ignore  = ' \t'

    # Error handling rule
    def t_error(self,t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    # Build the lexer
    def build(self,**kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    # Test it output
    def test(self,data):
        self.lexer.input(data)
        while True:
             tok = self.lexer.token()
             if not tok:
                 break
             print tok

# Build the lexer and try it out
m = MyLexer()

m.build()           # Build the lexer
#m.test("3 + 4")     # Test it
tokens = m.tokens

"""
def p_expr(p):
    '''expr : expr PLUS expr
            | LPAREN expr RPAREN
            | expr STAR
            | expr expr
            | CHAR
    '''
"""

def p_expr_plus(p):
    'expr : expr PLUS expr'
    global state_num,start_state
    p[0] = (state_num+1,state_num+2)
    final_states.append(state_num+2)
    final_states.remove(p[1][1])
    final_states.remove(p[3][1])

    transitiontable.append(DFA.Transition(state_num+1,"eps",p[1][0]))
    transitiontable.append(DFA.Transition(state_num+1,"eps",p[3][0]))
    transitiontable.append(DFA.Transition(p[1][1],"eps",state_num+2))
    transitiontable.append(DFA.Transition(p[3][1],"eps",state_num+2))
    start_state = state_num + 1
    state_num +=2


def p_expr_PAREN(p):
    'expr : LPAREN expr RPAREN'
    p[0] = p[2]

def p_expr_STAR(p):
    'expr : expr STAR'
    global state_num,start_state
    p[0] = (state_num+1,state_num+2)
    final_states.append(state_num+2)
    final_states.remove(p[1][1])

    transitiontable.append(DFA.Transition(state_num+1,"eps",p[1][0]))
    transitiontable.append(DFA.Transition(p[1][1],"eps",p[1][0]))
    transitiontable.append(DFA.Transition(p[1][1],"eps",state_num+2))
    transitiontable.append(DFA.Transition(state_num+1,"eps",state_num+2))
    start_state = state_num + 1
    state_num +=2

def p_expr_mul(p):
    'expr : expr expr'
    global state_num,start_state
    p[0] = (p[1][0],p[2][1])
    final_states.remove(p[1][1])
    transitiontable.append(DFA.Transition(p[1][1],"eps",p[2][0]))
    start_state = p[1][0]

def p_expr_char(p):
    'expr : CHAR'
    global state_num,start_state
    p[0] = (state_num+1,state_num+2)
    final_states.append(state_num+2)
    if p[1] == 'e':
        s = DFA.Transition(state_num+1,"eps",state_num+2)
    else :
        s = DFA.Transition(state_num+1,p[1],state_num+2)
    start_state = state_num+1
    state_num +=2
    transitiontable.append(s)
    if (not p[1] in input_symbols) and p[1] != 'e':
        input_symbols.append(p[1])



statelist = []
input_symbols = []
transitiontable = []
start_state = 0
final_states = []
state_num = 0


def p_error(p):
    print "Syntax error at '%s'" % p.value



yacc.yacc()

inputregular = raw_input("Input the regular expression (e = epsilon) : \n")
t =  yacc.parse(inputregular)

state_list = range(1,state_num+1)

"""
print state_list
print input_symbols
for i in transitiontable:
    print i.curr_state, i.input_character,i.next_state
print start_state
print final_states
print state_num

print t
"""
print '##epsilon-NFA to m-DFA Simulator##'
NFA1 = NFA(state_list, input_symbols, transitiontable, start_state, final_states)

print state_list
print input_symbols
for i in transitiontable:
    print i.curr_state, i.input_character,i.next_state
print start_state
print final_states

print 'A NFA is successfully made!'

#find e-closure-list for each state

e_closure_list =[]
for s in state_list:
    stack_list = []
    check_list = []
    stack_list.append(s)
    check_list.append(s)
    while stack_list != [] :
        k = stack_list.pop()
        for j in transitiontable :
            if j.curr_state == k and j.input_character == "eps" and not (j.next_state in check_list) :
                stack_list.append(j.next_state)
                check_list.append(j.next_state)
    e_closure_list.append(eclosure(s,check_list))

"""
for s in e_closure_list :
    print s.state_name, s.set_of_states
"""
#make dfa

s_l = []
#find inital e-closure
for s in e_closure_list:
    if s.state_name == NFA1.start_state :
        s_l = s.set_of_states
        break


d_input_symbols = input_symbols
d_transition_table = []

d_stack_list = [s_l]
d_check_list = [Set(s_l)]

while d_stack_list != [] :
    initial_set = d_stack_list.pop()
    for symbol in d_input_symbols :
        s_list =[]

        for j in initial_set:
            for k in NFA1.transit(j,symbol):
                if not k in s_list :
                    s_list.append(k)

        eps_list=[]

        for j in s_list:
            j_l = []
            for k in e_closure_list :
                if k.state_name == j :
                    j_l = k.set_of_states
                    break
            for h in j_l :
                if not h in eps_list :
                    eps_list.append(h)

        if not Set(eps_list) in d_check_list :
            d_stack_list.append(eps_list)
            d_check_list.append(Set(eps_list))
        d_transition_table.append(NFA.Transition(d_check_list.index(Set(initial_set)),symbol,d_check_list.index(Set(eps_list)) ))
d_state_list = range(len(d_check_list))
d_final_states = []
d_start_state = 0
for i in final_states :
    for j in d_check_list :
        index = d_check_list.index(j)
        if i in j and not(index in d_final_states):
            d_final_states.append(index)

print "#################  DFA  #################"
print "States : ",d_state_list
print "Vocabulary : ", input_symbols
print "State Transition Functions : "
for i in d_transition_table:
    print "(",i.curr_state,",",i.input_character,") => ",i.next_state
print "Initial State : ",d_start_state
print "Final State : ",d_final_states

print 'A DFA is successfully made!'

DFA1 = DFA(d_state_list,input_symbols,d_transition_table,d_start_state,d_final_states)

#make m-dfa
l = len(d_state_list)
m_table = [[0 for x in range(l)] for y in range(l)]


for i in range(0 ,l-1):
    for j in range(i+1,l):
        if (i in d_final_states and  not j in d_final_states) or (not i in d_final_states and j in d_final_states):
            m_table[i][j] = 2
        else :
            m_table[i][j] = 1


while(True):
    is_change = False
    for i in range(0,l-1):
        for j in range(i+1,l):
            if m_table[i][j] == 1:
                for symbol in input_symbols :
                    ni = DFA1.transit(i,symbol)
                    nj = DFA1.transit(j,symbol)
                    if ni != None and nj != None :
                        if m_table[ni][nj] == 2 or m_table[nj][ni] == 2 :
                            m_table[i][j] = 2
                            is_change = True
    if is_change == False :
        break

s_check_list = [True for x in range(l)]
m_state_list = []
list = []
#m_check_list
for i in range(0,l):
    if s_check_list[i] :
        list = [i]
        for j in range(i+1,l):
            if m_table[i][j] == 1 :
                list.append(j)
                s_check_list[j] = False
        m_state_list.append(list)



md_input_symbols = input_symbols
md_transition_table = []
md_start_state = 0

md_final_states=[]
for j in d_final_states :
    for i in m_state_list :
       index = m_state_list.index(i)
       if j in i and not index in md_final_states:
            md_final_states.append(index)

for i in m_state_list :
    i_index = m_state_list.index(i)
    for symbol in md_input_symbols :
        next_state_list = []
        next_index = None
        for k in i :
            next_state_list.append(DFA1.transit(k,symbol))
        for k in m_state_list :
            check = True
            k_index = m_state_list.index(k)
            for l in next_state_list:
                if l not in k :
                    check = False
            if check == True :
                next_index = k_index

        md_transition_table.append(DFA.Transition(i_index,symbol,next_index))


md_state_list = range(len(m_state_list))
print "################# m-DFA  #################"
print "States : ",md_state_list
print "Vocabulary : ", md_input_symbols
print "State Transition Functions : "
for i in md_transition_table:
    print "(",i.curr_state,",",i.input_character,") => ",i.next_state
print "Initial State : ",md_start_state
print "Final State : ",md_final_states

DFA2 = DFA(d_state_list,input_symbols,d_transition_table,d_start_state,d_final_states)

print "DFA TEST!!!"
print 'REGULAR EXPRESSION : ', inputregular
while True :
    print 'Input the string or "EXIT" to Exit'
    s = raw_input()
    if s == 'EXIT':
        print 'Good Bye!!'
        break
    else :
        if DFA2.simulate(s):
            print "네"
        else :
            print "아니오"


