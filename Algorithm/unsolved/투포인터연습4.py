T = int(input())
for tc in range(1, T+1):
    n, r = map(int, input().split())
    foods = list(map(int, input().split()))
    arr = foods * 2
    DAT = [0] * 201

    start = 0
    end = 2 * r
    flag = 0

    for k in range(start, end):
        DAT[arr[k]] += 1
        if DAT[arr[k]] > 1:
            flag = 1
            break

    while end < 2 * n and flag == 0:
        DAT[arr[end]] += 1
        if DAT[arr[end]] > 2:
            flag == 1
            break
        DAT[arr[start]] -= 1
        start += 1
        end += 1
    if flag == 1:
        print(f'#{tc} NO')
    else:
        print(f'#{tc} YES')
