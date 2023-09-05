from collections import deque

T = int(input())
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(M):
            s = deque([(i, j, 0)])
            v = {(i, j)}
            while s:
                y, x, level = s.popleft()
                if arr[y][x] == 'W':
                    result += level
                    break
                else:
                    for dy, dx in direction:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < N and 0 <= nx < M and (ny, nx) not in v:
                            v.add((ny, nx))
                            s.append((ny, nx, level + 1))
    print(f'#{tc} {result}')