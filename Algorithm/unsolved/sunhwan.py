T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    for a in range(N):
        A = arr[a]
        for b in range(a+1, N):
            B = arr[b]
            for c in range(N):
                C = arr[c]
                for d in range(c+1, N):
                    D = arr[d]
                    if a != b and a != c and a != d and b != c and b != d and c != d:
                        if abs(a-b)!=1 and abs(a-c)!=1 and abs(a-d)!=1 and abs(b-c)!=1 and abs(b-d)!=1 and abs(c-d)!=1:
                            if abs(a-b)!=N-1 and abs(a-c)!=N-1 and abs(a-d)!=N-1 and abs(b-c)!=N-1 and abs(b-d)!=N-1 and abs(c-d)!=N-1:
                                if a < c < b and a < d < b:
                                    result = (A + B) ** 2 + (C + D) ** 2
                                    if ans < result:
                                        ans = result
                                if (c < a or b < c) and (d < a or b < d):
                                    result = (A + B) ** 2 + (C + D) ** 2
                                    if ans < result:
                                        ans = result
    print(f'#{tc} {ans}')