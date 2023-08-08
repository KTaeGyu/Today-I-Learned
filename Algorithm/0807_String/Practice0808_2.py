"""
'+'와 '-'기호가 들어있는 수식을 입력받고, 자동으로 계산해주는 프로그램을 작성해 주세요.

[힌트]
Parsing을 하기 위한 매서드가 불충분하다면 필요한 함수를 직접 구현하는 것이 좋다.

[세부조건]
1. 괄호는 없다.
2. 첫 번째 수는 양수 또는 음수가 될 수 있다.
3. +와 - 이외의 문자는 입력되지 안흔ㄴ다.
4. 띄어쓰기 없이 입력된다.
5. 문자열 길이 최댓값: 1000
6. 최종 결과는 음수가 될 수 있다.
7. 첫번째 수가 양수라면 '+' 기호가 생략된다.
"""
import sys
sys.stdin = open("input.txt", "r")

equation = input()
n = len(equation)

distinguish = [0]*n
for i in range(n):
    if equation[i] == '+':
        distinguish[i] = 1
    elif equation[i] == '-':
        distinguish[i] = -1
distinguish.append(1)

result = 0
num = 0
last_symbol = 1
for i in range(n+1):
    if distinguish[i] == 0:
        num = num*10 + int(equation[i])
    else:
        result += num*last_symbol
        last_symbol = distinguish[i]
        num = 0

print(result)

"""강사님 풀이
# eval 메서드
print(eval(input()))

# 풀이2
word = input().split('+')
ans = 0
for w in word:
    w = w.split('-')
    inner_ans = int(w[0])
    for i in range(1, len(w)):
        inner_ans -= int(w[i])
    ans += inner_ans
print(ans)
"""

"""승희 풀이
i, buho, result = 0, 0, 0
exp = input().strip()
while i < len(exp):
    if exp[i] == '-':
        buho = 1
        i += 1
    elif exp[i] == '+':
        buho = 0
        i += 1
    subnum = 0
    while i < len(exp) and exp[i] != '+' and exp[i] != '-':
        subnum = (subnum * 10) + int(exp[i])
        i += 1
    if buho == 1:
        result -= subnum
    else:
        result += subnum

print(result)
"""

"""
100+100-50+30

180
"""