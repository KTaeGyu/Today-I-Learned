import sys
sys.stdin = open("input.txt", "r")


def combination(n, m):
    if n < 0:
        return
    elif m <= 0:
        ans = 1
        for a in choice:
            ans *= a
        global min_v
        global result
        if min_v > ans:
            min_v = ans
            result = choice.copy()
        return
    else:
        choice[m-1] = arr[n-1]
        combination(n-1, m-1)
        combination(n-1, m)


N, M = map(int, input().split())
arr = list(map(int, input().split()))
choice = [0]*M
result = []
min_v = float('inf')
combination(N, M)
print(*sorted(result))
