20120352 김태연
오토마타 프로젝트 3 3 * 4 한글 자판을 위한 한글 모아쓰기 오토마타

작업환경
OS : OS X Yosemitie 10.10
Language : Python 2.7.6
IDE : PyCharm CE
Working with UTF-8 encoding

파일 구성/설명
ply directory
Construct_korean.py
DFAsimulator.py
NFAsimulator.py
Mealy_machine_simulator.py
run.py
README.txt

Construct_korean.py -> 한글을 받아들일 수 있는 Mealy machine을 구성하기 위한 파일입니다.
transition table과 output table에 적절한 program block들이 함유된 mealy machine을 구성해 주었습니다.
DFAsimulator.py, NFAsimulator.py 적절한 DFA와 NFA를 구성하기 위한 파일입니다.
Mealy_machine_simulator.py -> Me class가 정의되어 있는 파일입니다.
ply directory -> lex.py/yacc.py가 들어있는 파일입니다.
run.py -> 실제 프로젝트 3이 작동되는 파일이며 콘솔 입출력이 이루어집니다.


실행 방법
run.py를 python 으로 실행하시면 됩니다 콘솔창으로 입력과 출력이 진행됩니다.

입력 방법
3*4 한글 자판의 문자열을 입력합니다.

1      2     3
ㅣ     .     ㅡ
q      w     e
ㄱㅋㄲ  ㄴㄹ  ㄷㅌㄸ
a      s     d
ㅂㅍㅃ ㅅㅎㅆ  ㅈㅊㅉ
       x     c
      ㅇㅁ   word-terminal

키보드 자판에 있지 않은 문자열들이 입력된 경우나 완성된 한글이 아닌 문자열들이 입력된 경우
regular expression으로 만든 m-dfa에서 받아들이지 못해 wrong input으로 처리됩니다.
원래 휴대폰처럼 한문자를 여러번 누르면 순환하는 기능은 구현하지 않았습니다.
새로운 단어를 입력하고 싶을 경우에는 CLEAR를 입력하면 새롭게 단어 입력이 시작됩니다.
단어 입력 도중에 입력을 잘못하여서 이전상태로 돌아가고 싶으면 '@'를 입력하여 자모를 하나 지울 수 있습니다.
'c'를 문자열 사이에 입력하면 한 문자가 종료됩니다.
q12qcq23 -> 각고
q12qq23 -> 가코
EXIT을 입력하면 프로그램이 종료됩니다.


제한 조건
입력된 문자열로 한글 자모를 구성 했을 때 한글 문법 규칙에 어긋나는(오토마타가 받아들이지 못하는 경우)는 입력이 들어올 경우 제대로 처리되지 않고,
다시 입력을 요청합니다. 원래의 상태는 보존 됩니다.
글자가 없는데 !를 입력하면 Not Valid Backspace를 출력합니다.

입출력 예시.

/System/Library/Frameworks/Python.framework/Versions/2.7/bin/python2.7 "/Users/ddubby/Desktop/2015 가을학기/CS322 오토마타/Project/Automata 3/run.py"
##한글모아쓰기 오토마타##

Input a complete strings, "EXIT" : Exit, ''"@"'' : Backspace, "CLEAR" : New word :
1      2     3
ㅣ     .     ㅡ
q      w     e
ㄱㅋㄲ  ㄴㄹ  ㄷㅌㄸ
a      s     d
ㅂㅍㅃ ㅅㅎㅆ  ㅈㅊㅉ
       x     c
      ㅇㅁ   word-terminal

q1222
Not valid input!!

Input a complete strings, "EXIT" : Exit, ''"@"'' : Backspace, "CLEAR" : New word :
1      2     3
ㅣ     .     ㅡ
q      w     e
ㄱㅋㄲ  ㄴㄹ  ㄷㅌㄸ
a      s     d
ㅂㅍㅃ ㅅㅎㅆ  ㅈㅊㅉ
       x     c
      ㅇㅁ   word-terminal

q12qcq23
네
받침우선      초성우선
ㄱ         ㄱ
가         가
각         가ㄱ
각ㄱ         각ㄱ
각고         각고
Current Input: ㄱㅏㄱㄱㅗ

Input a complete strings, "EXIT" : Exit, ''"@"'' : Backspace, "CLEAR" : New word :
1      2     3
ㅣ     .     ㅡ
q      w     e
ㄱㅋㄲ  ㄴㄹ  ㄷㅌㄸ
a      s     d
ㅂㅍㅃ ㅅㅎㅆ  ㅈㅊㅉ
       x     c
      ㅇㅁ   word-terminal

