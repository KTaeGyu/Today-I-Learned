from pprint import pprint
import sys
sys.stdin = open("input.txt", "r")
"""
3 5
2
_#_#@
_#_#@
@___#
"""

# # 폭발 함수
# def bomb(y, x, k):
#     for n in range(1, k+1):
#         di = [n, n, -n, -n, n, 0, -n, 0]
#         dj = [n, -n, n, -n, 0, n, 0, -n]
#         if arr[y][x] == 'w':
#             print('벽에는 폭탄을 둘 수 없습니다.')
#         else:
#             arr[y][x] = '#'
#             for m in range(8):
#                 ni = y + di[m]
#                 nj = x + dj[m]
#                 if 0 <= ni < 3 and 0 <= nj < 5 and arr[ni][nj] != 'W':
#                     arr[ni][nj] = '#'
#
#
# # 배열 생성
# N, M = int(input('배열의 크기(행, 열)를 입력하세요: '))
# arr = [['0']*M for _ in range(N)]
# arr[0][1] = arr[0][3] = arr[1][1] = arr[1][3] = 'W'
#
# # 폭탄 관련
# bomb_range = int(input('폭탄 화력을 입력하세요: '))
# bomb_num = int(input('폭탄 수를 입력하세요: '))
# for i in range(bomb_num):
#     row, col = map(int, input('폭탄 위치(행, 열)를 입력하세요: ').split())
#     bomb(row, col, bomb_range)
#
#
# pprint(arr)

# # 다른 방법
N, M = map(int, input('배열의 크기(행, 열)를 입력하세요: ').split())
bomb_range = int(input('폭탄 화력을 입력하세요: '))
arr = [list(input()) for _ in range(N)]
ly = [(1, 0), (-1, 0), (0, 1), (0, -1)]
print(arr)


def bomb(k):
    for y in range(N):
        for x in range(M):
            if arr[y][x] == '@':
                for dy, dx in ly:
                    for r in range(1, k+1):
                        ny = y + (dy*r)
                        nx = x + (dx*r)
                        if 0 <= ny < N and 0 <= nx < M:
                            if arr[ny][nx] == '_':
                                arr[ny][nx] = '%'
                            elif arr[ny][nx] == '#' or '@':
                                break
                arr[y][x] = '%'


bomb(bomb_range)
print('\n')
pprint(arr)


# 강사님 풀이
# N, M = map(int, input('배열의 크기(행, 열)를 입력하세요: ').split())
# bomb_range = int(input('폭탄 화력을 입력하세요: '))
# arr = [list(input()) for _ in range(N)]
# ly = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#
#
# def bomb2(directions, br):
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] == '@':
#                 for dy, dx in directions:
#                     for k in range(1, br + 1):
#                         ny, nx = i + (k * dy), j + (k * dx)
#                         if 0 <= ny < N and 0 <= nx < M:
#                             if arr[ny][nx] == '_':
#                                 arr[ny][nx] = '%'
#                             if arr[ny][nx] == '#' or '@':
#                                 break
#                 arr[i][j] = '%'
#     for row in arr:
#         print()
#         print(*row, sep='')
#
# bomb2(ly, bomb_range)
