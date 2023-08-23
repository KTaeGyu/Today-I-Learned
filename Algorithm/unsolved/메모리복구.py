T = int(input())
for tc in range(1, T+1):
    cnt = 0
    now = '0'
    num = input()
    for i in range(len(num)):
        if num[i] != now:
            cnt += 1
            now = num[i]
    print(f'#{tc} {cnt}')