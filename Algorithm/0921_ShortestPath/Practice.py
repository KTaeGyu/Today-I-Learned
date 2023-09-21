"""
6 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
"""
# 1. Dijkstra: 힙 사용
import heapq


def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0
    while pq:
        cur_cost, cur_node = heapq.heappop(pq)
        if distance[cur_node] < cur_cost:
            continue
        for next_cost, next_node in graph[cur_node]:
            weight = cur_cost + next_cost
            if distance[next_node] <= weight:
                continue
            distance[next_node] = weight
            heapq.heappush(pq, (weight, next_node))


n, m = map(int, input().split())
graph = [[] for i in range(n)]
for _ in range(m):
    f, t, w = map(int, input().split())
    graph[f].append([w, t])

INF = int(1e9)
distance = [INF] * n

dijkstra(0)
print(distance)
