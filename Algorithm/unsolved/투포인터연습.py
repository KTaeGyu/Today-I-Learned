n, m = map(int, input().split())
arr = list(map(int, input().split()))
left, right = 0, 0
add, cnt = 0, 0
while right <= n:
    if add < m:
        if right < n:
            add += arr[right]
        right += 1
    if add > m:
        add -= arr[left]
        left += 1
    if add == m:
        cnt += 1
        if right < n:
            add += arr[right]
        right += 1
print(cnt)
