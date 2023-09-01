n = int(input())
arr = list(map(int, input().split()))
arr.sort()

left = 0
right = n-1

MIN = 2e9 + 1
ansleft = 0
ansright = 0

while left < right:
    add = arr[left] + arr[right]
    if add == 0:
        print(arr[left], arr[right])
        exit()  # 프로그램 종료
    if MIN > abs(add):
        MIN = abs(add)
        ansleft = left
        ansright = right
    if add > 0:
        right -= 1
    else:
        left += 1

print(arr[ansleft], arr[ansright])