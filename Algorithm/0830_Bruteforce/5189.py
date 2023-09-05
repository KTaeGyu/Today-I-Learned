import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = float('inf')
    for i in range(1, N):
        sum_v = arr[0][i]
        for j in range(1, N):
            sum_v += arr[j][(i+j) % N]
        if result > sum_v:
            result = sum_v
    print(result) # 실패







"""
# 강사님 풀이
def cart(cur, start, total):
    global result
    if cur == n - 1:
        result = min(result, arr[start][0] + total)
        return
    for i in range(1, n):
        if visited[i] == 0 and start != i:
            visited[i] = 1
            cart(cur + 1, i, total + arr[start][i])
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0 for _ in range(n)]
    result = float('inf')
    cart(0, 0, 0)
    print(f'#{tc} {result}')
"""