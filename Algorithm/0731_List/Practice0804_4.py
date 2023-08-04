"""
사각형 그리기 게임에는 N x N 크기의 게임판이 주어진다.
이 게임의 목표는 최대한 면적이 큰 사각형을 몇 개 그릴 수 있는가를 구하는 것이다.

사각형을 그리는 데에는 아래 두가지 조건을 충족해야만 한다.
[1] 특정 좌표를 기준으로 "우측 하단"의 방향으로 사각형을 그릴 수 있다.
[2] 왼쪽 상단 좌표의 값과 우측 하단 좌효의 값이 동일해야 한다.

N x N 크기의 게임판이 주어졌을 때, 최대 면적의 사각형을 규칙대로 그릴 수 있는 총 사각형의 개수를 구하라.

[제약사항]
TC = 100
3 <= N <= 50
1<= 게임판의 값 <= 20

[입력]
첫번째 풀이는 테스트 케이스의 개수 T가 주어진다.
두번째 줄부터 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫번째 줄에는 게임판의 크기 N이 주어진다.
각 테스트 케이스의 두번째 줄부터 N개의 줄에 걸쳐 게임판의 각 정수가 공백으로 구현되어 N개가 주어진다.

[출력]
각 test case에 대하여 "#"와 test case의 번호 (1번부터 시작)와 공백을 둔 후, 주어진 게임맵에서 모든 사과를 순서대로 먹기 위해 필요한 최소한의 우회전의 수를 출력한다.
"""
from pprint import pprint
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    count = 0
    max_v = 0
    for i in range(N):
        for j in range(N):
            cur_no = arr[i][j]
            for y in range(i, N):
                for x in range(j, N):
                    if arr[y][x] == cur_no:
                        area = (y - i + 1) * (x - j + 1)
                        if area > max_v:
                            max_v = area
                            count = 1
                        elif area == max_v:
                            count += 1
    print(f'#{t} {count}')

# # 강사님 코드
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     MAP = [list(map(int, input().split())) for _ in range(N)]
#     maxarea = 0
#     cnt = 0
#     for y in range(N):
#         for x in range(N):
#             cur = MAP[y][x]
#             for ny in range(y, N):
#                 for nx in range(x, N):
#                     if MAP[ny][nx] == cur:
#                         area = (ny - y + 1) * (nx - x + 1)
#                         if area > maxarea:
#                             cur = 1
#                         elif area == maxarea:
#                             cnt += 1
#     print(f'#{tc} {cnt}')

"""
3
3
1 1 1
1 1 1
1 1 1
3
1 2 3
3 2 1
2 1 3
3
1 2 3
1 2 3
1 2 3

1
3
3
"""