"""
알렉산드로 집안에서 딸 아이가 태어났습니다.
유명한 작명소에서 딸 아이의 이름을 잘 짓는 노하우를 배우게 되었습니다.
좋은 이름의 조건은 다음과 같습니다.

[조건]
1. 소문자만 사용할 것.
2. 특수문자 사용 금지
3. 같은 알파벳이 2개 이하로만 사용할 것.
4. 모음(a, e, i, o, u) 알파벳은 3개 사용할 것. (중복 포함)

알렉산드로가 지은 n개의 이름을 입력 받고,
각 이름에 대해서 좋은 이름이라면 good을, 좋은 이름이 아니라면 no를 출력하라.

[입력]
첫 번째 줄에 이름의 개수 n이 주어집니다.(1 <= n <= 10)
다음 n개의 줄에 걸쳐 좋은 이름인지 확인할 문자열이 주어집니다.
단, 문자열에는 공백이 포함되어 있지 않습니다.

[출력]
각 이름에 대해서 좋은 이름이라면 good을, 좋은 이름이 아니라면 no를 출력
"""
import sys
sys.stdin = open("input.txt", "r")

n = int(input())
chars = {}
moem = ['a', 'e', 'i', 'o', 'u']

for tc in range(n):
    name = input()
    try:
        # 조건 1, 2, 3
        for i in name:
            if 97 <= ord(i) <= 122:
                pass
            else:
                raise ValueError
            if i not in chars:
                chars[i] = 1
            else:
                chars[i] += 1
                if chars[i] > 2:
                    raise ValueError

        # 조건 4
        sum_v = 0
        for i in moem:
            if i in chars.keys():
                sum_v += chars[i]
        if sum_v != 3:
            raise ValueError
        print('good')

    except ValueError:
        print('no')
"""
3
kfcbbqioi
mincoding
samham_t

good
good
no
"""
