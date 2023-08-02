# 버블정렬 구현
for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    print(f'#{tc}', arr)