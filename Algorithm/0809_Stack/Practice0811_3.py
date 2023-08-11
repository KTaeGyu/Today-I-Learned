"""
idx         0   1   2   3   4   5   6
evid        -1  0   0   1   2   4   4
timeStamp   8   3   5   6   8   9   10

추적을 시작 할 index를 입력 받으세요
만약 5를 입력받으면, 5번부터 시작
rut == 5 << 4 << 2 << 0 << -1(검거)
tim == 9    8    5    8
0번인덱스부터 몇시에 몇번 인덱스로 도착했는지
"""
evid = [-1, 0, 0, 1, 2, 4, 4]
timeStamp = [8, 3, 5, 6, 8, 9, 10]
start = int(input())

stack = [start]
visited = []
result = []

while stack:
    now = stack.pop()
    if evid[now] == -1:
        result.append(f'{now}번index(출발)')
        break
    if now not in visited:
        result.append(f'{now}번index({timeStamp[now]}시)')
        visited.append(now)
        stack.append(evid[now])

result.reverse()
for i in result:
    print(i)

"""강사님 풀이
evid = [-1, 0, 0, 1, 2, 4, 4]
timeStamp = [8, 3, 5, 6, 8, 9, 10]
N = int(input())

def DFS(idx, time):
    if evid[idx] == -1:
        print(f'{idx}번index(출발)')
        return
    DFS(evid[idx], timeStamp[idx])
    print(f'{idx}번index({timeStamp[idx]}시)')
    
DFS(N, timeStamp[N])
"""