"""
NxN 배열에 숫자가 들어있다. 한 줄에서 하나씩 N개의 숫자를 골라 합이 최소가 되도록 하려고 한다. 단, 세로로 같은 줄에서 두 개 이상의 숫자를 고를 수 없다.
조건에 맞게 숫자를 골랐을 때의 최소 합을 출력하는 프로그램을 만드시오.
예를 들어 다음과 같이 배열이 주어진다.
2 1 2
5 8 5
7 2 2
이경우 1, 5, 2를 고르면 합이 8로 최소가 된다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스의 첫 줄에 숫자 N이 주어지고, 이후 N개씩 N줄에 걸쳐 10보다 작은 자연수가 주어진다. 3≤N≤10

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 합계를 출력한다.
"""
import sys
sys.stdin = open("input.txt", "r")


def min_add(i, n, s):
    global min_v
    if i == n:
        if min_v > s:
            min_v = s
        return
    elif s >= min_v:
        return
    else:
        for j in range(i, n):
            A[i], A[j] = A[j], A[i]
            min_add(i + 1, n, s + arr[i][A[i]])
            A[i], A[j] = A[j], A[i]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    A = []
    for m in range(N):
        A.append(m)
    min_v = float('inf')
    min_add(0, N, 0)
    print(f'#{tc} {min_v}')

"""강사님 풀이
def DFS(idx, now_sum):
    global min_sum
    if now_sum >= min_sum:  # 현재 합이 최소 합보다 크면 더이상 탐색 x
        return
    if idx == N:    # 모든 행을 선택
        if min_sum > now_sum:   # 모든 행을 선택 했으면 현재합이 최소합보다 작으면 최소합을 현재합으로 업데이트
            min_sum = now_sum
            return
    for i in range(N):
        if not used[i]:
            used[i] = 1
            DFS(idx + 1, now_sum + arr[idx][i])     # 행을 다음행으로 넘어가면서 재귀호출
            used[i] = 0     # 복구(백트래킹)


T= int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * N
    min_sum = 21e8
    DFS(0, 0)
    print(f'#{tc} {min_sum}')
"""

"""
3
3
2 1 2
5 8 5
7 2 2
3
9 4 7
8 6 5
5 3 7
5
5 2 1 1 9
3 3 8 3 1
9 2 8 8 6
1 5 7 8 3
5 5 4 6 8

#1 8
#2 14
#3 9
"""