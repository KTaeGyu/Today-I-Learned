"""
띄어쓰기가 없는 한 문장이 입력됩니다.
다음 조건에 모두 허용이 된다면 pass, 하나라도 허용이 안된다면 fail을 출력해주세요.
[OK맨이 원하는 문자열 조건]
1. OK맨이 싫어하는 단어 "bad", "no", "puck"가 없어야 함
2. 연속적인 언더바 "_"가 총 5개 이하
3. 각 알파벳들 사용 횟수가 5회 이하 (대소문자 구분)
4. 숫자가 없어야 함
"""
import sys
sys.stdin = open("input.txt", "r")

string = input()
n = len(string)
udb_cnt = 0
word_dict = {}
word = ''

for i in range(n):
    try:
        int(string[i])
        print('fail')
        break
    except ValueError:
        if string[i] == '_':
            word = ''
            udb_cnt += 1
            if udb_cnt > 5:
                print('fail')
                break
        else:
            udb_cnt = 0
            if string[i] in word_dict.keys():
                word_dict[string[i]] += 1
                if word_dict[string[i]] > 5:
                    print('fail')
                    break
            else:
                word_dict[string[i]] = 1
            word += string[i]
            if word == 'bad' or word == 'no' or word == 'puck':
                print('fail')
                break
else:
    print('pass')

"""
____bck____a_c_k_

pass
"""