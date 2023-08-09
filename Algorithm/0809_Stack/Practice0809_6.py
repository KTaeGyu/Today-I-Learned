"""
1부터 N까지의 정수가 있다.
이 정수들을 활용한 합으로 N을 만들 수 있는 경우의 수를 모두 구하라.

[제한]
A. 중복 조합은 중복해서 카운팅 하지 않는다.
B. 같은 정수는 2번까지 사용할 수 있다.

[입력]
첫번째 줄에 N이 입력된다.

[출력]
첫번째 줄에 1~N의 정수들을 제한에 맞게 활용하여 합을 N으로 만들 수 있는 경우의 수의 개수를 출력한다.
"""
N = int(input())
path = [1]*N

while path[0] != N:
    if path[len(path)-1] == 1:
        path[len(path)-2] += path.pop(len(path)-1)
    else:
        temp = path.pop(len(path)-1)
        for


"""
5
1
10

5
1
22
"""