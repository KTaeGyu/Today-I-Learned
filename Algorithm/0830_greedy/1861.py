for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [0] * (N*N+1)
    for i in range(N):
        for j in range(N):
            for r, c in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                if 0 <= i+r < N and 0 <= j+c < N and arr[i][j] + 1 == arr[i+r][j+c]:
                    v[arr[i][j]] = 1
    start, cnt, temp = 0, 1, 1
    for i in range(len(v) - 1, -1, -1):
        if v[i] == 1:
            temp += 1
        else:
            if cnt <= temp:
                cnt = temp
                start = i + 1
    print(f'{tc} {start} {cnt}')