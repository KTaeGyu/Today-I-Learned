"""
N x N 사각형의 전투장에는 각 칸마다 몇 마리의 몬스터가 있는 지 적혀있다.
광대한 영영게 마법을 시전할 수 있는 마법사 mort는 전투장에서 최대한 많은 몬스터를 잡으려한다.

대각선 방향으로 각 방향마다 K 칸 만큼 마법을 시전할 수 있다.
마법은 마법사가 있는 지점에서 마법을 시전할 위치를 제외하고 대각선 방향으로 변화없이 시전된다

한번에 처치 가능한 최애 몬스터 수는?
입력:
5
1 2 3 5 10
9 7 2 2 9
0 0 1 5 7
5 2 3 2 2
1 1 1 1 1
2

첫째줄에 전투장의 가로세로크기인 N이 입력된다
다음 줄 부터는 N 줄에 걸쳐 각 줄마다 N 개의 정수가 공백으로 구분되어 입력된다
마지막 줄에는 마법의 시전범위 K가 입력된다.

잡을 수 있는 최대 몬스터 수를 출력한다.
"""
from pprint import pprint
import sys
sys.stdin = open("input.txt", "r")

N = int(input('전투장의 가로세로 크기, N을 입력하세요: \n'))
arr = [list(map(int, input(f'{_} 번째 행의 몬스터 수를 입력하세요: \n').split())) for _ in range(N)]
K = int(input('마법의 시전범위,K 를 입력하세요: \n'))

direction = [(-1, -1), (-1, 1), (1, 1), (1, -1)]

max_kill = 0
for y in range(N):
    for x in range(N):
        kill_count = 0
        for k in range(1, K+1):
            for dy, dx in direction:
                ny = y + (dy * k)
                nx = x + (dx * k)
                if 0 <= ny < N and 0 <= nx < N:
                    kill_count += arr[ny][nx]
        if max_kill < kill_count:
            max_kill = kill_count
print(max_kill)
