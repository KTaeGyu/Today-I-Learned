"""
바이러스가 한 마을을 집어삼켰다
여기에 차르봄바라는 백신 폭탄을 떨어뜨려, 최대한 많은 바이러스를 제거하려고 한다.
차르봄바는 P 크기만큼으로 가로, 세로 방향으로 퍼져나가면서 해당 영역의 바이러스를 제거할 수 있다.
N x N 크기와 마을의 한 위치에서 차르봄바를 떨어뜨려, 가장 많은 바이러스를 제거했을 때 제거된 바이러스의 수를 구하여라

[제약사항]
3 <= N <= 100
1 <= M <= N
0 <= 각 위치의 바이러스의 개수 <= 1,000

[입력]
첫 번째 줄에는 테스트 케이스의 개수 T가 주어진다.
두번째 줄부터 각 테스트 케이스가 주어진다.
각 테스트 케이스와 첫번째 줄에는 마을의 크기N, 차르봄바의 파워 P가 공백으로 구분되어 주어진다.
각 테스트케이스의 두번째 줄부터 N개의 줄에 걸쳐 좌표의 바이러스 개수가 공백으로 구분되어 주어진다.

[출력]
각 테스트 케이스,t 에 대한 결과를 각 줄에 '#t' (테스트 케이스는 1번부터 시작)을 출력하고, 한 칸을 띄운 다음 정답을 출력한다.
"""
from pprint import pprint
import sys
sys.stdin = open("input.txt", "r")

T = int(input('테스트 케이스의 개수 T를 입력하세요: \n'))

for t in range(1, T+1):
    N, P = map(int, input('마을의 크기, N 차르봄바의 파워, P를 공백을 두고 입력하세요: \n').split())
    arr = [list(map(int, input(f'{_}번째 줄의 바이러스 개수 N개를 공백을 두고 입력하세요: \n').split())) for _ in range(N)]

    direction = [(0, -1), (0, 1), (1, 0), (-1, 0)]

    max_kill = 0
    for y in range(N):
        for x in range(N):
            kill_count = arr[y][x]
            for p in range(1, P + 1):
                for dy, dx in direction:
                    ny = y + (dy * p)
                    nx = x + (dx * p)
                    if 0 <= ny < N and 0 <= nx < N:
                        kill_count += arr[ny][nx]
            if max_kill < kill_count:
                max_kill = kill_count
    print(f'#{t} {max_kill}')

"""
4
7 3
1 8 1 4 2 5 1
1 5 2 6 7 2 3
7 9 5 5 1 9 8
3 7 0 9 8 0 7
5 5 3 9 5 1 4
2 5 9 3 3 6 8
0 1 4 1 8 4 0
7 2
3 3 8 8 5 5 0
4 3 9 6 0 2 5
0 8 6 2 0 3 8
5 1 0 8 2 9 6
1 7 5 3 9 2 0
8 4 2 9 5 5 3
2 3 6 2 9 1 4
5 3
9 3 0 4 0
3 9 4 0 4
0 4 9 4 0
4 0 4 9 3
0 4 0 3 9
5 4
1 2 3 4 9
2 3 4 5 9
3 4 5 6 9
4 5 6 7 9
9 9 9 9 9

[결과]
75
47
40
81
"""