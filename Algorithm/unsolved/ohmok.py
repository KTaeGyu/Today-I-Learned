T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    direction = [(0, 1), (1, 0), (1, 1), (-1, 1)]
    result = 'NO'
    try:
        for y in range(N):
            for x in range(N):
                if arr[y][x] == 'o':
                    for dy, dx in direction:
                        for i in range(5):
                            ny, nx = y + dy * i, x + dx * i
                            if 0 <= ny < N and 0 <= nx < N:
                                if arr[ny][nx] == '.':
                                    break
                            else:
                                break
                        else:
                            result = 'YES'
                            raise ValueError
    except ValueError:
        pass
    print(f'#{tc} {result}')






"""
def rule():
    direction = [(1, 0), (0, 1), (1, 1), (-1, 1)]
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 'o':
                for d in range(4):
                    ny, nx = y, x
                    cnt = 0
                    while 0 <= ny < N and 0 <= nx < N and arr[ny][nx] == 'o':
                        cnt += 1
                        ny += direction[d][0]
                        nx += direction[d][1]
                    if cnt >= 5:
                        return 'YES'
    return 'NO'


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    print(f'#{tc} {rule()}')
"""
