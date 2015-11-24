20120352 김태연
오토마타 예비 프로젝트 1-1 DFA 시뮬레이터

작업환경
OS : OS X Yosemitie 10.10
Language : Python 2.7.6
IDE : PyCharm CE

파일 구성/설명
Input directory
- Final_state.txt
- Input_symbols.txt
- Set_of_states.txt
- Start_state.txt
- Transition_table.txt

DFAsimulator.py
run.py
README.txt

Input directory -> DFA 구성을 위한 Input들을 입력하는 텍스트 파일들 입니다.
DFAsimulator.py -> DFA class가 정의되어 있는 파일입니다.
run.py -> 실제 프로젝트 1-1이 작동되는 파일이며 파일 입출력이 이루어집니다.

실행 방법
Input directory의 파일들에 적절한 input들을 작성한 후 run.py를 python 으로 실행하시면 됩니다.
파일들에 적절한 input이 들어가서 DFA가 구성되는 경우, "A DFA is successfully made!"가 출력되며,
한 단어씩 콘솔창에 입력을 받아 그 String이 이 DFA를 만족하는지 검사합니다. 만족하는경우 콘솔창에 "네", 만족하지 않는 경우 "아니오"가 뜨며,
EXIT을 입력하는 경우 프로그램이 종료됩니다.

파일 입력방법
모든 텍스트 파일에 원하는 입력을 한줄씩 띄워서 입력합니다. Transition_table같은 경우 한 transition안의 character들끼리 한 칸씩 띄워서 입력합니다

제한 조건 (assertion 발생)
Transition_table의 state들이 set_of_state에 없거나, character가 input_symbol에 없는 경우.
Start_state가 set of state에 없는 경우.
Final_state가 set of state에 없는 경우.

입출력 예시.
Set_of_states.txt
q0
q1
q2
q3
q4
q5
q6
Input_symbols.txt
0
1
2
Transition_table.txt
q0 0 q1
q0 1 q2
q0 2 q3
q1 0 q1
q1 1 q2
q1 2 q3
q2 0 q4
q2 1 q4
q2 2 q4
q3 0 q5
q3 1 q5
q3 2 q5
q4 0 q5
q4 1 q5
q4 2 q5
q5 0 q6
q5 1 q6
q5 2 q6
q6 0 q6
q6 1 q6
q6 2 q6
Start_state.txt
q0
Final_states.txt
q1
q2
q3
q4
q5
Console창
/System/Library/Frameworks/Python.framework/Versions/2.7/bin/python2.7 /Users/ddubby/PycharmProjects/Automata/run.py
##DFA Simulator##
A DFA is successfully made!
Input the string or "EXIT" to Exit
123
아니오
Input the string or "EXIT" to Exit
121
네
Input the string or "EXIT" to Exit
100
네
Input the string or "EXIT" to Exit
000010
네
Input the string or "EXIT" to Exit
211
아니오
Input the string or "EXIT" to Exit
21
네
Input the string or "EXIT" to Exit
0021
네
Input the string or "EXIT" to Exit
00001
네
Input the string or "EXIT" to Exit
1
네
Input the string or "EXIT" to Exit
0
네
Input the string or "EXIT" to Exit
021
네
Input the string or "EXIT" to Exit
EXIT
Good Bye!!

Process finished with exit code 0