"""
트리 자료구조에서 너비 우선 탐색법으로 각 노드를 탐색해주세요.
시작 지점 부터, 노드에 방문할 때마다 값을 출력 해주세요.
출발지점은 입력으로 주어 집니다.
한번 방문 했던 노드는 방문할 수 없습니다.
트리 자료구조는 인접행렬로 하드코딩 해주세요.

[트리]
0: [1, 4], 1: [2, 5], 2:[3], 3: [], 4: [], 5: []
"""
import sys
sys.stdin = open("input.txt", "r")

k = int(input())
graph = {0: [1, 4], 1: [2, 5], 2: [3], 3: [], 4: [], 5: []}
n = 0
m = 0
for key in graph.keys():
    n += len(graph[key])
    m += 1

def BFS(start):
    queue = [0]*(n+1)
    front = -1
    rear = -1
    visited = [0]*(m + 1)

    rear += 1
    queue[rear] = start
    visited[start] = 1
    while front != rear:
        front += 1
        now = queue[front]
        print(now, end=" ")
        for i in graph[now]:
            if visited[i] == 0:
                visited[i] = 1
                rear += 1
                queue[rear] = i


BFS(k)

"""
0
"""