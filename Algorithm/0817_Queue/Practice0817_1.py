"""
다음 주어진 조건에 따라 n개의 수를 처리하면 8자리의 암호를 생성할 수 있다.
    - 8개의 숫자를 입력 받는다.
    - 첫 번째 숫자를 1 감소한 뒤, 맨 뒤로 보낸다.
다음 첫 번째 수는 2 감소한 뒤 맨 뒤로, 그 다음 첫 번째 수는 3을 감소하고 맨 뒤로, 그 다음 수는 4, 그 다음 수는 5를 감소한다.
이와 같은 작업을 한 사이클이라 한다.
    - 숫자가 감소할 때 0보다 작아지는 경우 0으로 유지되며, 프로그램은 종료된다. 이 때의 8자리의 숫자 값이 암호가 된다.

[제약 사항]
주어지는 각 수는 integer 범위를 넘지 않는다.
마지막 암호 배열은 모두 한 자리 수로 구성되어 있다.

[입력]
각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호가 주어지고, 그 다음 줄에는 8개의 데이터가 주어진다.

[출력]
# 부호와 함께 테스트케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 답을 출력한다.
"""
import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    T = int(input())
    codes = list(map(int, input().split()))
    N = len(codes)
    a = 1
    while a > 0:
        minus = 1
        for i in range(1, 6):
            a = codes.pop(0) - i
            if a <= 0:
                codes.append(0)
                break
            codes.append(a)
            minus += 1
    print(f'#{T}', end=' ')
    print(*codes)


"""
1
9550 9556 9550 9553 9558 9551 9551 9551 
2
2419 2418 2423 2415 2422 2419 2420 2415 
3
7834 7840 7840 7835 7841 7835 7835 7838 
4
4088 4087 4090 4089 4093 4085 4090 4084 
5
2945 2946 2950 2948 2942 2943 2948 2947 
6
670 667 669 671 670 670 668 671 
7
8869 8869 8873 8875 8870 8872 8871 8873 
8
1709 1707 1712 1712 1714 1710 1706 1712 
9
10239 10248 10242 10240 10242 10242 10245 10235 
10
6580 6579 6574 6580 6583 6580 6577 6581 


#1 6 2 2 9 4 1 3 0 
#2 9 7 9 5 4 3 8 0 
#3 8 7 1 6 4 3 5 0 
#4 7 5 8 4 8 1 3 0 
#5 3 8 7 4 4 7 4 0 
#6 6 7 5 9 6 8 5 0 
#7 7 6 8 3 2 5 6 0 
#8 9 2 1 7 3 6 3 0 
#9 4 7 8 1 2 8 4 0 
#10 6 8 9 5 8 5 2 0
"""