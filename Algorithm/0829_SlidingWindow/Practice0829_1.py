"""
n개의 정수를 입력받고, 연속된 m개의 정수들의 합을 구할 때 최대값 구하기

합이 가장 큰 구간의 값은 무엇일까요?

input
10 2
3 -2 -4 -9 0 3 7 13 8 -3

output
21
"""
N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = 0
for i in range(N-M):
    result = max(result, sum(arr[i:i+M]))
print(result)

# 강사님 코드
add = 0
for i in range(M):
    add += arr[i]
    MAX = add
for i in range(N-M):
    add += arr[i+M]
    add -= arr[i]
    if MAX < add:
        MAX = add
print(MAX)
