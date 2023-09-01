n = int(input())
arr= list(map(int, input().split()))

left = 0
right = n - 1

minimum = 2e9 + 1
ansleft = 0
ansright = 0
max_sum = 0

while left < right:
    sum = arr[left] + arr[right]
    if sum == 0:
        if abs(arr[left] + arr[right]) > max_sum:
            ansleft = left
            ansright =right
            max_sum = abs(arr[left] + arr[right])
        print(arr[left], arr[right])
        exit()
    if minimum > abs(sum):
        minimum = abs(sum)
        ansleft = left
        ansright = right
    if sum > 0:
        right -= 1
    else:
        left += 1
print(arr[ansleft], arr[ansright])
