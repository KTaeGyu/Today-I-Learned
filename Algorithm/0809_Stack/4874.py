"""
Forth라는 컴퓨터 언어는 스택 연산을 기반으로 하고 있어 후위 표기법을 사용한다. 예를 들어 3+4는 다음과 같이 표기한다.

3 4 + .

Forth에서는 동작은 다음과 같다.

숫자는 스택에 넣는다.
연산자를 만나면 스택의 숫자 두 개를 꺼내 더하고 결과를 다시 스택에 넣는다.
‘.’은 스택에서 숫자를 꺼내 출력한다.

Forth 코드의 연산 결과를 출력하는 프로그램을 만드시오. 만약 형식이 잘못되어 연산이 불가능한 경우 ‘error’를 출력한다.

다음은 Forth 연산의 예이다.

    코드        출력
    4 2 / .     2
    4 3 - .     1

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스의 별로 정수와 연산자가 256자 이내의 연산코드가 주어진다. 피연산자와 연산자는 여백으로 구분되어 있으며, 코드는 ‘.’로 끝난다.
나눗셈의 경우 항상 나누어 떨어진다.

[출력]
#과 1번부터인 테스트케이스 번호, 빈칸에 이어 계산결과를 정수로 출력하거나 또는 ‘error’를 출력한다.
"""
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    Forth_code = list(input().split())
    n = len(Forth_code)
    stack = [0]*n
    top = -1
    for i in Forth_code:
        if i in '+-*/':
            num1 = stack[top]
            top -= 1
            num2 = stack[top]
            top -= 1
            if top < -1:
                print(f'#{tc} error')
                break
            elif i == '+':
                top += 1
                stack[top] = num2 + num1
            elif i == '-':
                top += 1
                stack[top] = num2 - num1
            elif i == '*':
                top += 1
                stack[top] = num2 * num1
            elif i == '/':
                top += 1
                stack[top] = num2 / num1
        elif i == '.':
            if top != 0:
                print(f'#{tc} error')
            else:
                print(f'#{tc} {int(stack[top])}')
        else:
            top += 1
            stack[top] = int(i)

"""강사님 풀이
T = int(input())
for tc in range(1, T+1):
    forth = list(input().split())
    stack = []
    error = False
    for i in range(len(forth) - 1):
        if forth[i].isdigit():
            stack.append(forth[i])
        else:
            try:
                b = int(stack.pop())
                a = int(stack.pop())
                if forth[i] == "+":
                    ans = a + b
                elif forth[i] == "-":
                    ans = a - b
                elif forth[i] == "*":
                    ans = a * b
                elif forth[i] == "/":
                    ans = a // b
                stack.append(ans)
            except:
                error = True
    if error == True or len(stack) != 1:
        print(f'#{tc} error')
    else:
        print(f'#{tc} {stack.pop()}')
"""

"""
3
10 2 + 3 4 + * .
5 3 * + .
1 5 8 10 3 4 + + 3 + * 2 + + + .

#1 84
#2 error
#3 168
"""