CLEAR

Input a complete strings, "EXIT" : Exit, ''"@"'' : Backspace, "CLEAR" : New word :
1      2     3
ㅣ     .     ㅡ
q      w     e
ㄱㅋㄲ  ㄴㄹ  ㄷㅌㄸ
a      s     d
ㅂㅍㅃ ㅅㅎㅆ  ㅈㅊㅉ
       x     c
      ㅇㅁ   word-terminal

q12qq23
네
받침우선      초성우선
ㄱ         ㄱ
가         가
갘         가ㅋ
가코         가코
Current Input: ㄱㅏㅋㅗ

Input a complete strings, "EXIT" : Exit, ''"@"'' : Backspace, "CLEAR" : New word :
1      2     3
ㅣ     .     ㅡ
q      w     e
ㄱㅋㄲ  ㄴㄹ  ㄷㅌㄸ
a      s     d
ㅂㅍㅃ ㅅㅎㅆ  ㅈㅊㅉ
       x     c
      ㅇㅁ   word-terminal

CLEAR

Input a complete strings, "EXIT" : Exit, ''"@"'' : Backspace, "CLEAR" : New word :
1      2     3
ㅣ     .     ㅡ
q      w     e
ㄱㅋㄲ  ㄴㄹ  ㄷㅌㄸ
a      s     d
ㅂㅍㅃ ㅅㅎㅆ  ㅈㅊㅉ
       x     c
      ㅇㅁ   word-terminal

x23ee23xx12ee12a23waa3ww23d211qee3
네
받침우선      초성우선
ㅇ         ㅇ
오         오
옽         오ㅌ
오토         오토
오톰         오토ㅁ
오토마         오토마
오토맡         오토마ㅌ
오토마타         오토마타
오토마탑         오토마타ㅂ
오토마타보         오토마타보
오토마타본         오토마타보ㄴ
오토마타본ㅍ         오토마타본ㅍ
오토마타본프         오토마타본프
오토마타본플         오토마타본프ㄹ
오토마타본프로         오토마타본프로
오토마타본프롲         오토마타본프로ㅈ
오토마타본프로제         오토마타본프로제
오토마타본프로젝         오토마타본프로제ㄱ
오토마타본프로젝ㅌ         오토마타본프로젝ㅌ
오토마타본프로젝트         오토마타본프로젝트
Current Input: ㅇㅗㅌㅗㅁㅏㅌㅏㅂㅗㄴㅍㅡㄹㅗㅈㅔㄱㅌㅡ

Input a complete strings, "EXIT" : Exit, ''"@"'' : Backspace, "CLEAR" : New word :
1      2     3
ㅣ     .     ㅡ
q      w     e
ㄱㅋㄲ  ㄴㄹ  ㄷㅌㄸ
a      s     d
ㅂㅍㅃ ㅅㅎㅆ  ㅈㅊㅉ
       x     c
      ㅇㅁ   word-terminal

a12wq12as3aw1e12
네
받침우선      초성우선
ㅇ         ㅇ
오         오
옽         오ㅌ
오토         오토
오톰         오토ㅁ
오토마         오토마
오토맡         오토마ㅌ
오토마타         오토마타
오토마탑         오토마타ㅂ
오토마타보         오토마타보
오토마타본         오토마타보ㄴ
오토마타본ㅍ         오토마타본ㅍ
오토마타본프         오토마타본프
오토마타본플         오토마타본프ㄹ
오토마타본프로         오토마타본프로
오토마타본프롲         오토마타본프로ㅈ
오토마타본프로제         오토마타본프로제
오토마타본프로젝         오토마타본프로제ㄱ
오토마타본프로젝ㅌ         오토마타본프로젝ㅌ
오토마타본프로젝트         오토마타본프로젝트
오토마타본프로젝틉         오토마타본프로젝트ㅂ
오토마타본프로젝트바         오토마타본프로젝트바
오토마타본프로젝트반         오토마타본프로젝트바ㄴ
오토마타본프로젝트반ㄱ         오토마타본프로젝트반ㄱ
오토마타본프로젝트반가         오토마타본프로젝트반가
오토마타본프로젝트반갑         오토마타본프로젝트반가ㅂ
오토마타본프로젝트반값         오토마타본프로젝트반갑ㅅ
오토마타본프로젝트반갑스         오토마타본프로젝트반갑스
오토마타본프로젝트반갑습         오토마타본프로젝트반갑스ㅂ
오토마타본프로젝트반갑습ㄴ         오토마타본프로젝트반갑습ㄴ
오토마타본프로젝트반갑습니         오토마타본프로젝트반갑습니
오토마타본프로젝트반갑습닏         오토마타본프로젝트반갑습니ㄷ
오토마타본프로젝트반갑습니다         오토마타본프로젝트반갑습니다
Current Input: ㅇㅗㅌㅗㅁㅏㅌㅏㅂㅗㄴㅍㅡㄹㅗㅈㅔㄱㅌㅡㅂㅏㄴㄱㅏㅂㅅㅡㅂㄴㅣㄷㅏ

