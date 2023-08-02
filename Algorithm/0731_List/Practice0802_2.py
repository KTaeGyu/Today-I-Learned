from pprint import pprint

arr = [['_']*5 for _ in range(4)]

di = [1, 1, -1, -1, 1, 0, -1, 0]
dj = [1, -1, 1, -1, 0, 1, 0, -1]

bomb_num = int(input())


def bomb(y, x):
    for k in range(8):
        ni = y + di[k]
        nj = x + dj[k]
        if 0 <= ni < 4 and 0 <= nj < 5:
            arr[ni][nj] = '#'


for i in range(bomb_num):
    row, col = map(int, input().split())
    bomb(row, col)

pprint(arr)
