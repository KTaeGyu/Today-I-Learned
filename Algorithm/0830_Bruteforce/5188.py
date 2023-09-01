import sys
sys.stdin = open("input.txt", "r")


def dfs(i, n, y, x):
    global ans
    ans += arr[y][x]
    if i == 2 * n:
        global result
        if result > ans:
            result = ans
        ans -= arr[y][x]
        return
    else:
        if y < n:
            dfs(i + 1, n, y + 1, x)
        if x < n:
            dfs(i + 1, n, y, x + 1)
        ans -= arr[y][x]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    result = float('inf')
    dfs(0, N-1, 0, 0)
    print(f'#{tc} {result}')

"""
dir = [(0, 1), (1, 0)]

def dfs(x, y, sum_v):
    global result
    if sum_v >= result:
        return
    if x == N - 1 and y == N - 1:
        if sum_v < result:
            result = sum_v
        return
    for dx, dy in dir:
        ny, nx = x + dx, y + dy
        if 0 <= ny < N and 0 <= nx < N:
            dfs(nx, ny, sum_v + arr[ny][nx])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = float('inf')
    dfs(0, 0, arr[0][0])
    print(f'#{tc} {result}')
"""