Input a complete strings, "EXIT" : Exit, ''"@"'' : Backspace, "CLEAR" : New word :
1      2     3
ㅣ     .     ㅡ
q      w     e
ㄱㅋㄲ  ㄴㄹ  ㄷㅌㄸ
a      s     d
ㅂㅍㅃ ㅅㅎㅆ  ㅈㅊㅉ
       x     c
      ㅇㅁ   word-terminal

ss3ss211
네
받침우선      초성우선
ㅇ         ㅇ
오         오
옽         오ㅌ
오토         오토
오톰         오토ㅁ
오토마         오토마
오토맡         오토마ㅌ
오토마타         오토마타
오토마탑         오토마타ㅂ
오토마타보         오토마타보
오토마타본         오토마타보ㄴ
오토마타본ㅍ         오토마타본ㅍ
오토마타본프         오토마타본프
오토마타본플         오토마타본프ㄹ
오토마타본프로         오토마타본프로
오토마타본프롲         오토마타본프로ㅈ
오토마타본프로제         오토마타본프로제
오토마타본프로젝         오토마타본프로제ㄱ
오토마타본프로젝ㅌ         오토마타본프로젝ㅌ
오토마타본프로젝트         오토마타본프로젝트
오토마타본프로젝틉         오토마타본프로젝트ㅂ
오토마타본프로젝트바         오토마타본프로젝트바
오토마타본프로젝트반         오토마타본프로젝트바ㄴ
오토마타본프로젝트반ㄱ         오토마타본프로젝트반ㄱ
오토마타본프로젝트반가         오토마타본프로젝트반가
오토마타본프로젝트반갑         오토마타본프로젝트반가ㅂ
오토마타본프로젝트반값         오토마타본프로젝트반갑ㅅ
오토마타본프로젝트반갑스         오토마타본프로젝트반갑스
오토마타본프로젝트반갑습         오토마타본프로젝트반갑스ㅂ
오토마타본프로젝트반갑습ㄴ         오토마타본프로젝트반갑습ㄴ
오토마타본프로젝트반갑습니         오토마타본프로젝트반갑습니
오토마타본프로젝트반갑습닏         오토마타본프로젝트반갑습니ㄷ
오토마타본프로젝트반갑습니다         오토마타본프로젝트반갑습니다
오토마타본프로젝트반갑습니닿         오토마타본프로젝트반갑습니다ㅎ
오토마타본프로젝트반갑습니다흐         오토마타본프로젝트반갑습니다흐
오토마타본프로젝트반갑습니다흫         오토마타본프로젝트반갑습니다흐ㅎ
오토마타본프로젝트반갑습니다흐헤         오토마타본프로젝트반갑습니다흐헤
Current Input: ㅇㅗㅌㅗㅁㅏㅌㅏㅂㅗㄴㅍㅡㄹㅗㅈㅔㄱㅌㅡㅂㅏㄴㄱㅏㅂㅅㅡㅂㄴㅣㄷㅏㅎㅡㅎㅔ

Input a complete strings, "EXIT" : Exit, ''"@"'' : Backspace, "CLEAR" : New word :
1      2     3
ㅣ     .     ㅡ
q      w     e
ㄱㅋㄲ  ㄴㄹ  ㄷㅌㄸ
a      s     d
ㅂㅍㅃ ㅅㅎㅆ  ㅈㅊㅉ
       x     c
      ㅇㅁ   word-terminal

