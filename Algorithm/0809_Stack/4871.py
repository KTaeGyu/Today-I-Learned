"""
V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프에 대한 정보가 주어질 때, 특정한 두 개의 노드에 경로가 존재하는지 확인하는 프로그램을 만드시오.
두 개의 노드에 대해 경로가 있으면 1, 없으면 0을 출력한다.
예를 들어 다음과 같은 그래프에서 1에서 6으로 가는 경로를 찾는 경우, 경로가 존재하므로 1을 출력한다.

1: 4, 3
2: 3, 5
3:
4: 6
5:
6:

노드번호는 1번부터 존재하며, V개의 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스의 첫 줄에 V와 E가 주어진다. 5≤V≤50, 4≤E≤1000
테스트케이스의 둘째 줄부터 E개의 줄에 걸쳐, 출발 도착 노드로 간선 정보가 주어진다.
E개의 줄 이후에는 경로의 존재를 확인할 출발 노드 S와 도착노드 G가 주어진다.

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
"""
import sys
sys.stdin = open("input.txt", "r")


def dfs(graph, start, end):
    stack = [start]
    visited = set()

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for next_node in graph[node]:
                if next_node == end:
                    return True
                elif next_node not in visited:
                    stack.append(next_node)
    return False


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())            # 노드 수, 간선 수 입력

    nodes = {}                                  # 간선이 연결 된 노드 리스트
    for e in range(E):
        s, e = map(int, input().split())
        if s in nodes:
            nodes[s].append(e)
            nodes[s].sort()
        else:
            nodes[s] = [e]
        if e not in nodes:
            nodes[e] = []

    s_node, e_node = tuple(map(int, input().split()))  # 연결 여부를 확인할 노드 둘

    if dfs(nodes, s_node, e_node):
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')

    s_nodes = dict(sorted(nodes.items()))
    print(V, E, ":", s_nodes, ":", (s_node, e_node))


"""
3
6 5
1 4
1 3
2 3
2 5
4 6
1 6
7 4
1 6
2 3
2 6
3 5
2 5
9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9

#1 1
#2 1
#3 1
"""