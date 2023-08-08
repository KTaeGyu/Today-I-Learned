"""
AI의 발전으로 인해 세상의 많은 것이 편해졌다.
하지만 이로 인해 많은 것이 불편해진 것도 있다.
그 중 하나가 바로 사이버 범죄가 너무 많이 일어난다는 것이다.

사람들은 AI를 활용해 인터넷상에서 개인정보 해킹 등 여러 방면에서 문제를 일으키고 있다.
그렇기 때문에 많은 웹 사이트나 앱 중에서 "사람인가?"를 인증하기 위한 Captcha Code를 AI가 뚫을 수 없도록 발전시키고 있다.

코코가 개발한 새로운 Captcha Code 생성기는 아래와 같다.
[1] 랜덤으로 N개 길이의 Sample이 주어진다.
[2] 그리고 K개 길이의 PaseCode가 주어진다.
[3] 사용자는 Sample에서 PaseCode를 '순차적으로'만들 수 있는지를 검증해야 한다.

코코는 자신이 만든 생성기에 문자가 있는지 없는지 직접 QA 과정을 거치려고 한다.
Sample과 PaseCode가 주어졌을때, Sample에서 PaseCode를 만들 수 있는지 없는지를 판단하는 프로그램을 작성하라.

[입력]
첫번째 줄에는 테스트케이스의 개수 T가 주어진다.
두번째 줄부터 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫번째 줄에는 Sample의 길이 N, PaseCode의 길이 M가 주어진다.
각 테스트 케이스의 두번째 줄에는 N개 길이의 Sample이 공백으로 구분되어 주어진다.
각 테스트 케이스의 세번째 줄에는 M개 길이의 PaseCode가 공백으로 구분되어 주어진다.
공백으로 주어지는 값은 0과 9사이의 정수이다.

[출력]
각 테스트 케이스에 대한 결과를 각 줄에 '#' 테스트 케이스는 1번부터 시작을 출력하고 한 칸을 띄운 다음 정답을 출력한다.
정답은 만약 Sample에서 PaseCode를 생성할 수 있다면 1, 아니면 0 을 출력한다.
"""
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Sample = ''.join(input().split())
    # # 방법 1
    # PassCode = ''.join(input().split())

    # result = list(PassCode)
    # pos = 0
    # for i in range(M):
    #     for j in range(pos, N):
    #         if PassCode[i] == Sample[j]:
    #             pos = j + 1
    #             result.pop()
    #             break
    # if result:
    #     print(f'#{tc} {0}')
    # else:
    #     print(f'#{tc} {1}')
    # # 방법 2
    # PassCode = list(input().split())
    #
    # for j in range(N):
    #     if PassCode != [] and PassCode[0] == Sample[j]:
    #         PassCode.pop(0)
    #
    # if PassCode:
    #     print(f'#{tc} {0}')
    # else:
    #     print(f'#{tc} {1}')


# # 강사님 코드
# # 1. for, break 사용 방법
# T = int(input())
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     sample = list(map(int, input().split()))
#     passcode = list(map(int, input().split()))
#
#     cnt = 0
#     result = 0
#
#     for i in range(N):
#         if passcode[cnt] == sample[i]:
#             cnt += 1
#         if cnt == K:
#             result = 1
#             break
#     print(f'#{tc} {result}')
#
# # 2. index 메서드 사용
# T = int(input())
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     sample = list(map(int, input().split()))
#     passcode = list(map(int, input().split()))
#
#     indexes = []
#     result = 1
#
#     for i in range(len(passcode)):
#         now = passcode[i]
#         try:
#             index = sample.index(now)
#             sample = sample[index + 1:]
#         except:
#             result = 0
#     print(f'#{tc} {result}')
"""
1
10 4
1 1 2 2 3 3 4 4 5 5
1 2 3 4
7 4
1 2 2 4 3 3 4
4 3 2 1

#1 1
#2 0
"""