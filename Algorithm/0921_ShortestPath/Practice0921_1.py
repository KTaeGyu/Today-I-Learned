import sys
sys.stdin = open("../input.txt", "r")
import heapq


def dijkstra(start):
    pq = []
    heapq.heappush(pq, [0, start])
    distance[start] = 0
    while pq:
        cur_cost, cur_node = heapq.heappop(pq)
        if distance[cur_node] < cur_cost:
            continue
        for next_cost, next_node in graph[cur_node]:
            weight = cur_cost + next_cost
            if distance[next_node] < weight:
                continue
            distance[next_node] = weight
            heapq.heappush(pq, [weight, next_node])


N, T = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(T):
    a, b, w = map(int, input().split())
    graph[a].append([w, b])

INF = 300001
distance = [INF] * N
dijkstra(0)
print(distance[N-1] if distance[N-1] != INF else 'impossible')
