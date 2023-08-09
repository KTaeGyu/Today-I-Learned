"""
3 5 1 9 7
위 배열을 하드코딩 해주세요
그리고 R 또는 L 문자 4개를 입력받습니다.
R 은 right 방향을 의미하고
L 은 left 방향을 의미합니다.

아래 그림과 같이
R을 입력받으면 숫자를 오른쪽으로 한 칸씩 모두이동시키는데, 맨 뒤에 있는 숫자는맨 앞으로 와야합니다.
L을 입력받으면 숫자를 왼쪽으로 한 칸씩 모두이동시키는데, 맨 앞에 있는 숫자는 맨 뒤로 보내야합니다.
R또는 L을 4번 입력받은 후 처리된 결과를 출력해주세요
"""
import sys
sys.stdin = open("input.txt", "r")


def right(array):
    array.insert(0, array.pop())


def left(array):
    array.append(array.pop(0))


arr = [3, 5, 1, 9, 7]

for i in range(4):
    RL = input()
    if RL == 'R':
        right(arr)
    if RL == 'L':
        left(arr)

print(*arr)
