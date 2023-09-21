import sys
sys.stdin = open("../input.txt", "r")


def find(x):
    if parents[x] == x:
        return parents[x]
    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x > y:
        parents[x] = y
    else:
        parents[y] = x


N, Q = map(int, input().split())
parents = [i for i in range(N+1)]
for q in range(Q):
    K, A, B = map(int, input().split())
    if K:
        union(A, B)
    else:
        r1, r2 = find(A), find(B)
        print('YES' if r1 == r2 else 'NO')
