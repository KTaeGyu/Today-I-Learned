from collections import deque
dir = [(0, 1), (-1, 0), (0, 1), (1, 0)]
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    check = [[-1 for _ in range(M)] for _ in range(N)]
    q = deque()

    for i in range(N):
        t = input()
        for j in range(M):
            if t[j] == 'W':
                q.append((i, j))
                check[i][j] = 0

    result = 0
    while q:
        x, y = q.popleft()
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and check[nx][ny] == -1:
                q.append((nx, ny))
                check[nx][ny] = check[x][y] + 1
                result += check[nx][ny]
    
