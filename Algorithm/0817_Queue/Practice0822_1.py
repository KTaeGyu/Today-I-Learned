"""
코딩대학교에서는 매년 수학 게임 페스티벌이 열립니다. 이 페스티벌에는 코코도 참가하고 있습니다.

수학 게임 페스티벌은 서바이벌 방식으로, 전 단계를 성공한 사람들이 모여 계속해서 경쟁하여 최종 우승자를 가립니다.
금년의 우승 상품은 코코가 구하고 싶어도 구할 수 없었던 고가의 그래픽 카드이기에, 이를 악물고 게임에 참여했습니다.
그렇게 마지막 게임까지 살아남은 코코는 다른 남은 5명의 경쟁자와 함께 최후의 게임을 기다리고 있습니다.

마지막 게임은 자신의 발을 구속하고 있는 자물쇠 N개를 해제하여 10m 앞의 버튼을 누르면 우승하는 게임입니다.
단, 수학 게임인 만큼 일반적인 자물쇠가 아닌, 특수 자물쇠가 주어집니다. 그리고 각 자물쇠의 "해제 번호"도 주어집니다.
이 특수한 자물쇠에는 4개의 버튼이 달려 있는데, 이 버튼들의 동작은 다음과 같습니다.

    D (Double): 현재 숫자를 2배로 만듭니다.
    단, 4자리 숫자를 넘어가는 경우에는, 10000으로 나눈 나머지로 만듭니다.
    예) 1234 -> 2468, 5555 -> 1110

    S (Subtract): 현재 숫자에서 1을 뺍니다.
    단, 만약 숫자가 0 (0000)이라면, 9999로 만듭니다.
    예) 0000 -> 9999, 1234 -> 1233
    
    L (Left rotate): 현재 숫자를 왼쪽으로 한 자리씩 회전시킵니다.
    예) 1234 -> 2341, 123 -> 1230, 1000 -> 1

    R (Right rotate): 현재 숫자를 오른쪽으로 한 자리씩 회전시킵니다.
    예) 1234 -> 4123, 123 -> 3012, 1000 -> 100
    0012, 0101을 12, 101 로 표현하는 거와 같이 자리수를 채우기 위한 '0' 은 표현되는 수에 기재하지 않습니다.

코코는 자물쇠의 초기 번호가 주어졌을 때, 자물쇠를 최소한의 동작으로 "해제 번호"를 맞추는 프로그램을 작성하여 이번 게임에서 우승을 하려고 합니다.

자물쇠의 개수와 각 자물쇠의 초기 번호, 그리고 해당 자물쇠의 해제 번호가 주어졌을 때, 최소한의 동작으로 자물쇠를 열 수 있는 정답을 출력하는 프로그램을 작성해 주세요.
단, 자물쇠를 해제하기 위한 최소한의 동작이 여러개인 경우, D-S-L-R 순으로 먼저 동작하는 조합을 출력하세요.

입력
첫번째 줄에는 자물쇠의 개수 N이 입력됩니다. (1 <= N <= 100)
두번째 줄에는 자물쇠의 초기 번호 A와 자물쇠의 해제 번호 B가 공백으로 분리되어 주어집니다.
A와 B는 항상 다른 입력값이 주어집니다. (0 <= A <= 9,999)

출력
초기 번호 A에서 해제 번호 B를 만들기 위한 자물쇠의 최소한의 동작을 각각의 줄에 출력합니다.
최소한으로 가능한 동작이 여러 개면, D-S-L-R 순으로 먼저 동작하는 동작을 출력합니다.
"""
import sys
sys.stdin = open("input.txt", "r")


def L(num):
    lst = [0]*4
    for x in range(3, -1, -1):
        lst[x] = num % 10
        num //= 10
    if lst:
        lst.append(lst.pop(0))
    result = 0
    for x in lst:
        result = result*10 + x
    return result


def R(num):
    lst = [0]*4
    for x in range(3, -1, -1):
        lst[x] = num % 10
        num //= 10
    if lst:
        lst.insert(0, lst.pop())
    result = 0
    for x in lst:
        result = result*10 + x
    return result


N = int(input())
for n in range(N):
    A, B = map(int, input().split())
    queue = [(A, '')]
    flag = True
    while flag:
        now, ctrl = queue.pop(0)
        Next = [now * 2, now - 1, L(now), R(now)]
        ctrlst = ['D', 'S', 'L', 'R']
        for i in range(4):
            if Next[i] == B:
                n_ctrl = ctrl + ctrlst[i]
                print(n_ctrl)
                flag = False
                break
            elif 0 <= Next[i] <= 9999:
                n_ctrl = ctrl + ctrlst[i]
                queue.append((Next[i], n_ctrl))

"""
6
1234 3412
123 2301
123 1230
100 1
1 8
8 1

LL
LL
L
LL
DDD
DSRDS
"""