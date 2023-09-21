import heapq
N = int(input())
arr = list(map(int, input().split()))
que = []
cnt = 0
for i in range(N):
    heapq.heappush(que, [arr[i], -1])
while que:
    x, tp = heapq.heappop(que)
    if tp == 0:
        break
    cnt += 1
    y, tp = heapq.heappop(que)
    if tp == 0:
        break
    else:
        heapq.heappush(que, [y*2, 0])
    cnt += 1
print(cnt)