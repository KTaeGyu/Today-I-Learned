import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    string = input()
    stack = []
    cnt = 0
    result = 0
    for i in range(len(string)):
        if string[i] == '(':
            stack.append(string[i])
            cnt += 1
        else:
            if string[i-1] == '(':
                cnt -= 1
                stack.pop()
                result += cnt
            else:
                cnt -= 1
                result += 1
    print(result)

"""
2
()(((()())(())()))(())
(((()(()()))(())()))(()())

"""