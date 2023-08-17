"""
원형시계가 있습니다.
몇도 돌릴것인지 90도의 배수로 입력받아주세요.
그리고 시계를 시계방향으로 돌리고, 그 결과를 출력하세요.

입력
첫 번째 줄에 회전시킬 각도 K가 주어집니다.

출력
원형 시계를 K만큼 회전시켰을 때 시계의 숫자들을위, 왼쪽, 오른쪽, 아래순서로 출력합니다.
"""
import sys
sys.stdin = open("input.txt", "r")

K = int(input()) // 90
clock = [3, 6, 9, 12]
order = [3, 2, 0, 1]
for i in range(K):
    clock.insert(0, clock.pop())

for i in order:
    print(clock[i], end=' ')

"""
180

6 3 9 12
"""
