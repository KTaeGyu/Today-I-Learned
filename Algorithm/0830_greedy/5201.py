import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    wi = list(map(int, input().split()))
    ti = list(map(int, input().split()))

    wi.sort(reverse=True)
    ti.sort(reverse=True)

    result = 0

    s = 0
    for i in range(M):
        for j in range(s, N):
            if ti[i] >= wi[j]:
                result += wi[j]
                s = j+1
                break

    print(f'#{tc} {result}')

"""
3
3 2
1 5 3
8 3
5 10
2 12 13 11 18
17 4 7 20 3 9 7 9 20 5
10 12
10 13 14 6 19 11 5 20 11 14
5 18 17 8 9 17 18 4 1 16 15 13

#1 8
#2 45
#3 84
"""