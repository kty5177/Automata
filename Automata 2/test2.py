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


tokens = (
    'CHAR',
    'ADD',
    'STAR',
    'LPAREN',
    'RPAREN'
)

t_CHAR = r'[a-zA-Z0-9_]'
t_ADD = r'\+'
t_STAR = r'\*'
t_LPAREN = r'\('
t_RPAREN = r'\)'


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
(a+b)*abc
'''
# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)

"""
while True:
    s = raw_input(">>")
    if not (s or s == "exit"):
        break
    else :
        lexer.input(s)
        while True:
            tok = lexer.token()
            if not tok:
                break
            print(tok)
"""
