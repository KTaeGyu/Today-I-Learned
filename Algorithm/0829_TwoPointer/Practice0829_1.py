"""
1부터 100000사이의 n개의 자연수 중에서 연속된 숫자를 더했을 때 합이 m이 되는 경우는 몇 가지 인가요?
(구간의 크기가 정해지지 않았을 때는 투포인터 이용)

input
10 5
1 2 3 4 2 5 3 1 1 2

output
3
"""
n, m = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
for i in range(n):
    add = 0
    for j in range(i, n):
        add += arr[j]
        if add > m:
            break
        if add == m:
            cnt += 1
            break
print(cnt)

# 강사님 풀이
cnt, add = 0, 0
high, low = 0, 0
while True:
    if add >= m or high == n:
        add -= arr[low]
        low += 1
    elif add < m:
        add += arr[high]
        high += 1
    if add == m:
        cnt += 1
    if low == n:
        break
print(cnt)