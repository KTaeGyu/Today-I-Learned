"""
중괄호 { }와 대괄호 [ ]가 섞여있는 문자열이 있습니다.
중괄호의 대괄호 안에는 숫자들이 적혀있습니다.

왼쪽부터 오른쪽으로 Parsing을 하여, 중괄호 / 대괄호 안에 있는 숫자들로 연산을 하려고 합니다.
대괄호가 나오면 합을 구하면 되고, 중괄호가 나오면 곱을 구하면 됩니다.
위 예제에서는 [10], {3}, [20], [10], {2} 를 구할 수 있으며,
1. 0 + 10 = 10
2. 10 x 3 + 30
3. 30 + 20 = 50
4. 50 + 10 = 60
5. 60 x 2 = 120
따라서 정답은 120 입니다.
Parsing 후 연산 결과를 출력 해 주세요.

[세부조건]
1. 연산의 결과에 해당하는 수 n은 1 <= n <=10000을 만족한다.
2. 숫자는 모두 양수로 구성되어 있다.
3. 괄호가 부정확한 데이터는 입력되지 않는다.
4. 괄호 안에는 모두 숫자로 구성되어 있다.
"""
import sys
sys.stdin = open("input.txt", "r")

string = input()
n = len(string)

result = 0
num = 0
for i in range(n):
    try:
        num = num*10 + int(string[i])
    except ValueError:
        if string[i] == '[' or string[i] == '{':
            num = 0
        elif string[i] == ']':
            result += num
        elif string[i] == '}':
            result *= num
print(result)

"""강사님 풀이
word = input()
result = 0
for i in range(len(worl)):
    temp = ''
    index = i + 1
    if word[i] == '[':
        while word[index] != ']':
            temp += word[index]
            index += 1
        result += int(temp)
    elif word[i] == '{':
        while word[index] != '}':
            temp += word[index]
            index += 1
        result *= int(temp)
print(result)
"""

"""
ABC123[10]B{3}AT[20][10]BB{2}Q

120
"""
