"""
A: 노드
E: 단방향 간선 수
s, e, w = 시작노드, 끝노드, 거리

최소거리?
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
    N, M, X = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for m in range(M):
        x, y, c = map(int, input().split())
        graph[x].append((c, y))

    ans = 0
    for i in range(1, N+1):
        if i == X:
            continue
        ans = max(ans, dijstra(i, X) + dijstra(X, i))

    print(f'#{tc} {ans}')