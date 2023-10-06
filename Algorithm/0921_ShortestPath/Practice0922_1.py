"""
N : 집 수
M : 노드 수
X : 인수 집
x, y, c : 출발노드, 도착노드, 비용

각 노드에서 X로 오고 가는데 드는 최소 비용?
 -> 플로이드 워셜?
 -> 다익스트라 여러번?
"""
import sys
sys.stdin = open("../input.txt", "r")
import heapq


def dijstra(start, end):
    pq = []
    heapq.heappush(pq, (0, start))
    weight_table = [float('inf')] * (N+1)
    weight_table[start] = 0
    while pq:
        cur_cost, cur_node = heapq.heappop(pq)
        if cur_cost > weight_table[cur_node]:
            continue
        for next_cost, next_node in graph[cur_node]:
            weight = cur_cost + next_cost
            if weight > weight_table[next_node]:
                continue
            weight_table[next_node] = weight
            heapq.heappush(pq, (weight, next_node))
    return weight_table[end]


T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((w, e))

    ans = dijstra(0, N)

    print(f'#{tc} {ans}')