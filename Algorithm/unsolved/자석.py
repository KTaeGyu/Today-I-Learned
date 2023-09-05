T = 10
for tc in range(1, T+1):
    N = int(input())
    mag = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for j in range(N):
        y, x = 0, j
        stack = []
        while y < N:
            if not stack and mag[y][x] == 1:
                stack.append(1)
            elif stack and mag[y][x] == 2:
                cnt += stack.pop()
            y += 1
    print(f'#{tc} {cnt}')
