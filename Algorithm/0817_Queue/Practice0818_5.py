"""
코코는 결혼 상대를 찾기 위해 결혼 정보 회사에 가입을 하였습니다.
결혼 정보 회사에서는 코코와 지인이 아닌 사람을 주선해주려고 합니다.
아래 이미지는 사람들간 관계 여부를 표현한 그래프입니다.

위 그림에서는 1, 2, 3, 4 가 서로 지인 관계이며, 이들은 5, 6, 7번과는 지인 관계가 아닙니다.
따라서,A그룹, B그룹, C그룹 사람들은 서로 친분이 없습니다.

코코를 포함하여 총 N 명의 사람들이 결혼 정보 회사에 가입이 되어있는 상황에서,
코코에게 특정 사람을 주선해도 될지 판단하는 프로그램을 작성 해주세요.

입력
첫째 줄에 결혼정보회사에 가입된 사람의 수 N과  ( 2 <= N <= 100)
서로 연관됨을 나타내는 관계수 T 가 입력됩니다. ( 1 <= T <= N(N-1)/2 )
둘째 줄에는 T 줄에 걸쳐 서로 연관이 있는 사람들의 정보가 주어집니다.
사람들 지인 관계 정보는 A B 형태로 입력되며, A 번 사람과 B번 사람이 서로 지인 임을 나타냅니다. ( 1 <= A, B <= N, A=/=B)
마지막 줄에는 코코씨와 결혼 상대로 적합한지 확인해볼 상대 번호가 입력됩니다. ( 1 <= 번호 <= N)

출력
연관이 있는 상대이면 YES연관이 없는 상대이면 NO를 출력해주세요.
"""
import sys
sys.stdin = open("input.txt", "r")

N = int(input())
T = int(input())
graph = {}
for _ in range(1, N+1):
    graph[_] = []
for t in range(T):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)
coco = int(input())
match = int(input())

q = [coco]
visited = set()
visited.add(coco)
while q:
    now = q.pop(0)
    if now == match:
        print("YES")
        break
    for i in graph[now]:
        if i not in visited:
            q.append(i)
            visited.add(i)
else:
    print("NO")
"""
6
4
1 2
3 1
3 4
5 6
1
5

NO
"""