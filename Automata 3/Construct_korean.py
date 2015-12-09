#-*- coding: utf-8 -*-
__author__ = 'ddubby'
from Mealy_machine_simulator import *
def Make_korean_mealy_machine():
##Make a Korean_accepted_Mealy_machine
    c = ['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
    o = ['ㅗ']
    u = ['ㅜ']
    a = ['ㅏ','ㅑ','ㅓ','ㅕ','ㅡ']
    i = ['ㅛ','ㅠ','ㅣ','ㅐ','ㅔ','ㅖ','ㅒ']

    oti = ['ㅣ','ㅐ']
    ota = ['ㅏ']
    uti = ['ㅣ','ㅔ']
    uta = ['ㅓ']
    ati = ['ㅣ']

    k = ['ㄱ','ㅂ']
    n = ['ㄴ']
    r = ['ㄹ']
    l = ['ㄷ','ㅁ','ㅅ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ','ㄲ','ㅆ']
    ouaitv = ['ㄸ','ㅃ','ㅉ']

    ktl = ['ㅅ']
    ntl = ['ㅈ','ㅎ']
    rtl = ['ㄱ','ㅁ','ㅂ','ㅅ','ㅌ','ㅍ','ㅎ']

    ktv = [x for x in c if not c in ktl]
    ntv = [x for x in c if not c in ntl]
    rtv = [x for x in c if not c in rtl]

    state_list = ['S','V','O','U','A','I','K','N','R','L']
    input_symbols = c + o + u + a + i
    transition_table = []
    for s in c : transition_table.append(Me.Transition('S',s,'V'))
    for s in o :
        transition_table.append(Me.Transition('V',s,'O'))
        transition_table.append(Me.Transition('K',s,'O'))
        transition_table.append(Me.Transition('N',s,'O'))
        transition_table.append(Me.Transition('R',s,'O'))
        transition_table.append(Me.Transition('L',s,'O'))
    for s in u :
        transition_table.append(Me.Transition('V',s,'U'))
        transition_table.append(Me.Transition('K',s,'U'))
        transition_table.append(Me.Transition('N',s,'U'))
        transition_table.append(Me.Transition('R',s,'U'))
        transition_table.append(Me.Transition('L',s,'U'))
    for s in a :
        transition_table.append(Me.Transition('V',s,'A'))
        transition_table.append(Me.Transition('K',s,'A'))
        transition_table.append(Me.Transition('N',s,'A'))
        transition_table.append(Me.Transition('R',s,'A'))
        transition_table.append(Me.Transition('L',s,'A'))
    for s in i :
        transition_table.append(Me.Transition('V',s,'I'))
        transition_table.append(Me.Transition('K',s,'I'))
        transition_table.append(Me.Transition('N',s,'I'))
        transition_table.append(Me.Transition('R',s,'I'))
        transition_table.append(Me.Transition('L',s,'I'))
    for s in oti : transition_table.append(Me.Transition('O',s,'I'))
    for s in ota : transition_table.append(Me.Transition('O',s,'A'))
    for s in uti : transition_table.append(Me.Transition('U',s,'I'))
    for s in uta : transition_table.append(Me.Transition('U',s,'A'))
    for s in ati : transition_table.append(Me.Transition('A',s,'I'))
    for s in k :
        transition_table.append(Me.Transition('O',s,'K'))
        transition_table.append(Me.Transition('U',s,'K'))
        transition_table.append(Me.Transition('A',s,'K'))
        transition_table.append(Me.Transition('I',s,'K'))
    for s in n :
        transition_table.append(Me.Transition('O',s,'N'))
        transition_table.append(Me.Transition('U',s,'N'))
        transition_table.append(Me.Transition('A',s,'N'))
        transition_table.append(Me.Transition('I',s,'N'))
    for s in r :
        transition_table.append(Me.Transition('O',s,'R'))
        transition_table.append(Me.Transition('U',s,'R'))
        transition_table.append(Me.Transition('A',s,'R'))
        transition_table.append(Me.Transition('I',s,'R'))
    for s in l :
        transition_table.append(Me.Transition('O',s,'L'))
        transition_table.append(Me.Transition('U',s,'L'))
        transition_table.append(Me.Transition('A',s,'L'))
        transition_table.append(Me.Transition('I',s,'L'))
    for s in ouaitv :
        transition_table.append(Me.Transition('O',s,'V'))
        transition_table.append(Me.Transition('U',s,'V'))
        transition_table.append(Me.Transition('A',s,'V'))
        transition_table.append(Me.Transition('I',s,'V'))
    for s in ktl : transition_table.append(Me.Transition('K',s,'L'))
    for s in ntl : transition_table.append(Me.Transition('N',s,'L'))
    for s in rtl : transition_table.append(Me.Transition('R',s,'L'))
    for s in ktv : transition_table.append(Me.Transition('K',s,'V'))
    for s in ntv : transition_table.append(Me.Transition('N',s,'V'))
    for s in rtv : transition_table.append(Me.Transition('R',s,'V'))
    for s in c : transition_table.append(Me.Transition('L',s,'V'))

# construct output_table
    output_table = []
    for s in c : output_table.append(Me.making_output('S',s,s_to_v))
    for s in o+u+a+i : output_table.append(Me.making_output('V',s,v_to_ouai))
    for s in oti : output_table.append(Me.making_output('O',s,oua_to_ai))
    for s in uti : output_table.append(Me.making_output('U',s,oua_to_ai))
    for s in ati : output_table.append(Me.making_output('A',s,oua_to_ai))
    for s in ota : output_table.append(Me.making_output('O',s,oua_to_ai))
    for s in uta : output_table.append(Me.making_output('U',s,oua_to_ai))
    for s in k+n+r+l :
        output_table.append(Me.making_output('O',s,ouai_to_knrl))
        output_table.append(Me.making_output('U',s,ouai_to_knrl))
        output_table.append(Me.making_output('A',s,ouai_to_knrl))
        output_table.append(Me.making_output('I',s,ouai_to_knrl))
    for s in ouaitv :
        output_table.append(Me.making_output('O',s,ouai_to_v))
        output_table.append(Me.making_output('U',s,ouai_to_v))
        output_table.append(Me.making_output('A',s,ouai_to_v))
        output_table.append(Me.making_output('I',s,ouai_to_v))
    for s in o+u+a+i :
        output_table.append(Me.making_output('K',s,knrl_to_ouai))
        output_table.append(Me.making_output('N',s,knrl_to_ouai))
        output_table.append(Me.making_output('R',s,knrl_to_ouai))
        output_table.append(Me.making_output('L',s,knrl_to_ouai))

    for s in ktl : output_table.append(Me.making_output('K',s,knr_to_l))
    for s in ntl : output_table.append(Me.making_output('N',s,knr_to_l))
    for s in rtl : output_table.append(Me.making_output('R',s,knr_to_l))

    for s in ktv : output_table.append(Me.making_output('K',s,knrl_to_v))
    for s in ntv : output_table.append(Me.making_output('N',s,knrl_to_v))
    for s in rtv : output_table.append(Me.making_output('R',s,knrl_to_v))
    for s in c : output_table.append(Me.making_output('L',s,knrl_to_v))

    start_state = 'S'

    """
    print state_list
    print input_symbols
    for i in transition_table:
        print i.curr_state, i.input_character, i.next_state
    for i in output_table:
        print i.curr_state, i.input_character, i.output_function

    print start_state
    """

    print '##한글모아쓰기 오토마타##'
    Me1 = Me(state_list, input_symbols, transition_table, output_table, start_state)
    return Me1