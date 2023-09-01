import sys
sys.stdin = open("input.txt", "r")


def check(nums):
    for i in range(10):
        if nums[i] >= 3:
            return True
        if i <= 7 and nums[i] >= 1 and nums[i+1] >= 1 and nums[i+2] >= 1:
            return True
    return False


T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    p1 = [0]*10
    p2 = [0]*10
    for i in range(6):
        num1 = arr[i*2]
        p1[num1] += 1
        if check(p1):
            print(f'#{tc} 1')
            break
        num2 = arr[i*2+1]
        p2[num2] += 1
        if check(p2):
            print(f'#{tc} 2')
            break
    else:
        print(f'#{tc} 0')

"""
def check_win(cards):
    cnt = [0] * 10
    for num in cards:
        cnt[num] += 1
    if 3 in cnt:
        return True
    for i in range(8):
        if 0 not in cnt[i:i+3]:
            return True
    return False
.
.
.
"""