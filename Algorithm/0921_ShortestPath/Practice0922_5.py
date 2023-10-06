"""
N, M: 행, 열
K: 비용

행열 시작부터 끝까지 가는데 드는 최소비용
"""
import sys
from pprint import pprint
sys.stdin = open("../input.txt", "r")
import heapq


def dijkstra(y, x):
    pq = []
    heapq.heappush(pq, (arr[y][x], y, x))
    distance = [[float('inf')] * M for _ in range(N)]
    distance[y][x] = arr[y][x]
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while pq:
        cw, cy, cx = heapq.heappop(pq)
        if distance[cy][cx] < cw:
            continue
        for dy, dx in direction:
            ny, nx = cy + dy, cx + dx
            if ny < 0 or ny >= N:
                continue
            if nx < 0 or nx >= M:
                continue
            weight = cw + arr[ny][nx]
            if distance[ny][nx] <= weight:
                continue
            distance[ny][nx] = weight
            heapq.heappush(pq, (weight, ny, nx))
    print(distance[N-1][M-1])


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dijkstra(0, 0)
