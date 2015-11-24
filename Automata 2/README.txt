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


ply directory -> lex.py, yacc.py가 들어있습니다.
DFAsimulator.py -> 1-1에서 작성한 파일로 DFA class가 정의되어 있는 파일입니다, 나중에 DFA가 제대로 구성되어있는지 테스트하기 위하여 쓰입니다.
run.py -> 실제 프로젝트 2가 작동되는 파일이며 파일 입출력이 이루어집니다. lex, yacc을 이용한 부분을 제외하고는 예비프로젝트 2-1 내용을 그대로 인용 하였습니다.
NFAsimulator.py -> NFA class가 정의 되어있는 파일이며 DFAclass와 유사합니다.


실행 방법
run.py를 python 으로 실행하시면 됩니다.
콘솔창에서 입출력이 진행됩니다.
m-dfa로 바꾸기를 원하는 regular expression을 입력합니다.
input string은 무조건 문자 하나로 구성되며('a'-'z'(e는 제외), 'A'-'Z', '0'-'9') 입실론 기호는 e로 표현합니다.
E := a | E+E | EE | E* | (E) (a : alphabet)
와 같은 형태로 regular expression을 정의합니다.
적절한 regular expression을 입력후 enter를 치면
그에 상응하는 e-NFA, dfa, m-dfa를 출력하고 m-dfa를 이용하여 실제 string들이 그 dfa를 만족하는지 test할 수 있습니다.


입출력 예시.
/System/Library/Frameworks/Python.framework/Versions/2.7/bin/python2.7 "/Users/ddubby/Desktop/2015 가을학기/CS322 오토마타/Project/Automata 2/run.py"
Input the regular expression (e = epsilon) :
(a+b)(ab)*(e+1)
##epsilon-NFA to m-DFA Simulator##
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
['a', 'b', '1']
1 a 2
3 b 4
5 eps 1
5 eps 3
2 eps 6
4 eps 6
7 a 8
9 b 10
8 eps 9
11 eps 7
10 eps 7
10 eps 12
11 eps 12
13 eps 14
15 1 16
17 eps 13
17 eps 15
14 eps 18
16 eps 18
12 eps 17
6 eps 11
5
[18]
A NFA is successfully made!
#################  DFA  #################
States :  [0, 1, 2, 3, 4, 5, 6]
Vocabulary :  ['a', 'b', '1']
State Transition Functions :
( 0 , a ) =>  1
( 0 , b ) =>  2
( 0 , 1 ) =>  3
( 3 , a ) =>  3
( 3 , b ) =>  3
( 3 , 1 ) =>  3
( 2 , a ) =>  4
( 2 , b ) =>  3
( 2 , 1 ) =>  5
( 5 , a ) =>  3
( 5 , b ) =>  3
( 5 , 1 ) =>  3
( 4 , a ) =>  3
( 4 , b ) =>  6
( 4 , 1 ) =>  3
( 6 , a ) =>  4
( 6 , b ) =>  3
( 6 , 1 ) =>  5
( 1 , a ) =>  4
( 1 , b ) =>  3
( 1 , 1 ) =>  5
Initial State :  0
Final State :  [1, 2, 5, 6]
A DFA is successfully made!
################# m-DFA  #################
States :  [0, 1, 2, 3, 4]
Vocabulary :  ['a', 'b', '1']
State Transition Functions :
( 0 , a ) =>  1
( 0 , b ) =>  1
( 0 , 1 ) =>  2
( 1 , a ) =>  3
( 1 , b ) =>  2
( 1 , 1 ) =>  4
( 2 , a ) =>  2
( 2 , b ) =>  2
( 2 , 1 ) =>  2
( 3 , a ) =>  2
( 3 , b ) =>  1
( 3 , 1 ) =>  2
( 4 , a ) =>  2
( 4 , b ) =>  2
( 4 , 1 ) =>  2
Initial State :  0
Final State :  [1, 4]
DFA TEST!!!
REGULAR EXPRESSION :  (a+b)(ab)*(e+1)
Input the string or "EXIT" to Exit
a1
네
Input the string or "EXIT" to Exit
a
네
Input the string or "EXIT" to Exit
bbbabab
아니오
Input the string or "EXIT" to Exit
ababab1
아니오
Input the string or "EXIT" to Exit
aabababababab
네
Input the string or "EXIT" to Exit
a1
네
Input the string or "EXIT" to Exit
b1
네
Input the string or "EXIT" to Exit
aabb
아니오
Input the string or "EXIT" to Exit
abba
아니오
Input the string or "EXIT" to Exit
abab
아니오
Input the string or "EXIT" to Exit
bababa
아니오
Input the string or "EXIT" to Exit
babab
네
Input the string or "EXIT" to Exit
EXIT
Good Bye!!

Process finished with exit code 0
