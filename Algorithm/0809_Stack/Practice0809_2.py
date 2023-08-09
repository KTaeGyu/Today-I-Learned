"""
자연수 N 을 입력 받으시오
N 을 이진수로 바꿔서 출력하는 프로그램을 작성하시오.
단, 재귀 호출을 이용하세요

[입력]
첫째 줄에 자연수 N이 주어집니다.(N의 길이는 100000이하입니다.)

[출력]
이진수로 변환한 결과를 출력하면 된다.
"""


def bin_maker(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    elif num == 2:
        return 10
    elif num % 2 == 1:
        return bin_maker(num-1) + bin_maker(1)
    elif num % 2 == 0:
        return 10*bin_maker(num // 2)


for i in range(10):
    print(bin_maker(i))

"""강사님 풀이
def func(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return func(n // 2) + str(n % 2)
N = int(input())
print(func(N))
"""

"""
2

10
"""
