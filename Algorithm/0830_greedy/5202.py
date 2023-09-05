import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    se = [list(map(int, input().split())) for _ in range(N)] + [[25, 25]]
    se.sort(key=lambda x: x[1])
    se2 = list(zip(*se))
    cnt = 0
    idx = 0
    while True:
        s, e = se[idx]
        if s == 25:
            break
        cnt += 1
        for i in range(idx, N+1):
            if se2[0][i] >= e:
                idx = i
                break
    print(f'#{tc} {cnt}')


"""
3
5
20 23
17 20
23 24
4 14
8 18
10
14 23
2 19
1 22
12 24
21 23
6 15
20 24
1 4
6 15
15 16
15
18 19
2 7
11 15
13 16
23 24
2 14
13 22
20 23
13 19
7 15
5 21
20 24
16 22
17 21
9 24

#1 4
#2 4
#3 5
"""