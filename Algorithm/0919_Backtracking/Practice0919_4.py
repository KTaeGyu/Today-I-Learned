def dfs(idx, sum_v):
    global answer
    if answer < sum_v:
        return
    if idx >= N:
        answer = sum_v
        return
    for i in range(count, 0, -1):
        dfs(idx+i, sum_v+1)
T = int(input())
for tc in range(1, T+1):
    answer = float('inf')
    station = list(map(int, input().split()))
    N = station.pop(0)
    dfs(0, -1)
    print(f'#{tc} {answer}')
