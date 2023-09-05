T = int(input())
for tc in range(1, T+1):
    N = int(input())
    time = [0]
    fst = [[]]
    for n in range(1, N+1):
        arr = list(map(int, input().split()))
        t = arr[0]
        time.append(t)
        M = arr[1]
        if M == 0:
            fst.append([])
        else:
            fst.append(arr[2:])
    
    print(time)
    print(fst)

