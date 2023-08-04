"""
사과 먹기 게임은 N x N 크기의 맵에서 캐릭터를 이동하여 사과를 먹는 게임이다.
게임의 룰은 간단하다. 주어진 M 개의 사과를 사과를 1번부터 M번 사과까지 순서대로 먹기만 하면 되는 게임이다.
아래는 N = 5, M = 3의 게임맵의 예시이다. (사과의 개수 M은 입력에서 주어지지 않는다.)
배열:
0  0  0  0  0
0  0  0 '3' 0
0 '1' 0  0  0
0  0 '2' 0  0
0  0  0  0  0

실제 게임에서는 2번 사과는 1번 사과를 먹었을 때, 3번 사과는 2번 사과를 먹었을때 해당 위치에 나타난다고 생각하면 된다.
(그렇기에 i+1번째 사과를 i번째 사과 이전에 먹는 경우는 생각하지 않아도 된다.)
배열:
0  0  0  0  0        0  0  0  0  0        0  0  0  0  0
0  0  0  0  0        0  0  0  0  0        0  0  0 '3' 0
0 '1' 0  0  0   ->   0  0  0  0  0   ->   0  0  0  0  0
0  0  0  0  0        0  0 '2' 0  0        0  0  0  0  0
0  0  0  0  0        0  0  0  0  0        0  0  0  0  0

여기서 플레이어는 (0, 0)의 좌표에서, 항상 오른쪽을 향한 상태에서 시작한다.
배열:
-> 0  0  0  0
0  0  0 '3' 0
0 '1' 0  0  0
0  0 '2' 0  0
0  0  0  0  0

정상적인 게임에서는, 플레이어는 앞으로 이동하며 좌, 우 방향으로 방향을 전환하며 맵을 움직이며 사과를 순차적으로 먹기만 하면 게임이 클리어가 되는 간단한 형식이다.
하지만, 현재 게임에서는 버그가 발생하며, 플레이어가 왼쪽으로 회전을 하지 목하고 오른쪽으로만 회전이 가능한 상태이다.
즉, 기존에는 손쉽게 다음과 같은 방법으로 게임을 클리어 할 수 있을 것이다.
배열:
-  |  0  0  0
0  |  0 '3' 0
0 '1' 0  |  0
0  - '2' |  0
0  0  0  0  0

하지만 왼쪽 방향으로 회전이 불가능 하므로, 다음과 같이 게임을 클리어 해야 할 것이다.
배열:
-  |  0  0  0
0  |  0 '3' 0
0 '1' 0  |  0
-  | '2' -  |
|  -  0  |  -

이 때, 게임을 클리어하기 위한 총 우회전의 횟수는 7번이 되며, 이는 게임을 킬리어하기 위한 최소 우회전의 횟수가 된다.
게임맵에 대한 정보가 주어졌을 때, 현재 버그로 인해 전진과 우회전만 되는 상황에서 게임을 클리어 하기 위한 최소 우회전의 횟수를 구하는 프로그램을 작성하시오.

[제한조건]
5 <= N <= 10
1 <= M <= 10
사과의 번호는 1 ~ M번까지 중간 값의 누락 없이 주어짐이 보장된다.
사과의 개수 M은 직접적으로 입력이 되지 않는다.
사과는 N x N 크기의 맵의 테두리 부분에서 주어지지 않는다.(0번 행, 0번 열, N-1번 행, N-1번 열)
i 번째 사과와 i+1 번째 사과의 위치는 같은 행, 열에 주어지지 않음이 보장된다.
단, i번째 사과와 i+2번째 사과의 위치는 같은 행, 열에 주어질 수 있다.

[입력]
첫 번째 줄에 test case의 개수 T(1 <= T <= 50)가 공백주어진다. 다으므 줄부터 각 test case에 대한 정보가 주어진다.
각 test case의 첫번째 줄에는 N이 주어진다.
다음 N개의 줄에 걸쳐 게임 맵의 정보가 공백으로 구분되어 주어진다.
게임 뱁의 정보에서 0은 이동 가능한 길을 의미하며, 1~M 사이의 정수는 플레이어가 먹어야 하는 사과의 순번을 나타낸다.

[출력]
각 test case에 대하여 "#"와 test case의 번호 (1번부터 시작)와 공백을 둔 후, 주어진 게임맵에서 모든 사과를 순서대로 먹기 위해 필요한 최소한의 우회전의 수를 출력한다.
"""
from pprint import pprint
import sys
sys.stdin = open("input.txt", "r")


def search_apple(num, array):
    result = []
    for i in range(1, 11):
        try:
            for y in range(num):
                for x in range(num):
                    if array[y][x] == i:
                        result.append((y, x))
                        raise ValueError
        except ValueError:
            continue
    return result


def eat_apple(coord_list):
    count = 0  # 우회전 수
    left, right, up, down = (0, -1), (0, 1), (-1, 0), (1, 0)  # 보고있는 방향
    last_direction = right  # 시작 방향
    pos = [0, 0]  # 시작 위치
    for y, x in coord_list:  # 1번의 인덱스부터 ~
        if last_direction == right:  # 현재 보고 있는 방향 (시작 방향이 오른쪽 일때)
            if y >= pos[0] and x > pos[1]:  # 1번만 돌아도 되면
                count += 1
                last_direction = down  # 돌고 방향 재설정
            elif y > pos[0] and x <= pos[1]:  # 2번
                count += 2
                last_direction = left
            else:  # 3번
                count += 3
                last_direction = up
            pos = [y, x]  # 현재 위치 재설정
        elif last_direction == left:  # 시작 방향이 왼쪽일때
            if y <= pos[0] and x < pos[1]:
                count += 1
                last_direction = up
            elif y < pos[0] and x >= pos[1]:
                count += 2
                last_direction = right
            else:
                count += 3
                last_direction = down
            pos = [y, x]
        elif last_direction == up:
            if y < pos[0] and x >= pos[1]:
                count += 1
                last_direction = right
            elif y >= pos[0] and x > pos[1]:
                count += 2
                last_direction = down
            else:
                count += 3
                last_direction = left
            pos = [y, x]
        elif last_direction == down:
            if y > pos[0] and x <= pos[1]:
                count += 1
                last_direction = left
            elif y <= pos[0] and x < pos[1]:
                count += 2
                last_direction = up
            else:
                count += 3
                last_direction = right
            pos = [y, x]
    return count   # 우회전 수를 반환


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    coordination = search_apple(N, arr)
    turn_count = eat_apple(coordination)

    print(f'#{tc} {turn_count}')


""" test cases
5
5
0 0 0 0 0
0 0 0 3 0
0 1 0 0 0
0 0 2 0 0
0 0 0 0 0
5
0 0 0 0 0
0 3 0 0 0
0 0 2 0 0
0 0 4 1 0
0 0 0 0 0
5
0 0 0 0 0
0 0 1 4 0
0 5 3 0 0
0 2 0 0 0
0 0 0 0 0
7
0 0 0 0 0 0 0
0 2 0 4 0 0 0
0 0 0 0 0 6 0
0 0 0 0 5 0 0
0 0 0 0 1 3 0
0 0 7 0 0 0 0
0 0 0 0 0 0 0
10
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 5 0 0 0 0
0 0 0 0 4 0 0 0 0 0
0 0 0 10 0 0 0 0 0 0
0 0 0 0 0 0 8 0 0 0
0 0 0 0 0 0 0 0 2 0
0 0 0 0 0 0 0 1 0 0
0 0 0 0 6 9 0 0 0 0
0 0 3 0 0 0 0 0 7 0
0 0 0 0 0 0 0 0 0 0

"""