"""
양의 정수 N이 주어지면 N의 모든 자릿수를 합한 값을 출력하는 프로그램을 재귀함수를 활용하여 작성하시오
"""


def add_nums(num):
    if num // 10 == 0:
        return num
    return (num % 10) + add_nums(num // 10)


n = int(input())
print(add_nums(n))
