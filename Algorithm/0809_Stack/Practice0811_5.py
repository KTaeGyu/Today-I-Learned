"""
그래프의 정보와, 탐색을 시작할 노드번호를 입력받는다.
전위 순회 및 후위 순회로 그래프를 탐색하라
탐색 순서대로 노드 번호를 출력하라

[유의 사항]
시작노드 입력값부터 탐색을 해주세요
1. 자식 노드가 여러개 일때, 노드번호가 큰 번호 우선으로 탐색합니다
2. 한번 탐색한 노드는 다시 탐색되지 않습니다.

[입력]
철 번째 줄에는 노드의 개수 N과 간선의 개수 K를 입력받아주세요
다음 줄에는 탐색을 시작할 노드번호 S를 입력받으세요

그 다움줄부터 K줄만큼 노드 간선 A,B를 입력받습니다.
A, B 는 노드 A 에서 B로 단방향 연결됨을 의미합니다.

[출력]
첫째 줄에 전위 순회, 둘째 줄에 후위 순회를 노드번호를 출력
"""
# import sys
# sys.stdin = open("input.txt", "r")

N, K = map(int, input().split())
S = int(input())
edges = []
for k in range(K):
    A, B = map(int, input().split())
    edges.append((A, B))

graph = {}
for i in range(1, N+1):
    graph[i] = []
for A, B in edges:
    graph[A].append(B)

for i in graph.keys():
    graph[i].sort(reverse=True)

postorder = []
preorder = []

visited = [0]*(N+1)
def post(v):
    visited[v] = 1
    preorder.append(v)
    for i in graph[v]:
        if visited[i] == 0:
            post(i)
    postorder.append(v)

post(S)
print(*preorder)
print(*postorder)

"""input 값들
6 5
1
1 2
1 4
2 3
4 5
4 6

1 4 6 5 2 3
6 5 4 3 2 1

5 7
1
1 3
1 4
4 1
4 5
4 3
4 2
3 5

1 4 5 3 2
5 3 2 4 1
"""













