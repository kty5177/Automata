20120352 김태연
오토마타  본프로젝트 2 정규식이 나타내는 언어를 받아들이는 m-dfa만들기

작업환경
OS : OS X Yosemitie 10.10
Language : Python 2.7.6
IDE : PyCharm CE

파일 구성/설명

DFAsimulator.py
NFAsimulator.py
run.py
README.txt


DFAsimulator.py -> 1-1에서 작성한 파일로 DFA class가 정의되어 있는 파일입니다, 나중에 DFA가 제대로 구성되어있는지 테스트하기 위하여 쓰입니다.
run.py -> 실제 프로젝트 2가 작동되는 파일이며 파일 입출력이 이루어집니다.
NFAsimulator.py -> NFA class가 정의 되어있는 파일이며 DFAclass와 유사합니다.


실행 방법
Input directory의 파일들에 적절한 input들을 작성한 후 run.py를 python 으로 실행하시면 됩니다.
파일들에 적절한 NFA에 관한 정보가 입력되면 이와 equivalent한 DFA와 m-DFA를 즉시 출력하여 보여준후 m-DFA를 기준으로 언어를 받기 시작합니다.
한 단어씩 콘솔창에 입력을 받아 그 String이 이 DFA를 만족하는지 검사합니다. 만족하는경우 콘솔창에 "네", 만족하지 않는 경우 "아니오"가 뜨며,
EXIT을 입력하는 경우 프로그램이 종료됩니다.

파일 입력방법
모든 텍스트 파일에 원하는 입력을 한줄씩 띄워서 입력합니다. Transition_table같은 경우 한 transition안의 character들끼리 한 칸씩 띄워서 입력합니다
입실론 기호는 "eps"로 입력합니다.

제한 조건 (assertion 발생)
Transition_table의 state들이 set_of_state에 없거나, character가 input_symbol에 없는 경우.
Start_state가 set of state에 없는 경우.
Final_state가 set of state에 없는 경우.
Input_symbols에 eps가 들어 있는 경우

입출력 예시.
Set_of_states.txt
0
1
2
3
4
5
6
7
8
9
10
Input_symbols.txt
a
b
Transition_table.txt
0 eps 1
0 eps 7
1 eps 2
1 eps 4
2 a 3
3 eps 6
4 b 5
5 eps 6
6 eps 1
6 eps 7
7 a 8
8 b 9
9 b 10
Start_state.txt
0
Final_states.txt
10
Console창
/System/Library/Frameworks/Python.framework/Versions/2.7/bin/python2.7 "/Users/ddubby/Desktop/2015 가을학기/CS322 오토마타/Project/Automata 2-1/run.py"
##epsilon-NFA to m-DFA Simulator##
#################  DFA  #################
States :  [0, 1, 2, 3, 4]
Vocabulary :  ['a', 'b']
State Transition Functions :
( 0 , a ) =>  1
( 0 , b ) =>  2
( 2 , a ) =>  1
( 2 , b ) =>  2
( 1 , a ) =>  1
( 1 , b ) =>  3
( 3 , a ) =>  1
( 3 , b ) =>  4
( 4 , a ) =>  1
( 4 , b ) =>  2
Initial State :  0
Final State :  [4]
A DFA is successfully made!
################# m-DFA  #################
States :  [0, 1, 2, 3]
Vocabulary :  ['a', 'b']
State Transition Functions :
( 0 , a ) =>  1
( 0 , b ) =>  0
( 1 , a ) =>  1
( 1 , b ) =>  2
( 2 , a ) =>  1
( 2 , b ) =>  3
( 3 , a ) =>  1
( 3 , b ) =>  0
Initial State :  0
Final State :  [3]
DFA TEST!!!
Input the string or "EXIT" to Exit
aa
아니오
Input the string or "EXIT" to Exit
ab
아니오
Input the string or "EXIT" to Exit
abb
네
Input the string or "EXIT" to Exit
bab
아니오
Input the string or "EXIT" to Exit
aaab
아니오
Input the string or "EXIT" to Exit
aabbaa
아니오
Input the string or "EXIT" to Exit
aabbbaab
아니오
Input the string or "EXIT" to Exit
abbaabbbabb
네
Input the string or "EXIT" to Exit
aaababaaabbb
아니오
Input the string or "EXIT" to Exit
