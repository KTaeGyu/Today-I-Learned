# import sys
# sys.stdin = open("input.txt", "r")
from pprint import pprint
from copy import deepcopy


blank = '_'
board_range = 15
plate = [[blank]*board_range for _ in range(board_range)]
for dx in range(board_range):
    plate[dx].append(dx % 10)
dy = list(range(board_range))
for i in range(board_range):
    dy[i] = dy[i] % 10
plate.append(dy)
judge = [[(-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0)],    # strip
         [(0, -2), (0, -1), (0, 0), (0, 1), (0, 2)],    # rank
         [(-2, -2), (-1, -1), (0, 0), (1, 1), (2, 2)],  # dia_1
         [(-2, 2), (-1, 1), (0, 0), (1, -1), (2, -2)],  # dia_2
         [(-3, 0), (3, 0)],                             # over_strip
         [(0, -3), (0, 3)],                             # over_rank
         [(-3, -3), (3, 3)],                            # over_dia_1
         [(-3, 3), (3, -3)]]                            # over_dia_2


def white():
    while True:
        try:
            y, x = map(int, input().split())
            if x < 0 or x >= board_range or y < 0 or y >= board_range:
                print('오목 판을 벗어났습니다.')
                raise ValueError
            elif plate[y][x] == blank:
                plate[y][x] = 1
                break
            else:
                print('다른 돌 위에 두셨습니다.')
                raise ValueError
        except ValueError:
            continue
    for line in plate:
        print(*line, sep=' ')
    print()


def black():
    while True:
        try:
            y, x = map(int, input().split())
            if x < 0 or x >= board_range or y < 0 or y >= board_range:
                print('오목 판을 벗어났습니다.')
                raise ValueError
            elif plate[y][x] == blank:
                plate[y][x] = 2
                break
            else:
                print('다른 돌 위에 두셨습니다.')
                raise ValueError
        except ValueError:
            continue
    for line in plate:
        print(*line, sep=' ')
    print()


def judgement():
    ww = False
    bw = False
    is_break = False
    for std in range(4):
        for i in range(board_range):
            for j in range(board_range):
                wc = 0
                bc = 0
                for k in range(5):
                    ni = i + judge[std][k][0]
                    nj = j + judge[std][k][1]
                    if 0 <= ni < board_range and 0 <= nj < board_range:
                        if plate[ni][nj] == 1:
                            wc += 1
                        if plate[ni][nj] == 2:
                            bc += 1
                if wc == 5 or bc == 5:
                    is_ok = True
                    for k2 in range(2):
                        ci = i + judge[std+4][k2][0]
                        cj = j + judge[std+4][k2][1]
                        if wc == 5 and 0 <= ci < board_range and 0 <= cj < board_range and plate[ci][cj] == 1:
                            is_ok = False
                        if bc == 5 and 0 <= ci < board_range and 0 <= cj < board_range and plate[ci][cj] == 2:
                            is_ok = False
                    if is_ok:
                        if wc == 5:
                            return 1
                        if bc == 5:
                            return 2
    return 0


def play():
    winner = 0
    while winner == 0:
        black()
        winner = judgement()
        if winner == 2:
            print('흑돌 승 ', end=' ')
            break

        white()
        winner = judgement()
        if winner == 1:
            print('백돌 승 ', end=' ')
            break

    print('게임을 종료합니다.')


play()

