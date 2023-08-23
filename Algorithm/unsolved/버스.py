T = int(input())
for tc in range(1, T+1):
    N = int(input())
    stop = [0]* 5001
    for i in range(N):
        Ai, Bi = map(int, input().split())
        for j in range(Ai, Bi + 1):
            stop[j] += 1
    P = int(input())
    result = []
    for j in range(P):
        Cj = int(input())
        result.append(stop[Cj])
    print(f'#{tc}', *result)
