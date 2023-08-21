"""
사각형 그리기 게임에는 N x N 크기의 게임판이 주어진다. 
이 게임의 목표는 최대한 면적이 큰 사각형을 몇 개 그릴 수 있는가?를 구하는 것이다. 

사각형을 그리는 데에는 아래 두가지 조건을 충족해야만 한다. 
[1] 특정 좌표를 기준으로, "우측 하단"의 방향으로 사각형을 그릴 수 있다. 
[2] 왼쪽 상단 좌표의 값과 우측 하단 좌표의 값이 동일해야 한다. 

N x N 크기의 게임판이 주어졌을 때, 최대 면적의 사각형을 규칙대로 그릴 수 있는 총 사각형의 개수를 구하라. 

[제약사항] 
    TC = 100 
    3 <= N <= 50
    1 <= 게임판의 값 <= 20

입력
첫번째 줄에는 테스트 케이스의 개수 T가 주어진다. 
두번째 줄부터 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫번째 줄에는 게임판의 크기 N이 주어진다.
각 테스트 케이스의 두번째 줄부터 N개의 줄에 걸쳐 게임판의 각 정수가 공백으로 구분되어 N개가 주어진다.

출력
각 테스트 케이 t에 대한 결과를 각 줄에 "#t" (테스트 케이스는 1번부터 시작)을 출력하고, 한 칸을 띄운 다음 정답을 출력한다. 
"""
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    max_w = 0
    cnt = 0
    for y in range(N):
        for x in range(N):
            for ny in range(y, N):
                for nx in range(x, N):
                    if board[y][x] == board[ny][nx]:
                        now_w = (ny - y + 1) * (nx - x + 1)
                        if max_w < now_w:
                            max_w = now_w
                            cnt = 1
                        elif max_w == now_w:
                            cnt += 1
    print(f'#{tc} {cnt}')

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

#1 1
#2 3
#3 3
"""