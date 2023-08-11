"""
트리 DFS를 돌리려 한다
숫자 n과 인접 행렬을 입력 받는다.
DFS를 돌리고 탐색 순서대로 출력하라

[주의]
노드 값은 없고, 노드 번호를 출력하면 된다.
항상 0번부터 탐색한다
자식 노드가 여러개라면, 노드 번호가 작은 것부터 탐색한다.
1 <= n <= 100
노드 번호는 0~n-1번 까지 있다.

[입력]
첫 번째 줄에 노드의 수를 입력받는다.
다음 n개의 줄에 인접행렬 정보를 받는다.

각 인전행렬의 줄 번호i, 칸번호 j, 해당 위치의 값 Aij 일때
Aij가 1이면 i번 노드에서 j번 노드로 갈 수 있다는 것을 의미
"""


def dfs(graph, length):
    stack = [0]
    visited = set()

    while stack:
        now = stack.pop()
        print(now, end=' ')
        if now not in visited:
            visited.add(now)
            for i in range(length):
                if graph[now][i] == 1:
                    stack.append(i)


n = int(input())
adj = [list(map(int, input().split())) for _ in range(n)]
dfs(adj, n)

"""강사님 코드
n = int(input())
adj = [list(map(int, input().split())) for _ in range(n)]


def dfs(now):
    print(now, end=' ')
    for i in range(n):
        if adj[now][i] == 1:
            dfs(i)


dfs(0)
"""
"""
5
0 1 1 0 0
0 0 0 1 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0

0 1 3 4 2
"""