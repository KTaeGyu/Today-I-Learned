"""
단어와 숫자들이 번갈아가며 적혀있는 한 문장을 입력받습니다. ex)AB514CDE112G5F
죄수명(대문자)과 사건번호(숫자)가 한 세트로 되어있지만, 띄어쓰기가 없기에 알아보기 힘듭니다.
죄수명과 사건번호를 각각 Parsing하고 사건번호에 17을 더한 값으로 출력해주세요

[입력]
첫 번째 줄에 parsing할 문자열이 주어집니다.
단, 문자열의 길이는 100을 넘지 않습니다.

[출력]
"죄수명#사건 번호"의 형식으로 parsing된 정보를 줄을 구분으로 출력합니다.
단, 각 정보는 문자열에서 앞에 위치한 정보일 수록 먼저 출력합니다.
"""
import sys
sys.stdin = open("input.txt", "r")

String = input()
N = len(String)

split = [0]*N
for i in range(N):
    try:
        int(String[i])
    except ValueError:
        split[i] = 1
split.append(1)

peoples = 1
for i in range(N):
    if split[i] + 1 == split[i+1]:
        peoples += 1

name = ''
num = 0
for j in range(N):
    if split[j] + 1 == split[j+1]:
        num = num*10 + int(String[j]) + 17
        pos = j + 1
        print(f'{name}#{num}')
        name = ''
        num = 0
    elif split[j] == 1:
        name += String[j]
    elif split[j] == 0:
        num = num*10 + int(String[j])

"""
AB100CDEF112F4G5

AB#117
CDEF#129
F#21
G#22
"""