"""
AI의 발전으로 인해 세상의 많은 것이 편해졌다.
하지만 이로 인해 많은 것이 불편해진 것도 있다.
그중 하나가 바로 사이버 범죄가 너무 많이 일어난다는 것이다. 

사람들은 AI를 활용해 인터넷상에서 개인정보 해킹 등 여러 방면에서 문제를 일으키고 있다.
그렇기 때문에 많은 웹사이트나 앱 등에서 "사람인가?" 를 인증하기 위한 Captcha Code를 AI가 뚫을 수 없도록 발전시키고 있다. 

코코가 개발한 새로운 Captcha Code 생성기는 아래와 같다.
    [1] 랜덤으로 N개 길이의 Sample이 주어진다.
    [2] 그리고 K개 길이의 PassCode가 주어진다.
    [3] 사용자는 Sample에서 PassCode를 "순차적으로" 만들 수 있는지를 검증해야 한다. 

코코는 자신이 만든 생성기에 문제가 있는지 없는지 직접 QA 과정을 거치려고 한다.
Sample과 PassCode가 주어졌을때, Sample에서 PassCode를 만들 수 있는지 없는지를 판단하는 프로그램을 작성하라.

[제약사항] 
    5 <= N <= 300,000
    3 <= K < N

입력
첫번째 줄에는 테스트 케이스의 개수 T가 주어진다. 
두번째 줄부터 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫번째 줄에는 Sample의 길이 N, PassCode의 길이 K가 주어진다.
각 테스트 케이스의 두번째 줄에는 N개 길이의 Sample이 공백으로 구분되어 주어진다.
각 테스트 케이스의 세번째 줄에는 K개 길이의 PassCode가 공백으로 구분되어 주어진다. 
공백으로 주어지는 값은 0과 9사이의 정수이다.

출력
각 테스트 케이 t에 대한 결과를 각 줄에 "#t" (테스트 케이스는 1번부터 시작)을 출력하고, 한 칸을 띄운 다음 정답을 출력한다. 
정답은 만약 Sample에서 PassCode를 생성할 수 있다면 1, 아니면 0을 출력한다.
"""
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    Sample = list(map(int, input().split()))
    Passcode = list(map(int, input().split()))
    for i in Sample:
        if Passcode and i == Passcode[0]:
            Passcode.pop(0)
    if Passcode:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')

"""
2
10 4
1 1 2 2 3 3 4 4 5 5
1 2 3 4
7 4
1 2 2 4 3 3 4
4 3 2 1

#1 1
#2 0
"""