@
ㅇㅗㅌㅗㅁㅏㅌㅏㅂㅗㄴㅍㅡㄹㅗㅈㅔㄱㅌㅡㅂㅏㄴㄱㅏㅂㅅㅡㅂㄴㅣㄷㅏㅎㅡㅎ
받침우선      초성우선
ㅇ         ㅇ
오         오
옽         오ㅌ
오토         오토
오톰         오토ㅁ
오토마         오토마
오토맡         오토마ㅌ
오토마타         오토마타
오토마탑         오토마타ㅂ
오토마타보         오토마타보
오토마타본         오토마타보ㄴ
오토마타본ㅍ         오토마타본ㅍ
오토마타본프         오토마타본프
오토마타본플         오토마타본프ㄹ
오토마타본프로         오토마타본프로
오토마타본프롲         오토마타본프로ㅈ
오토마타본프로제         오토마타본프로제
오토마타본프로젝         오토마타본프로제ㄱ
오토마타본프로젝ㅌ         오토마타본프로젝ㅌ
오토마타본프로젝트         오토마타본프로젝트
오토마타본프로젝틉         오토마타본프로젝트ㅂ
오토마타본프로젝트바         오토마타본프로젝트바
오토마타본프로젝트반         오토마타본프로젝트바ㄴ
오토마타본프로젝트반ㄱ         오토마타본프로젝트반ㄱ
오토마타본프로젝트반가         오토마타본프로젝트반가
오토마타본프로젝트반갑         오토마타본프로젝트반가ㅂ
오토마타본프로젝트반값         오토마타본프로젝트반갑ㅅ
오토마타본프로젝트반갑스         오토마타본프로젝트반갑스
오토마타본프로젝트반갑습         오토마타본프로젝트반갑스ㅂ
오토마타본프로젝트반갑습ㄴ         오토마타본프로젝트반갑습ㄴ
오토마타본프로젝트반갑습니         오토마타본프로젝트반갑습니
오토마타본프로젝트반갑습닏         오토마타본프로젝트반갑습니ㄷ
오토마타본프로젝트반갑습니다         오토마타본프로젝트반갑습니다
오토마타본프로젝트반갑습니닿         오토마타본프로젝트반갑습니다ㅎ
오토마타본프로젝트반갑습니다흐         오토마타본프로젝트반갑습니다흐
오토마타본프로젝트반갑습니다흫         오토마타본프로젝트반갑습니다흐ㅎ

Input a complete strings, "EXIT" : Exit, ''"@"'' : Backspace, "CLEAR" : New word :
1      2     3
ㅣ     .     ㅡ
q      w     e
ㄱㅋㄲ  ㄴㄹ  ㄷㅌㄸ
a      s     d
ㅂㅍㅃ ㅅㅎㅆ  ㅈㅊㅉ
       x     c
      ㅇㅁ   word-terminal

@
ㅇㅗㅌㅗㅁㅏㅌㅏㅂㅗㄴㅍㅡㄹㅗㅈㅔㄱㅌㅡㅂㅏㄴㄱㅏㅂㅅㅡㅂㄴㅣㄷㅏㅎㅡ
받침우선      초성우선
ㅇ         ㅇ
오         오
옽         오ㅌ
오토         오토
오톰         오토ㅁ
오토마         오토마
오토맡         오토마ㅌ
오토마타         오토마타
오토마탑         오토마타ㅂ
오토마타보         오토마타보
오토마타본         오토마타보ㄴ
오토마타본ㅍ         오토마타본ㅍ
오토마타본프         오토마타본프
오토마타본플         오토마타본프ㄹ
오토마타본프로         오토마타본프로
오토마타본프롲         오토마타본프로ㅈ
오토마타본프로제         오토마타본프로제
오토마타본프로젝         오토마타본프로제ㄱ
오토마타본프로젝ㅌ         오토마타본프로젝ㅌ
오토마타본프로젝트         오토마타본프로젝트
오토마타본프로젝틉         오토마타본프로젝트ㅂ
오토마타본프로젝트바         오토마타본프로젝트바
오토마타본프로젝트반         오토마타본프로젝트바ㄴ
오토마타본프로젝트반ㄱ         오토마타본프로젝트반ㄱ
오토마타본프로젝트반가         오토마타본프로젝트반가
오토마타본프로젝트반갑         오토마타본프로젝트반가ㅂ
오토마타본프로젝트반값         오토마타본프로젝트반갑ㅅ
오토마타본프로젝트반갑스         오토마타본프로젝트반갑스
오토마타본프로젝트반갑습         오토마타본프로젝트반갑스ㅂ
오토마타본프로젝트반갑습ㄴ         오토마타본프로젝트반갑습ㄴ
오토마타본프로젝트반갑습니         오토마타본프로젝트반갑습니
오토마타본프로젝트반갑습닏         오토마타본프로젝트반갑습니ㄷ
오토마타본프로젝트반갑습니다         오토마타본프로젝트반갑습니다
오토마타본프로젝트반갑습니닿         오토마타본프로젝트반갑습니다ㅎ
오토마타본프로젝트반갑습니다흐         오토마타본프로젝트반갑습니다흐

