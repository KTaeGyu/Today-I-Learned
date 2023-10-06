"""
N: 노드 수
M: 간선 수
K: 햇수
A, B: 출발점, 도착점
f, t, c: 시작노드, 끝노드, 통행료
p: 연도별 통행료 인상

연도별 최소 통행료 출력
"""
import sys
sys.stdin = open("../input.txt", "r")
import heapq

N, M, K = map(int, input().split())
A, B = map(int, input().split())
graph = [[] for _ in range(N+1)]
for m in range(M):
    f, t, c = map(int, input().split())
    graph[f].append((c, t))
    graph[t].append((c, f))

p = 0
for k in range(K+1):
    if k > 0:
        p += int(input())
    pq = []
    heapq.heappush(pq, (0, A))
    distance = [float('inf') for _ in range(N+1)]
    distance[A] = 0
    while pq:
        cur_cost, cur_node = heapq.heappop(pq)
        if distance[cur_node] < cur_cost:
            continue
        for next_cost, next_node in graph[cur_node]:
            weight = cur_cost + next_cost + p
            if distance[next_node] <= weight:
                continue
            distance[next_node] = weight
            heapq.heappush(pq, (weight, next_node))
    print(distance[B])
