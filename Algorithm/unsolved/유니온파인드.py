def find(node):
    if node != root[node]:
        root[node] = find(root[node])
    return root[node]


def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if rank[root_x] > rank[root_y]:
        root[root_y] = root_x
    else:
        root[root_x] = root_y
        if rank[root_x] == rank[root_y]:
            rank[root_y] += 1


N, Q = map(int, input().split())
rank = [0] * (N + 1)
root = [i for i in range(N + 1)]
for _ in range(Q):
    K, A, B = map(int, input().split())
    if K == 0:
        if find(A) == find(B):
            print('YES')
        else:
            print('NO')
    else:
        union(A, B)
