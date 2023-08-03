from pprint import pprint
import sys
sys.stdin = open("input.txt", "r")

# 빙고게임
# 빙고판 먼저 주어짐 5*5
# 숫자 5개씩 주어짐
# 중간에 빙고 가능하면 핵심 숫자를 말한다.
"""
17 6 9 7 20
13 2 10 3 5
15 18 8 12 14
23 19 4 24 25
22 1 21 11 16
6 24 13 12 10
9 2 5 15 22
4 11 1 7 20
19 16 17 25 14
"""


bingo = [list(map(int, input().split())) for _ in range(5)]
# pprint(list(zip(*bingo)))
# pprint(bingo)
#
# while True:
#     calls = list(map(int, input().split()))
#     try:
#         for k in range(5):
#             for j in range(5):
#                 if calls[j] in bingo[k]:
#                     bingo[k][bingo[k].index(calls[j])] = 0
#                     for y in range(5):
#                         for x in range(5):
#                             tc = 0
#                             tem = bingo[y][x]
#                             dia1, dia2 = [], []
#                             for i in range(5):
#                                 bingo[y][x] = 0
#                                 if sum(bingo[i]) == 0:
#                                     pprint(bingo)
#                                     tc += 1
#                                 if sum(list(zip(*bingo))[i]) == 0:
#                                     pprint(bingo)
#                                     tc += 1
#                                 dia1.append(bingo[i][i])
#                                 dia2.append(bingo[i][-i-1])
#                                 bingo[y][x] = tem
#                             if sum(dia1) == 0:
#                                 pprint(bingo)
#                                 tc += 1
#                             if sum(dia2) == 0:
#                                 pprint(bingo)
#                                 tc += 1
#                             if tc > 3:
#                                 print(tem)
#                                 raise ValueError
#     except ValueError:
#         break


# 강사님 풀이
board = [int(num) for _ in range(5) for num in input().split()]
call = [int(num) for _ in range(5) for num in input().split()]
cnt = 0
print(board)
print(call)
pprint(bingo)
x_lst = [0]*10
y_lst = [0]*10
di_lst1 = [0]*10
di_lst2 = [0]*10

for n in call:
    a = board.index(n)
    x, y = a // 5, a % 5
    x_lst[x] += 1
    y_lst[y] += 1
    di_lst1[x + y] += 1
    di_lst2[y - x + 4] += 1
    if x_lst[x] == 5:
        cnt += 1
    if y_lst[y] == 5:
        cnt += 1
    if di_lst1[x + y] == 5 or di_lst2[y - x + 4] == 5:
        cnt += 1
    if cnt == 3:
        print(n)
        break