Input a complete strings, "EXIT" : Exit, ''"@"'' : Backspace, "CLEAR" : New word :
1      2     3
ㅣ     .     ㅡ
q      w     e
ㄱㅋㄲ  ㄴㄹ  ㄷㅌㄸ
a      s     d
ㅂㅍㅃ ㅅㅎㅆ  ㅈㅊㅉ
       x     c
      ㅇㅁ   word-terminal

s3
네
받침우선      초성우선
ㅇ         ㅇ
오         오
옽         오ㅌ
오토         오토
오톰         오토ㅁ
오토마         오토마
오토맡         오토마ㅌ
오토마타         오토마타
오토마탑         오토마타ㅂ
오토마타보         오토마타보
오토마타본         오토마타보ㄴ
오토마타본ㅍ         오토마타본ㅍ
오토마타본프         오토마타본프
오토마타본플         오토마타본프ㄹ
오토마타본프로         오토마타본프로
오토마타본프롲         오토마타본프로ㅈ
오토마타본프로제         오토마타본프로제
오토마타본프로젝         오토마타본프로제ㄱ
오토마타본프로젝ㅌ         오토마타본프로젝ㅌ
오토마타본프로젝트         오토마타본프로젝트
오토마타본프로젝틉         오토마타본프로젝트ㅂ
오토마타본프로젝트바         오토마타본프로젝트바
오토마타본프로젝트반         오토마타본프로젝트바ㄴ
오토마타본프로젝트반ㄱ         오토마타본프로젝트반ㄱ
오토마타본프로젝트반가         오토마타본프로젝트반가
오토마타본프로젝트반갑         오토마타본프로젝트반가ㅂ
오토마타본프로젝트반값         오토마타본프로젝트반갑ㅅ
오토마타본프로젝트반갑스         오토마타본프로젝트반갑스
오토마타본프로젝트반갑습         오토마타본프로젝트반갑스ㅂ
오토마타본프로젝트반갑습ㄴ         오토마타본프로젝트반갑습ㄴ
오토마타본프로젝트반갑습니         오토마타본프로젝트반갑습니
오토마타본프로젝트반갑습닏         오토마타본프로젝트반갑습니ㄷ
오토마타본프로젝트반갑습니다         오토마타본프로젝트반갑습니다
오토마타본프로젝트반갑습니닿         오토마타본프로젝트반갑습니다ㅎ
오토마타본프로젝트반갑습니다흐         오토마타본프로젝트반갑습니다흐
오토마타본프로젝트반갑습니다흣         오토마타본프로젝트반갑습니다흐ㅅ
오토마타본프로젝트반갑습니다흐스         오토마타본프로젝트반갑습니다흐스
Current Input: ㅇㅗㅌㅗㅁㅏㅌㅏㅂㅗㄴㅍㅡㄹㅗㅈㅔㄱㅌㅡㅂㅏㄴㄱㅏㅂㅅㅡㅂㄴㅣㄷㅏㅎㅡㅅㅡ

Input a complete strings, "EXIT" : Exit, ''"@"'' : Backspace, "CLEAR" : New word :
1      2     3
ㅣ     .     ㅡ
q      w     e
ㄱㅋㄲ  ㄴㄹ  ㄷㅌㄸ
a      s     d
ㅂㅍㅃ ㅅㅎㅆ  ㅈㅊㅉ
       x     c
      ㅇㅁ   word-terminal

