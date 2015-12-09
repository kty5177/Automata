#-*- coding: utf-8 -*-

class Me(object):
    class Transition(object):
        def __init__(self, curr_state, input_character, next_state):
            self.curr_state = curr_state
            self.input_character = input_character
            self.next_state = next_state

    class making_output(object):
        def __init__(self, curr_state, input_character, output_function):
            self.curr_state = curr_state
            self.input_character = input_character
            self.output_function = output_function

    def __init__(self, states, input_symbols, transition_table, output_table, start_state):
        self.states = states
        self.input_symbols = input_symbols
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
                return t.output_function

    def simulate(self, s):
        len1 = 0
        len2 = 0
        outputstring1 = [['' for _ in range(5)] for _ in range(100)]
        outputstring2 = [['' for _ in range(5)] for _ in range(100)]
        curr_state = self.start_state
        print "받침우선      초성우선"

        for i in range(len(s)/3):
            c = s[i*3:i*3+3]
            h = self.make_output(curr_state, c)

            if h != None:
                k1 , len1 = h(outputstring1,len1,True,c) #받침우선
                k2 , len2 = h(outputstring2,len2,False,c) #초성우선
                print list_to_string(outputstring1,len1), "       ", list_to_string(outputstring2, len2)
            else:
                print "Wrong Input!!"
                return False
            curr_state = self.transit(curr_state,c)

            if curr_state == None :
                print "Wrong Input!!"
                return False
        return True

def s_to_v (string, length, order_boolean, ch):
    length +=1
    string[length][0] = ch
    return string, length
def v_to_ouai (string, length, order_boolean, ch):
    string[length][1] = ch
    return string, length
def oua_to_ai(string, length, order_boolean, ch):
    string[length][2] = ch
    return string, length
def ouai_to_knrl(string, length, order_boolean, ch):
    if order_boolean:
        string[length][3] = ch
    else :
        length += 1
        string[length][0] = ch
    return string, length
def ouai_to_v(string,length,order_boolean,ch):
    length+=1
    string[length][0] = ch
    return string, length
def knr_to_l(string,length,order_boolean,ch):
    if order_boolean:
        string[length][4] = ch
    else :
        string[length-1][3] = string[length][0]
        string[length][0] = ch
    return string,length
def knrl_to_ouai(string,length,order_boolean,ch):
    if order_boolean:
        length +=1
        if string[length-1][4] != '' :
            string[length][0] = string[length-1][4]
            string[length-1][4] = ''
        else :
            string[length][0] = string[length-1][3]
            string[length-1][3] = ''
        string[length][1] = ch
    else :
        string[length][1] = ch
    return string, length
def knrl_to_v(string,length,order_boolean,ch):
    if order_boolean:
        length+=1
        string[length][0] = ch
    else :
        if string[length-1][3] == '':
            string[length-1][3] = string[length][0]
        else :
            string[length-1][4] = string[length][0]
        string[length][0] = ch
    return string, length

def list_to_string(string,length):
    ini = ['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
    medi = ['ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅗㅏ','ㅗㅐ','ㅗㅣ','ㅛ','ㅜ','ㅜㅓ','ㅜㅔ','ㅜㅣ','ㅠ','ㅡ',
            'ㅡㅣ','ㅣ']
    fi= ['','ㄱ','ㄲ','ㄱㅅ','ㄴ','ㄴㅈ','ㄴㅎ','ㄷ','ㄹ','ㄹㄱ','ㄹㅁ','ㄹㅂ','ㄹㅅ','ㄹㅌ','ㄹㅍ','ㄹㅎ','ㅁ','ㅂ','ㅂㅅ',
          'ㅅ','ㅆ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
    s = ""
    for i in range(1 , length+1):
        i_index =  ini.index(string[i][0])
        if string[i][1] == '' :
            s += string[i][0].decode('UTF-8')
        else :
            m_index =  medi.index(string[i][1] + string[i][2])
            f_index =  fi.index(string[i][3]+string[i][4])
            s += unichr(44032 + ((i_index * 21) + m_index) * 28 +  f_index)
    return s
