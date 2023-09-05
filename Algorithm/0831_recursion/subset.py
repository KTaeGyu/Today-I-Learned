import sys
sys.stdin = open("input.txt", "r")


def combination(i, n):
    global add
    global cnt
    if sum(add) == S:
        cnt += 1
    elif i >= n:
        return
    else:
        add.append(arr[i])
        combination(i+1, n)
        add.remove(arr[i])
        combination(i+1, n)


T = int(input())
for tc in range(1, T+1):
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    add = []
    combination(0, N)
    print(f'#{tc} {cnt}')