@
ㅇㅗㅌㅗㅁㅏㅌㅏㅂㅗㄴㅍㅡㄹㅗㅈㅔㄱㅌㅡㅂㅏㄴㄱㅏㅂㅅㅡㅂㄴㅣㄷㅏㅎㅡㅅ
받침우선      초성우선
ㅇ         ㅇ
오         오
옽         오ㅌ
오토         오토
오톰         오토ㅁ
오토마         오토마
오토맡         오토마ㅌ
오토마타         오토마타
오토마탑         오토마타ㅂ
오토마타보         오토마타보
오토마타본         오토마타보ㄴ
오토마타본ㅍ         오토마타본ㅍ
오토마타본프         오토마타본프
오토마타본플         오토마타본프ㄹ
오토마타본프로         오토마타본프로
오토마타본프롲         오토마타본프로ㅈ
오토마타본프로제         오토마타본프로제
오토마타본프로젝         오토마타본프로제ㄱ
오토마타본프로젝ㅌ         오토마타본프로젝ㅌ
오토마타본프로젝트         오토마타본프로젝트
오토마타본프로젝틉         오토마타본프로젝트ㅂ
오토마타본프로젝트바         오토마타본프로젝트바
오토마타본프로젝트반         오토마타본프로젝트바ㄴ
오토마타본프로젝트반ㄱ         오토마타본프로젝트반ㄱ
오토마타본프로젝트반가         오토마타본프로젝트반가
오토마타본프로젝트반갑         오토마타본프로젝트반가ㅂ
오토마타본프로젝트반값         오토마타본프로젝트반갑ㅅ
오토마타본프로젝트반갑스         오토마타본프로젝트반갑스
오토마타본프로젝트반갑습         오토마타본프로젝트반갑스ㅂ
오토마타본프로젝트반갑습ㄴ         오토마타본프로젝트반갑습ㄴ
오토마타본프로젝트반갑습니         오토마타본프로젝트반갑습니
오토마타본프로젝트반갑습닏         오토마타본프로젝트반갑습니ㄷ
오토마타본프로젝트반갑습니다         오토마타본프로젝트반갑습니다
오토마타본프로젝트반갑습니닿         오토마타본프로젝트반갑습니다ㅎ
오토마타본프로젝트반갑습니다흐         오토마타본프로젝트반갑습니다흐
오토마타본프로젝트반갑습니다흣         오토마타본프로젝트반갑습니다흐ㅅ

Input a complete strings, "EXIT" : Exit, ''"@"'' : Backspace, "CLEAR" : New word :
1      2     3
ㅣ     .     ㅡ
q      w     e
ㄱㅋㄲ  ㄴㄹ  ㄷㅌㄸ
a      s     d
ㅂㅍㅃ ㅅㅎㅆ  ㅈㅊㅉ
       x     c
      ㅇㅁ   word-terminal

@
ㅇㅗㅌㅗㅁㅏㅌㅏㅂㅗㄴㅍㅡㄹㅗㅈㅔㄱㅌㅡㅂㅏㄴㄱㅏㅂㅅㅡㅂㄴㅣㄷㅏㅎㅡ
받침우선      초성우선
ㅇ         ㅇ
오         오
옽         오ㅌ
오토         오토
오톰         오토ㅁ
오토마         오토마
오토맡         오토마ㅌ
오토마타         오토마타
오토마탑         오토마타ㅂ
오토마타보         오토마타보
오토마타본         오토마타보ㄴ
오토마타본ㅍ         오토마타본ㅍ
오토마타본프         오토마타본프
오토마타본플         오토마타본프ㄹ
오토마타본프로         오토마타본프로
오토마타본프롲         오토마타본프로ㅈ
오토마타본프로제         오토마타본프로제
오토마타본프로젝         오토마타본프로제ㄱ
오토마타본프로젝ㅌ         오토마타본프로젝ㅌ
오토마타본프로젝트         오토마타본프로젝트
오토마타본프로젝틉         오토마타본프로젝트ㅂ
오토마타본프로젝트바         오토마타본프로젝트바
오토마타본프로젝트반         오토마타본프로젝트바ㄴ
오토마타본프로젝트반ㄱ         오토마타본프로젝트반ㄱ
오토마타본프로젝트반가         오토마타본프로젝트반가
오토마타본프로젝트반갑         오토마타본프로젝트반가ㅂ
오토마타본프로젝트반값         오토마타본프로젝트반갑ㅅ
오토마타본프로젝트반갑스         오토마타본프로젝트반갑스
오토마타본프로젝트반갑습         오토마타본프로젝트반갑스ㅂ
오토마타본프로젝트반갑습ㄴ         오토마타본프로젝트반갑습ㄴ
오토마타본프로젝트반갑습니         오토마타본프로젝트반갑습니
오토마타본프로젝트반갑습닏         오토마타본프로젝트반갑습니ㄷ
오토마타본프로젝트반갑습니다         오토마타본프로젝트반갑습니다
오토마타본프로젝트반갑습니닿         오토마타본프로젝트반갑습니다ㅎ
오토마타본프로젝트반갑습니다흐         오토마타본프로젝트반갑습니다흐

