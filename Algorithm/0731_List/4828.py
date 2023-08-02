# 문제 1. 4828, min max
'''
9
7 4 2 0 0 6 0 7 0
'''
for tc in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))

    max_v = arr[0]
    min_v = arr[0]
    for i in range(1, N):
        if max_v < arr[i]:
            max_v = arr[i]
        if min_v > arr[i]:
            min_v = arr[i]
    ans = max_v - min_v

    print(f'#{tc+1} {ans}')

