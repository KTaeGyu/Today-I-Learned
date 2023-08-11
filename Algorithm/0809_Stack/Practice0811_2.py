"""
N x N 인접행렬 트리를 입력받는다
0번 노드에서부터 DFS로 탐색하여 레벨 2에 도착할 때마다 경로를 출력하면 된다.

[입력]
첫 번째에 노드의 갯수 n이 주어진다.
이어지는 n개의 줄에 걸쳐 인접행렬에 대한 정보가 주어진다.

각 인전행렬의 줄 번호i, 칸번호 j, 해당 위치의 값 Aij 일때
Aij가 1이면 i번 노드에서 j번 노드로 갈 수 있다는 것을 의미

[출력]
level2에 도착할 때마다 탐색 경로를 출력
"""
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


def dfs(graph, length):
    stack = [(0, 0, [0])]
    visited = set()

    while stack:
        print(stack)
        now, level, previous = stack.pop()
        if level == 2:
            print(*previous)
        if now not in visited:
            visited.add(now)
            for i in range(length-1, -1, -1):
                if graph[now][i] == 1:
                    n_previous = previous.copy()
                    n_previous.append(i)
                    stack.append((i, level + 1, n_previous))


dfs(arr, n)

"""강사님 풀이
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0]*3


def DFS(now, level):
    global visited
    visited[level] = str(now)
    if level == 2:
        print(' '.join(visited))
    for i in range(N):
        if arr[now][i] == 1:
            DFS(i, level + 1)


DFS(0, 0)
"""

"""
9
0 1 1 0 0 0 0 0 0
0 0 0 1 1 1 0 0 0
0 0 0 0 0 0 1 1 1
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0

0 1 3
0 1 4
0 1 5
0 2 6
0 2 7
0 2 8
"""