Input a complete strings, "EXIT" : Exit, ''"@"'' : Backspace, "CLEAR" : New word :
1      2     3
ㅣ     .     ㅡ
q      w     e
ㄱㅋㄲ  ㄴㄹ  ㄷㅌㄸ
a      s     d
ㅂㅍㅃ ㅅㅎㅆ  ㅈㅊㅉ
       x     c
      ㅇㅁ   word-terminal

ss3
네
받침우선      초성우선
ㅇ         ㅇ
오         오
옽         오ㅌ
오토         오토
오톰         오토ㅁ
오토마         오토마
오토맡         오토마ㅌ
오토마타         오토마타
오토마탑         오토마타ㅂ
오토마타보         오토마타보
오토마타본         오토마타보ㄴ
오토마타본ㅍ         오토마타본ㅍ
오토마타본프         오토마타본프
오토마타본플         오토마타본프ㄹ
오토마타본프로         오토마타본프로
오토마타본프롲         오토마타본프로ㅈ
오토마타본프로제         오토마타본프로제
오토마타본프로젝         오토마타본프로제ㄱ
오토마타본프로젝ㅌ         오토마타본프로젝ㅌ
오토마타본프로젝트         오토마타본프로젝트
오토마타본프로젝틉         오토마타본프로젝트ㅂ
오토마타본프로젝트바         오토마타본프로젝트바
오토마타본프로젝트반         오토마타본프로젝트바ㄴ
오토마타본프로젝트반ㄱ         오토마타본프로젝트반ㄱ
오토마타본프로젝트반가         오토마타본프로젝트반가
오토마타본프로젝트반갑         오토마타본프로젝트반가ㅂ
오토마타본프로젝트반값         오토마타본프로젝트반갑ㅅ
오토마타본프로젝트반갑스         오토마타본프로젝트반갑스
오토마타본프로젝트반갑습         오토마타본프로젝트반갑스ㅂ
오토마타본프로젝트반갑습ㄴ         오토마타본프로젝트반갑습ㄴ
오토마타본프로젝트반갑습니         오토마타본프로젝트반갑습니
오토마타본프로젝트반갑습닏         오토마타본프로젝트반갑습니ㄷ
오토마타본프로젝트반갑습니다         오토마타본프로젝트반갑습니다
오토마타본프로젝트반갑습니닿         오토마타본프로젝트반갑습니다ㅎ
오토마타본프로젝트반갑습니다흐         오토마타본프로젝트반갑습니다흐
오토마타본프로젝트반갑습니다흫         오토마타본프로젝트반갑습니다흐ㅎ
오토마타본프로젝트반갑습니다흐흐         오토마타본프로젝트반갑습니다흐흐
Current Input: ㅇㅗㅌㅗㅁㅏㅌㅏㅂㅗㄴㅍㅡㄹㅗㅈㅔㄱㅌㅡㅂㅏㄴㄱㅏㅂㅅㅡㅂㄴㅣㄷㅏㅎㅡㅎㅡ

Input a complete strings, "EXIT" : Exit, ''"@"'' : Backspace, "CLEAR" : New word :
1      2     3
ㅣ     .     ㅡ
q      w     e
ㄱㅋㄲ  ㄴㄹ  ㄷㅌㄸ
a      s     d
ㅂㅍㅃ ㅅㅎㅆ  ㅈㅊㅉ
       x     c
      ㅇㅁ   word-terminal

a32211wwqee3211wwa
Not valid input!!

Input a complete strings, "EXIT" : Exit, ''"@"'' : Backspace, "CLEAR" : New word :
1      2     3
ㅣ     .     ㅡ
q      w     e
ㄱㅋㄲ  ㄴㄹ  ㄷㅌㄸ
a      s     d
ㅂㅍㅃ ㅅㅎㅆ  ㅈㅊㅉ
       x     c
      ㅇㅁ   word-terminal

