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
cnt = 0
comb_lst = []

while True:
    tem_path = path.copy()
    # 조건 B 설정
    cnt_dict = {}
    for i in path:
        if i not in cnt_dict:
            cnt_dict[i] = 1
        else:
            cnt_dict[i] += 1
    tem_cnt = 0
    for i in cnt_dict.values():
        if i > 2:
            tem_cnt = 0
            break
        else:
            tem_cnt += 1
    
    # 조건 A, B 적용
    else:
        if tem_cnt != 0 and sorted(tem_path) not in comb_lst:
            cnt += 1

    # 조건 A 설정
    if sorted(tem_path) not in comb_lst:
        comb_lst.append(sorted(tem_path))

    if path[0] == N:
        break
    elif path[0] == 1:
        temp = path.pop(0)
        path[0] += temp
    else:
        temp = path.pop(0)
        path[0] += 1
        for i in range(1, temp):
            path.insert(0, 1)

print(cnt)


"""
5
1
10

5
1
22
"""