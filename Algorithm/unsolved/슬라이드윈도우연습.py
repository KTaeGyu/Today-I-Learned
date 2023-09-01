T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    start = 0
    end = m-1

    midsum = sum(arr[:end])

    ans = -999999
    s_idx = 0
    e_idx = 0

    while end < n:
        midsum += arr[end]
        if midsum > ans:
            ans = midsum
            s_idx = start
            e_idx = end
        midsum -= arr[start]
        start += 1
        end += 1
    print(f'#{tc} {s_idx} {e_idx} {ans}')
