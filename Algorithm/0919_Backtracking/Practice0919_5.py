def func(cur, total):
    global min_v
    if total > min_v:
        return
    if cur == n:
        min_v = min(min_v, total)
        return
    for i in range(n):
        if visited[i] == 1:
            continue
        visited[i] = 1
        func(cur+1, total+arr[cur][i])
        visited[i] = 0
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0 for _ in range(n)]
    min_v = float('inf')
    func(0, 0)
    print(f'#{tc} {min_v}')