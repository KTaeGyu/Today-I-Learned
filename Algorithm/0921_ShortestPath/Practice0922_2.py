"""
N : 노드 수
M : 간선 수
n1, n2 : 두 노드 연결

형성된 그룹 수는?
"""
import sys
sys.stdin = open("../input.txt", "r")


def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x < y:
        parents[y] = x
    elif y < x:
        parents[x] = y


T = int(input())
for tc in range(1, T+ 1):
    N, M = map(int, input().split())
    parents = [i for i in range(N + 1)]

    for m in range(M):
        n1, n2 = map(int, input().split())
        union(n1, n2)
    for n in range(1, N+1):
        find(n)

    result = len(set(parents))
    print(f'#{tc} {result-1}')