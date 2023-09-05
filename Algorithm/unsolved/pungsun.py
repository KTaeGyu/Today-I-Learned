def solve(i, n):
    if i == n:
        arr = [1] + B.copy() + [1]
        score = 0
        for a in A:
            if len(arr) == 3:
                score += arr[1]
                global result
                if result < score:
                    result = score
                break
            idx = arr.index(a, 1, n+1)
            score += arr[idx - 1] * arr[idx + 1]
            arr.pop(idx)
    else:
        for j in range(i, n):
            A[i], A[j] = A[j], A[i]
            solve(i+1, n)
            A[i], A[j] = A[j], A[i]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    B = A.copy()
    result = 0
    solve(0, N)
    print(f'#{tc} {result}')