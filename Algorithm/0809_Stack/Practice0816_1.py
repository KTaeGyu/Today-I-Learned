"""
다빈치 민코드 게임은 1 : 1 로 대결하는 보드게임입니다.
이 게임에는 N개의 패가 등장합니다.
다음 그림은 7개의 패가 놓여진 상태입니다.
각 패에는 -9 ~ 9 사이의 수가 적혀있습니다.

1 5 4 -2 6 7 -1

여러개의 패 중, 상대에게 M개의 패를 전달해 주어야 합니다.
M개의 패에 적혀있는 수들의 곱이 최소값이 되면, 나의 승리가 됩니다.
M이 3일때, 다음 그림과 같이 -2, 6, 7 패를 선택하면 곱이 -87로 최소값이 되어 나의 승리가 됩니다.

1 5 4 (-2 6 7) -1

상대의 곱이 최소패가 되도록 하려면,
어떤 패들을 주어야하는지오름차순으로 순서대로 출력해 주세요.

패의 개수 N과 뽑아야 하는 개수 M 이 입력 됩니다. (3 <= M < N <= 40)
그 다음 줄에는 패에 적혀있는 수들이 입력 됩니다.

M개의 곱이 최소값이 되기 위해 선택해야 하는 패의 종류를
오름차순 순서대로 출력합니다.
"""
import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
cards = list(map(int, input().split()))
visited = [0]*N
combination = []
min_v = float('inf')
result = []


def min_multi(i, m, s):
    global min_v, result
    if i == m:
        print(combination)
        if min_v > s:
            min_v = s
            result = combination.copy()
        return
    else:
        for k in range(N):
            if visited[k] == 0:
                combination.append(cards[k])
                visited[k] = 1
                min_multi(i+1, m, s*cards[k])
                combination.pop()
                visited[k] = 0


min_multi(0, M, 1)
result.sort()
print(*result)
# 아니 이게 왜안되지?
"""강사님 풀이
import copy
N, M = int(input())
lst = list(map(int, input().split()))
path = []
used = [0]*N
Min = float('inf')
result = []


def DFS(level, Sum):
    global Min, path, result
    if level == M:
        if Sum < Min:
            Min = Sum
            result = copy.deepcopy(path)
        return

    for i in range(N):
        if used[i] == 1:
            continue
        path.append(lst[i])
        used[i] = 1
        DFS(level + 1, Sum * lst[i])
        used[i] = 0
        path.pop()

DFS(0, 1)
result.sort()
print(*result)
"""
"""
7 3
1 5 4 -2 6 7 -1

-2 6 7
"""