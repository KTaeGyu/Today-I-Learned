def check(num):
    num = str(num)
    for i in range(len(num)-1):
        if num[i] > num[i + 1]:
            return False
    return True


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    result = 0
    for i in range(N-1):
        for j in range(i+1, N):
            number = A[i] + A[j]
            if check(number):
                result = max(result, number)
        if result == 0:
            result = -1
    print(f'#{tc} {result}')