import itertools
# vscode keymap 설치 -> 적용


# 버블정렬 : 인접한 두 요소를 비교하여 큰 값을 오른쪽으로 이동시키는 과정을 반복.
def bubble(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


numbers = [63, 31, 27, 11, 25]
bubble(numbers)
print(numbers)

# 디버깅 방법 : 왼쪽에 브레이킹 포인트 설정 후 우클릭 > 디버그, 스텝오버(F8), 스텝인투(F7) 등 기능을 활용할 것


# 카운팅 정렬 : 정수를 정렬하는 알고리즘, 각 숫자의 개수를 세어서 정렬
def counting(arr):
    max_val = max(arr)
    # 카운트를 저장할 리스트
    count_arr = [0]*(max_val + 1)

    for num in arr:
        count_arr[num] += 1

    sorted_arr = []
    for i, count in enumerate(count_arr):  # 인덱스와 값을 쌍으로 반환
        sorted_arr.extend([i] * count)  # 인덱스를 카운트만큼 iterable 추가

    return sorted_arr


lst = [1, 4, 1, 2, 7, 5, 2]
print(counting(lst))

# 순열 : 주어진 항목들로 만들 수 있는 모든 가능한 순서(튜플)
for i1 in range(1, 4):
    for i2 in range(1, 4):
        if i2 != i1:
            for i3 in range(1, 4):
                if i3 != i1 and i3 != i2:
                    print(i1, i2, i3)

# 위 방법의 단점 : 시간복잡도가 숫자가 늘어날수록 기하급수적으로 늘어난다.

# itertools 모듈 사용
arr = [1, 2, 3]
result = list(itertools.permutations(arr))
print(result)

# 그리디 알고리즘 : 각 단계에서 가장 최선의 선택을 하는 방법
# 단점 : 매우 주관적이다.


# 거스름돈 문제. 가장 적은 수의 동전을 사용하여 거스름돈을 주는 문제
# 가장 큰 단위의 동전부터 사용하는 것이 최선
# 동전 동류 : 100, 50, 10
# 거스름돈 : 380
# 가장 적은 수의 동전으로 주는 방법은?
def coin_num(count):
    coin_types = (100, 50, 10)

    change_num = {}
    for coin_type in coin_types:
        change_num[coin_type] = count // coin_type
        count %= coin_type

    return change_num


print(coin_num(380))


def greedy(money, coins):
    coins.sort(reverse=True)
    # 거스름돈의 개수를 저장할 딕셔너리
    change = {coin: 0 for coin in coins}
    for coin in coins:
        while money >= coin:
            money -= coin
            # 해당 동전의 개수를 1씩 증가
            change[coin] += 1

    return change


print(greedy(380, [100, 50, 10]))

