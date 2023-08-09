"""
콜라즈 추측은 1937년에 처음으로 이 추측을 제기한 로타르 클라츠의 이름을 딴 것이다.
콜라즈 추측은 특정 자연수가 아래의 과정을 거치면 무조건 1이 된다는 추측이다.

1. 어떤 수가 짝수라면 2로 나눈다.
2. 어떤 수가 홀수라면 3을 곱하고 1을 더한다.
3. 어떤수가 1이 아니라면 1, 2를 반복한다.

예를 들어, 6은 6 3 10 5 16 8 4 2 1로 총 8번만에 1이 됩니다.
양수인 정수 N이 주어질 때 콜라츠 추측의 과정을 몇 번 거쳐야 1이 되는지 구하는 프로그램을 작성하시오

[입력]
첫번째 줄에 양의 정수 N이 주어진다.

[출력]
N이 1이 되는 콜라츠 추츠그이 과정 횟수를 출력한다.
"""


def colatz(N):
    if N == 1:
        return 0
    elif N % 2 == 0:
        return 1 + colatz(N // 2)
    else:
        return 1 + colatz(N * 3 + 1)


n = int(input())
print(colatz(n))
