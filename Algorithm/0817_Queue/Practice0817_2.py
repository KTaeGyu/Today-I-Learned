"""
아래에 그래프가 놓여져 있습니다.
입력 받은 출발 지점에서 너비 우선 탐색법으로 그래프를 탐색해주세요.
한번 방문했던 노드는 다시 방문할 수 없습니다.
시작 지점부터 BFS가 끝날때까지 방문한 노드를 출력해주세요.

[그래프]
0 : [4]
1 : [0, 2, 5]
2 : [0, 3]
3 : [0, 1]
4 : [1, 3]
5 : [2, 3]

BFS를 시작할 노드번호를 입력받습니다.

입력받은 노드를 시작으로 BFS의 순서로 방문한 노드번호들을 출력합니다.
단, BFS의 순서로 갈 수 있는 방법이 여러가지인 경우 작은 노드번호를 먼저 방문하는 방법으로 출력합니다.
"""
import sys
sys.stdin = open("input.txt", "r")

s = int(input())
graph = {0: [4], 1: [0, 2, 5], 2: [0, 3], 3: [0, 1], 4: [1, 3, 5], 5: [2, 3]}
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
        print(now)
        for i in graph[now]:
            if visited[i] == 0:
                visited[i] = 1
                rear += 1
                queue[rear] = i


BFS(s)


"""
0
"""