a32211wwqeee32211wwa
네
받침우선      초성우선
ㅇ         ㅇ
오         오
옽         오ㅌ
오토         오토
오톰         오토ㅁ
오토마         오토마
오토맡         오토마ㅌ
오토마타         오토마타
오토마탑         오토마타ㅂ
오토마타보         오토마타보
오토마타본         오토마타보ㄴ
오토마타본ㅍ         오토마타본ㅍ
오토마타본프         오토마타본프
오토마타본플         오토마타본프ㄹ
오토마타본프로         오토마타본프로
오토마타본프롲         오토마타본프로ㅈ
오토마타본프로제         오토마타본프로제
오토마타본프로젝         오토마타본프로제ㄱ
오토마타본프로젝ㅌ         오토마타본프로젝ㅌ
오토마타본프로젝트         오토마타본프로젝트
오토마타본프로젝틉         오토마타본프로젝트ㅂ
오토마타본프로젝트바         오토마타본프로젝트바
오토마타본프로젝트반         오토마타본프로젝트바ㄴ
오토마타본프로젝트반ㄱ         오토마타본프로젝트반ㄱ
오토마타본프로젝트반가         오토마타본프로젝트반가
오토마타본프로젝트반갑         오토마타본프로젝트반가ㅂ
오토마타본프로젝트반값         오토마타본프로젝트반갑ㅅ
오토마타본프로젝트반갑스         오토마타본프로젝트반갑스
오토마타본프로젝트반갑습         오토마타본프로젝트반갑스ㅂ
오토마타본프로젝트반갑습ㄴ         오토마타본프로젝트반갑습ㄴ
오토마타본프로젝트반갑습니         오토마타본프로젝트반갑습니
오토마타본프로젝트반갑습닏         오토마타본프로젝트반갑습니ㄷ
오토마타본프로젝트반갑습니다         오토마타본프로젝트반갑습니다
오토마타본프로젝트반갑습니닿         오토마타본프로젝트반갑습니다ㅎ
오토마타본프로젝트반갑습니다흐         오토마타본프로젝트반갑습니다흐
오토마타본프로젝트반갑습니다흫         오토마타본프로젝트반갑습니다흐ㅎ
오토마타본프로젝트반갑습니다흐흐         오토마타본프로젝트반갑습니다흐흐
오토마타본프로젝트반갑습니다흐흡         오토마타본프로젝트반갑습니다흐흐ㅂ
오토마타본프로젝트반갑습니다흐흐부         오토마타본프로젝트반갑습니다흐흐부
오토마타본프로젝트반갑습니다흐흐붸         오토마타본프로젝트반갑습니다흐흐붸
오토마타본프로젝트반갑습니다흐흐뷀         오토마타본프로젝트반갑습니다흐흐붸ㄹ
오토마타본프로젝트반갑습니다흐흐뷁         오토마타본프로젝트반갑습니다흐흐뷀ㄱ
오토마타본프로젝트반갑습니다흐흐뷁ㄸ         오토마타본프로젝트반갑습니다흐흐뷁ㄸ
오토마타본프로젝트반갑습니다흐흐뷁뚜         오토마타본프로젝트반갑습니다흐흐뷁뚜
오토마타본프로젝트반갑습니다흐흐뷁뛔         오토마타본프로젝트반갑습니다흐흐뷁뛔
오토마타본프로젝트반갑습니다흐흐뷁뛜         오토마타본프로젝트반갑습니다흐흐뷁뛔ㄹ
오토마타본프로젝트반갑습니다흐흐뷁뛟         오토마타본프로젝트반갑습니다흐흐뷁뛜ㅂ
Current Input: ㅇㅗㅌㅗㅁㅏㅌㅏㅂㅗㄴㅍㅡㄹㅗㅈㅔㄱㅌㅡㅂㅏㄴㄱㅏㅂㅅㅡㅂㄴㅣㄷㅏㅎㅡㅎㅡㅂㅜㅔㄹㄱㄸㅜㅔㄹㅂ

Input a complete strings, "EXIT" : Exit, ''"@"'' : Backspace, "CLEAR" : New word :
1      2     3
ㅣ     .     ㅡ
q      w     e
ㄱㅋㄲ  ㄴㄹ  ㄷㅌㄸ
a      s     d
ㅂㅍㅃ ㅅㅎㅆ  ㅈㅊㅉ
       x     c
      ㅇㅁ   word-terminal

EXIT
Good Bye!!

Process finished with exit code 0
