20120352 김태연
오토마타 프로젝트 1 한글 모아쓰기 오토마타 Mealy Machine

작업환경
OS : OS X Yosemitie 10.10
Language : Python 2.7.6
IDE : PyCharm CE
Working with UTF-8 encoding

파일 구성/설명
Mealy_machine_simulator.py
Construct_korean.py
run.py
README.txt

Construct_korean.py -> 한글을 받아들일 수 있는 Mealy machine을 구성하기 위한 파일입니다.
transition table과 output table에 적절한 program block들이 함유된 mealy machine을 구성해 주었습니다.

Mealy_machine_simulator.py -> Me class가 정의되어 있는 파일입니다.
run.py -> 실제 프로젝트 1이 작동되는 파일이며 콘솔 입출력이 이루어집니다.

실행 방법
run.py를 python 으로 실행하시면 됩니다 콘솔창으로 입력과 출력이 진행됩니다.

입력 방법
한글자모 하나씩을 반복적으로 입력하면서 그에 따라서 적절한 받침우선과 초성우선 모아쓰기 표시 방법을 확인가능 합니다.
한글자모가 아닌 글자가 입력되거나 여러글자가 한꺼번에 입력되는 경우는 Wrong Input으로 처리되지 않습니다.
새로운 단어를 입력하고 싶을 경우에는 CLEAR를 입력하면 새롭게 단어 입력이 시작됩니다.
단어 입력 도중에 입력을 잘못하여서 이전상태로 돌아가고 싶으면 !를 입력하여 자모를 하나 지울 수 있습니다.
EXIT을 입력하면 프로그램이 종료됩니다.


제한 조건
입력된 문자가 한글 자모가 아니거나 한글 문법 규칙에 어긋나는(이 한글 모아쓰기 오토마타가 받아들이지 못하는 경우)는 입력이 들어올 경우 제대로 처리되지 않고,
다시 입력을 요청합니다. 원래의 상태는 보존 됩니다.
ㅏㅣ는 ㅐ가 아니라 잘못된 입력입니다.
마찬가지로 ㅓㅣ대신 ㅔ를 입력해야합니다.
글자가 없는데 !를 입력하면 Not Valid Backspace를 출력합니다.

입출력 예시.

