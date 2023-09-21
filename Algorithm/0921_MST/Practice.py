""" 
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
"""
# 1. MST, prim: 힙 사용
import heapq


def prim(start):
    heap = []
    MST = [0] * V
    sum_weight = 0
    heapq.heappush(heap, (0, start))
    while heap:
        weigth, v = heapq.heappop(heap)
        if MST[v]: continue
        MST[v] = 1
        sum_weight += weigth
        for nxt in range(V):
            if graph[v][nxt] == 0 or MST[nxt]: continue
            heapq.heappush(heap, (graph[v][nxt], nxt))
    return sum_weight


# 2. MST, kruskal: 정렬, union-find 사용
def find_set(x):
    if parents[x] == x:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x == y:
        return
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


V, E = map(int, input().split())
# 인접 그래프
graph = [[0]*V for _ in range(V)]
# 간선 정보
edge = []
for _ in range(E):
    f, t, w = map(int, input().split())
    # 인접 그래프
    graph[f][t] = w
    graph[t][f] = w
    # 간선 정보
    edge.append([f, t, w])

# 1. prim
result1 = prim(0)
print(result1)

# 2. kruskal: 정렬, Union-Find 사용
edge.sort(key=lambda x: x[2])

parents = [i for i in range(V)]

cnt = 0
sum_weight2 = 0
for f, t, w in edge:
    if find_set(f) != find_set(t):
        cnt += 1
        sum_weight2 += w
        union(f, t)
        if cnt == V:
            break

print(sum_weight2)