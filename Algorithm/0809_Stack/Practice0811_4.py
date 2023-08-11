"""
신종 바이러스인 웜 바이러스는 네트워크를 통해 전파됩니다.
한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸린다.

예를 들어 7대의 컴퓨터가 다음과 같이 연결되어있으면 1번 컴퓨터는 2, 5, 3, 6 컴퓨터를 감염시킨다.
그러나 4, 7번 컴퓨터는 영향을 받지 않는다.
1 2
2 3
1 5
5 2
5 6
4 7

어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다.
컴퓨터 수와 연결 정보가 주어질 때, 1번 컴퓨터에 의해 감염되는 컴퓨터 수를 구하라

[입력]
첫째 줄에는 컴퓨터의 수가 주어진다(100 이하, 1번부터 차례대로 번호)
둘째 줄에는 연결되어 있는 컴퓨터 수가 주어진다
이어서 그 수만큼 연결된 번호 쌍이 주어진다.

[출력]
1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터 수를 출력
"""
import sys
sys.stdin = open("input.txt", "r")

N = int(input())
M = int(input())
edges = []
for m in range(M):
    c1, c2 = map(int, input().split())
    edges.append((c1, c2))

graph = {}
for i in range(1, N+1):
    graph[i] = []
for c1, c2 in edges:
    graph[c1].append(c2)
    graph[c2].append(c1)

stack = [1]
visited = []

while stack:
    now = stack.pop()
    if now not in visited:
        visited.append(now)
        for i in graph[now]:
            stack.append(i)
            
print(len(visited)-1)

"""강사님 풀이1
N = int(input())
M = int(input())
arr = [[0] * N for _ in range(N)]
visited = [0] * N
for _ in range(M):
    c1, c2 = map(int, input().split())
    arr[c1-1][c2-1] = arr[c2-1][c1-1] = 1
    
def DFS(v):
    visited[v] = 1
    for i in range(N):
        if arr[v][i] == 1 and not visited[i]:
            DFS(i)

DFS(0)
print(sum(visited)-1)
"""
"""강사님 풀이2
N = int(input())
M = int(input())
arr = [[0] * N for _ in range(N)]
visited = [0] * N
cnt = 0

for _ in range(M):
    c1, c2 = map(int, input().split())
    arr[c1].append(c2)
    arr[c2].append(c1)
visited[1] = 1

def DFS(v):
    global cnt
    for i in arr[c1]:
        if not visited[i]:
            visited[i] = 1
            cnt += 1
            DFS(i)
            
DFS(1)
print(cnt)
"""

"""
7
6
1 2
2 3
1 5
5 2
5 6
4 7

4
"""
