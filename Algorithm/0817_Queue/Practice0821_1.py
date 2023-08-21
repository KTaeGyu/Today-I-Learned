"""
2차원 평면상에m개의 수직선과n개의 수평선으로 이루어진 격자 형태의 도로망이 있습니다.
아래 그림은7개의 수직선과6개의 수평선으로 이루어진 도로망의 예입니다.

수직선과 수평선이 만나는 교차점들 중 가장 왼쪽 아래 점의 위치는(1,1)이고,가장 오른쪽 위 점의 좌표는(m,n)입니다.
이 도로망을 운행하는 버스들이k개 있고,각 버스는 하나의 수평선 상의 두 교차점 사이 선분이나 하나의 수직선 상의 두 교차점 사이 선분을 왕복 운행합니다.
각 버스는 운행하는 선분 사이의 모든 교차점(선분의 양 끝 교차점 포함)에서 정차합니다.
출발지로부터 목적지가 주어졌을 때, 출발지로부터 목적지까지 갈 수 있는 최소한의 환승 횟수를 출력하는 프로그램을 작성하세요.
처음 탑승하는 버스도 환승 횟수에 포함하며, 출발지와 목적지는 항상 다른 교차점이 주어집니다.

입력
첫 번째 줄에 수직선의 수m과 수평선의 수n이 빈칸을 사이에 두고 주어집니다.(1≤m,n≤100,000)
두 번째 줄에 버스의 수k (1≤k≤5,000)가 주어집니다.
세 번째 줄부터k줄에 걸쳐 각 줄에 버스의 운행구간을 나타내는5개의 수b, x1, y1, x2, y2가 빈칸을 사이에 두고 주어집니다.
여기서b (1≤b≤k)는 버스의 번호, (x1,y1)과(x2, y2)는 이 버스가 운행하는 양쪽 끝 교차점의 좌표를 나타냅니다.
마지막 줄에 출발지와 목적지 좌표를 나타내는 네 개의 수sx, sy, dx, dy가 빈칸을 사이에 두고 주어집니다.
여기서(sx, sy)는 출발지 좌표이고(dx, dy)는 목적지 좌표이다. 1≤x1,x2,sx,dx≤m이고, 1≤y1,y2,sy,dy≤n입니다.
모든 입력에 대하여,출발지와 목적지는 다르게 주어지며 출발지에서 목적지로 가는 방법은 한 가지 이상 존재합니다.

출력
첫째 줄에 이용하는 최소 버스 수를 출력합니다.
"""
import sys
sys.stdin = open("input.txt", "r")

# 입력
m, n = map(int, input().split())
k = int(input())

# 그래프 정리
graph = {}
for _ in range(1, k + 1):
    graph[_] = []
for _ in range(k):
    b, x1, y1, x2, y2 = map(int, input().split())
    y, dy, x, dx = min(y1, y2), max(y1, y2), min(x1, x2), max(x1, x2)   # x와 y 좌표를 큰것, 작은것으로 구분하여 정리
    for i in range(y, dy + 1):
        for j in range(x, dx + 1):
            if (i, j) not in graph[b]:
                graph[b].append((i, j))                                 # 해당 노선에 포함되는 모든 좌표를 그래프에 입력

# 입력
sx, sy, dx, dy = map(int, input().split())

# BFS 로 가장 가까운 길 탐색
queue = []
visited = []

# 큐와 방문기록 초기 값 설정
for _ in range(1, k + 1):
    if (sy, sx) in graph[_]:
        queue.append((_, 1))    # 처음 level을 1로 설정
        visited.append(_)

# BFS 실행
while queue:
    now, level = queue.pop(0)   # 출발지에서 가까운 정류장을 찾기 위해 level 도입
    for i in graph[now]:        # 그래프의 좌표 중에,
        if i == (dy, dx):       # 목적지가 있으면, 출력 후 정지
            print(level)
            break
        for j in range(1, k + 1):
            if i in graph[j] and j not in visited:  # 없다면, 현재 좌표가 다른 노선과 곂치는지 확인 후, 곂치는 노선을 큐에 추가, level + 1, 방문 기록
                queue.append((j, level + 1))
                visited.append(j)

"""
7 6
8
1 2 1 2 2
2 1 1 5 1
6 7 3 7 6
7 2 1 2 6
3 3 2 6 2
4 5 6 5 1
5 1 5 7 5
8 3 5 6 5
2 1 7 4

3
"""