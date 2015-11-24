20120352 김태연
오토마타 예비 프로젝트 1-2 Mealy Machine 시뮬레이터

작업환경
OS : OS X Yosemitie 10.10
Language : Python 2.7.6
IDE : PyCharm CE

파일 구성/설명
Input directory
- Input_symbols.txt
- Output_symbols.txt
- Set_of_states.txt
- Start_state.txt
- Transition_table.txt
- Output_table.txt

Mealy_machine_simulator.py
run.py
README.txt

Input directory -> Mealy Machine 구성을 위한 Input들을 입력하는 텍스트 파일들 입니다.
Mealy_machine_simulator.py -> Me class가 정의되어 있는 파일입니다.
run.py -> 실제 프로젝트 1-2이 작동되는 파일이며 파일 입출력이 이루어집니다.

실행 방법
Input directory의 파일들에 적절한 input들을 작성한 후 run.py를 python 으로 실행하시면 됩니다.
파일들에 적절한 input이 들어가서 Mealy_Machine 이구성되는 경우, "A Mealy Machine is successfully made!"가 출력되며,
한 단어씩 콘솔창에 입력을 받아 그 String이 이 MealyMachine을 거쳤을때 생성되는 Output String을 출력하게 됩니다.

파일 입력방법
모든 텍스트 파일에 원하는 입력을 한줄씩 띄워서 입력합니다. Transition_table과 Output_table 같은 경우 한 transition안의 character들끼리 한 칸씩 띄워서 입력합니다

제한 조건 (assertion 발생)
Transition_table의 state들이 set_of_state에 없거나, character가 input_symbol에 없는 경우.
Output_table의 state가 set_of_state에 없거나, character가 input_symbol에 없거나, alphabet이 output_symbols에 없는 경우.
Start_state가 set of state에 없는 경우.

모든 input string은 transition_table과 Output_table에 있는 state들로만 구성 되어있다고 가정합니다.

입출력 예시.
Set_of_states.txt
q0
q1
q2
q3
q4
q5

Input_symbols.txt
0
1

Output_symbols.txt
a
b
c
d
e
f
g
h
i
j
k
l

Transition_table.txt
q0 0 q0
q0 1 q1
q1 0 q0
q1 1 q2
q2 0 q3
q2 1 q2
q3 0 q2
q3 1 q4
q4 0 q5
q4 1 q2
q5 0 q3
q5 1 q4

Output_table.txt
q0 0 a
q0 1 b
q1 0 c
q1 1 d
q2 0 e
q2 1 f
q3 0 g
q3 1 h
q4 0 i
q4 1 j
q5 0 k
q5 1 l

Start_state.txt
q0

Console창
/System/Library/Frameworks/Python.framework/Versions/2.7/bin/python2.7 "/Users/ddubby/Desktop/2015 가을학기/CS322 오토마타/Project/Automata/run.py"
##Mealy Machine Simulator##
A Mealy Machine is successfully made!
Input the string or "EXIT" to Exit
001
aab
Input the string or "EXIT" to Exit
110110
bdehje
Input the string or "EXIT" to Exit
0100010
abcaabc
Input the string or "EXIT" to Exit
0110110110
abdehjehje
Input the string or "EXIT" to Exit
110110110101010
bdehjehjehilili
Input the string or "EXIT" to Exit
11110111010100010
bdffehjfehilikgfe
Input the string or "EXIT" to Exit
000000100101000010
aaaaaabcabcbcaaabc
Input the string or "EXIT" to Exit
EXIT
Good Bye!!

Process finished with exit code 0
