"""
가능한 날짜가 몇 개가 있는지 알려주는 프로그램을 작성해 주세요.

[세부사항]
1. 10, 11, 12월은 두 자릿수로 표현하고, 1 ~ 9월은 한 자릿수로 표현한다. 즉, 7월을 07로 표현하지 않는다.
2. 년도는 네자리로 표현한다.
3. 날짜는 모든 달이 1~31일 이라고 가정한다. 1 ~ 9일은 한 자릿수로 표현한다. 즉, 4일을 04로 편한하지 않는다.
4. 년도 부분이 찢어질 수 도 있지만, 년도가 찢어지는 것은 무시한다.
(예를 들어 xxxx.12.23인 경우 년도를 무시하기에 가능한 날짜의 수는 1개이다.)
5. x의 개수는 최대 8개 까지 될 수 있다.

[입력]
첫 번째 줄에 Y,M,D의 형식으로 날짜 정보가 주어집니다.
Y는 연도, M은 월, D는 일을 의미합니다.

[출력]
가능한 날짜의 개수를 출력합니다.
"""
import sys
sys.stdin = open("input.txt", "r")

# T = int(input())
# for tc in range(1, T+1):
Day = input().split(".")
M, D = Day[1], Day[2]

result = 1
if len(M) == 1:
    if M[0] == 'X':
        result *= 9
elif len(M) == 2:
    if M[1] == 'X':
        result *= 3

if len(D) == 1:
    if D[0] == 'X':
        result *= 9
elif len(D) == 2:
    if D[0] == 'X':
        if D[1] == 'X':
            result *= 22
        elif int(D[1]) < 2:
            result *= 3
        else:
            result *= 2
    elif D[0] == '3':
        if D[1] == 'X':
            result *= 2
    else:
        if D[1] == 'X':
            result *= 10

print(result)

# print(f'#{tc} {result}')

"""
12
2025.X.1X
XXXX.XX.XX
2025.12.31
2025.XX.31
2025.1X.31
2025.X1.31
2025.X.31
2025.12.XX
2025.12.X1
2025.12.X2
2025.12.3X
2025.12.1X
2025.12.X


90
"""
