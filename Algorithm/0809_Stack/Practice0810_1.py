"""
8개의 알파벳으로 구성된 문자열과 대응되는 인접 행렬을 입력받아주세요,
아래 이미지는 입력 에시에 해당하는 트리입니다.
0번 알파벳부터 DFS로 노드들을 탐색하면서 출력해주세요

[입력]
첫번째에 8개의 알파벳으로 이루어진 문자열이 주어집니다.
이어지는 8개의 줄에 걸쳐 인접행렬에 대한 정보가 주어집니다.

각 인접 행렬의 줄 번호 i, 칸 번호 j, 해당 위치의 값 Aij라고 할 때 Aij가 1이면 i번 알파벳에서 j번 알파벳으로 갈 수 있다는 것을 의미합니다.

[출력]
첫 알파벳 부터 시작하여 DFS로 탐색하였을 때, 방문한 노드들을 순서대로 출력합니다.
단, 한 알파벳에서 탐색 가능한 알파벳이 여럿 있다면 입력받은 순서가 빠른 알파벳부터 탐색합니다.
"""
import sys
from pprint import pprint
sys.stdin = open("input.txt", "r")


def dfs(node_arr):
    stack = [0]
    visited = []

    while stack:
        node = stack.pop()
        print(string[node], end="")
        if node not in visited:
            visited.append(node)

            for j in range(7, -1, -1):
                if node_arr[node][j] == 1 and j not in visited:
                    stack.append(j)


string = input()
arr = [list(map(int, input().split())) for _ in range(8)]

dfs(arr)

"""강사님 코드
lst = list(input())
N = len(lst)
adj = [list(map(int, input().split())) for _ in range(N)]
visited = [False for _ in range(N)]

def dfs(v):
    print(lst[v], end="")
    visited[v] = True

    for i in range(N):
        if adj[v][i] and not visited[i]:
            dfs(i)

def(0)
"""

"""
RKFCBICM
0 1 1 1 0 0 0 0
0 0 0 0 1 1 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 1
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0

RKBIFCCM
"""