/System/Library/Frameworks/Python.framework/Versions/2.7/bin/python2.7 "/Users/ddubby/Desktop/2015 가을학기/CS322 오토마타/Project/Automata/run.py"
##한글모아쓰기 오토마타##
Input a character repeatedly, "EXIT" : Exit, "!" : Backspace, "CLEAR" : New word :
!
Not Valid Backspace
Input a character repeatedly, "EXIT" : Exit, "!" : Backspace, "CLEAR" : New word :
a
Wrong Input!!!
Input a character repeatedly, "EXIT" : Exit, "!" : Backspace, "CLEAR" : New word :
ㄱㄴ
Input character one by one
Input a character repeatedly, "EXIT" : Exit, "!" : Backspace, "CLEAR" : New word :
ㅎ
받침우선      초성우선
ㅎ         ㅎ
Current Input: ㅎ
Input a character repeatedly, "EXIT" : Exit, "!" : Backspace, "CLEAR" : New word :
ㅏ
받침우선      초성우선
ㅎ         ㅎ
하         하
Current Input: ㅎㅏ
Input a character repeatedly, "EXIT" : Exit, "!" : Backspace, "CLEAR" : New word :
ㄹ
받침우선      초성우선
ㅎ         ㅎ
하         하
할         하ㄹ
Current Input: ㅎㅏㄹ
Input a character repeatedly, "EXIT" : Exit, "!" : Backspace, "CLEAR" : New word :
ㅁ
받침우선      초성우선
ㅎ         ㅎ
하         하
할         하ㄹ
핢         할ㅁ
Current Input: ㅎㅏㄹㅁ
Input a character repeatedly, "EXIT" : Exit, "!" : Backspace, "CLEAR" : New word :
ㅓ
받침우선      초성우선
ㅎ         ㅎ
하         하
할         하ㄹ
핢         할ㅁ
할머         할머
Current Input: ㅎㅏㄹㅁㅓ
Input a character repeatedly, "EXIT" : Exit, "!" : Backspace, "CLEAR" : New word :
ㄴ
받침우선      초성우선
ㅎ         ㅎ
하         하
할         하ㄹ
핢         할ㅁ
할머         할머
할먼         할머ㄴ
Current Input: ㅎㅏㄹㅁㅓㄴ
Input a character repeatedly, "EXIT" : Exit, "!" : Backspace, "CLEAR" : New word :
ㅏ
받침우선      초성우선
ㅎ         ㅎ
하         하
할         하ㄹ
핢         할ㅁ
할머         할머
할먼         할머ㄴ
할머나         할머나
Current Input: ㅎㅏㄹㅁㅓㄴㅏ
Input a character repeatedly, "EXIT" : Exit, "!" : Backspace, "CLEAR" : New word :
!
ㅎㅏㄹㅁㅓㄴ
받침우선      초성우선
ㅎ         ㅎ
하         하
할         하ㄹ
핢         할ㅁ
할머         할머
할먼         할머ㄴ
Input a character repeatedly, "EXIT" : Exit, "!" : Backspace, "CLEAR" : New word :
ㅣ
받침우선      초성우선
ㅎ         ㅎ
하         하
할         하ㄹ
핢         할ㅁ
할머         할머
할먼         할머ㄴ
할머니         할머니
Current Input: ㅎㅏㄹㅁㅓㄴㅣ
Input a character repeatedly, "EXIT" : Exit, "!" : Backspace, "CLEAR" : New word :
CLEAR
Input a character repeatedly, "EXIT" : Exit, "!" : Backspace, "CLEAR" : New word :
ㅎ
받침우선      초성우선
ㅎ         ㅎ
Current Input: ㅎ
Input a character repeatedly, "EXIT" : Exit, "!" : Backspace, "CLEAR" : New word :
ㅏ
받침우선      초성우선
ㅎ         ㅎ
하         하
Current Input: ㅎㅏ
Input a character repeatedly, "EXIT" : Exit, "!" : Backspace, "CLEAR" : New word :
ㄱ
받침우선      초성우선
ㅎ         ㅎ
하         하
학         하ㄱ
Current Input: ㅎㅏㄱ
Input a character repeatedly, "EXIT" : Exit, "!" : Backspace, "CLEAR" : New word :
ㄱ
받침우선      초성우선
ㅎ         ㅎ
하         하
학         하ㄱ
학ㄱ         학ㄱ
Current Input: ㅎㅏㄱㄱ
Input a character repeatedly, "EXIT" : Exit, "!" : Backspace, "CLEAR" : New word :
ㅛ
받침우선      초성우선
ㅎ         ㅎ
하         하
학         하ㄱ
학ㄱ         학ㄱ
학교         학교
Current Input: ㅎㅏㄱㄱㅛ
Input a character repeatedly, "EXIT" : Exit, "!" : Backspace, "CLEAR" : New word :
!
ㅎㅏㄱㄱ
받침우선      초성우선
ㅎ         ㅎ
하         하
학         하ㄱ
학ㄱ         학ㄱ
Input a character repeatedly, "EXIT" : Exit, "!" : Backspace, "CLEAR" : New word :
ㅜ
받침우선      초성우선
ㅎ         ㅎ
하         하
학         하ㄱ
학ㄱ         학ㄱ
학구         학구
Current Input: ㅎㅏㄱㄱㅜ
Input a character repeatedly, "EXIT" : Exit, "!" : Backspace, "CLEAR" : New word :
!
ㅎㅏㄱㄱ
받침우선      초성우선
ㅎ         ㅎ
하         하
학         하ㄱ
학ㄱ         학ㄱ
Input a character repeatedly, "EXIT" : Exit, "!" : Backspace, "CLEAR" : New word :
!
ㅎㅏㄱ
받침우선      초성우선
ㅎ         ㅎ
하         하
학         하ㄱ
Input a character repeatedly, "EXIT" : Exit, "!" : Backspace, "CLEAR" : New word :
ㄱ
받침우선      초성우선
ㅎ         ㅎ
하         하
학         하ㄱ
학ㄱ         학ㄱ
Current Input: ㅎㅏㄱㄱ
Input a character repeatedly, "EXIT" : Exit, "!" : Backspace, "CLEAR" : New word :
ㅛ
받침우선      초성우선
ㅎ         ㅎ
하         하
학         하ㄱ
학ㄱ         학ㄱ
학교         학교
Current Input: ㅎㅏㄱㄱㅛ
Input a character repeatedly, "EXIT" : Exit, "!" : Backspace, "CLEAR" : New word :
EXIT
Good Bye!!

Process finished with exit code 0

받침우선 / 초성우성의 장단점

받침우선은 우선 우리가 일반적으로 사용하는 입력방식이며 어떤 Input이 주어졌을 때 만들어지는 한글을 정확하게 표현 가능합니다.
그러나 국어문법적으로 완성된 문자열이 아닌 예를들어 발ㅂ이라는 문자를 치고 싶을 경우에 이를 표현할 수 있는 방법이 없습니다. 그렇기에 현재의 키보드는 방향키로 다음 글자로
넘어갈 수 있게끔 이를 조정해 주고 있습니다. 대부분의 입력이 국어문법적으로 완성된 글자를 입력하기에 현재의 키보드 입력을 윈도우에서 표현하는 방식도 받침우선입니다.

그에 비해 초성우성은 밟이라는 받침있는 문자열을 표현하고 싶을때 ㅂㅏㄹㅂ 의 입력만으로 만들 수 없으며 그 다음 문자열까지 입력을 해주어야 밟이라는 글자를 표현할 수 있으므로
상대적으로 받침우선에 비해 불편합니다. 그러나 원래 내가 의도한 문자가 완성된 문자인 밟이 아니라 발ㅂ 이었을 경우에는 초성우성으로만 이 문자열을 표현 가능하고
문자열의 길이도 초성우성일 경우에만 정확하게 인식가능합니다. 또한 다음 입력될 문자의 초성이 다음 글자에 표현되어 있어서 받침에서 찾지 않아도 되므로 눈으로 보기에 편합니다.
초성우선 역시 받침우선과 같이 방향키등을 이용한다면 원하는 받침이 있는 문자열을 만들 수 있도록 할 수 있으리라고 생각합니다.