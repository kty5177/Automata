#-*- coding: utf-8 -*-
##Automata Project
##2015 9.22 Start

from Mealy_machine_simulator import *
from Construct_korean import *

Me1 = Make_korean_mealy_machine()

k = ""
while True :
    print 'Input a character repeatedly, "EXIT" : Exit, ''"!"'' : Backspace, "CLEAR" : New word :  '
    s = raw_input()
    if s == 'EXIT':
        print 'Good Bye!!'
        break
    elif s == 'CLEAR' or s == 'clear' :
        k = ""
    elif s == '!' :
        if len(k) < 3 :
            print "Not Valid Backspace"
        else :
            k = k[:-3]
            print k
            Me1.simulate(k)
    elif len(s) > 3 :
        print 'Input character one by one'
    elif not s in Me1.input_symbols:
        print 'Wrong Input!!!'
    else :
        k = k + s
        t = Me1.simulate(k)
        if not t :
            k = k[:-3]
        print 'Current Input:', k



