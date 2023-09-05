T = int(input())
for tc in range(1, T+1):
    n, c = input().split()
    c = int(c)
    now = set([n])
    next = set()
    for _ in range(c):
        while now:
            s = now.pop()
            s = list(s)
            for i in range(len(n) - 1):
                for j in range(i + 1, len(n)):
                    s[i], s[j] = s[j], s[i]
                    next.add(''.join(s))
                    s[i], s[j] = s[j], s[i]
        now, next = next, now
    result = max(map(int, now))
    print(f'#{tc} {result}')