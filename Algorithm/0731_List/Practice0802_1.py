# [입력]
"""
5
3 3 5 3 1
2 2 4 2 6
4 9 2 3 4
1 1 1 1 1
3 3 5 9 2
"""

import sys
sys.stdin = open("input.txt", "r")

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]


def cross_sum(arr):
    di = [1, 1, -1, -1]
    dj = [1, -1, 1, -1]
    max_v = 0
    max_row = None
    max_col = None
    for i in range(N):
        for j in range(N):
            s = arr[i][j]
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    s += arr[ni][nj]
            if max_v < s:
                max_v = s
                max_row = i
                max_col = j
    return max_row, max_col


print(cross_sum(arr))
