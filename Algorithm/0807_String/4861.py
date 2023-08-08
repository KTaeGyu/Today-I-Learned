# ABBA 처럼 어느 방향에서 읽어도 같은 문자열을 회문이라 한다. NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램을 만드시오.
# 회문은 1개가 존재하는데, 가로 뿐만 아니라 세로로 찾아질 수도 있다.
#
# 예를 들어 N=10, M=10 일 때, 다음과 같이 회문을 찾을 수 있다.
#
# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
# 다음 줄부터 테스트케이스의 첫 줄에 N과 M이 주어진다. 10≤N≤100, 5≤M≤N
# 다음 줄부터 N개의 글자를 가진 N개의 줄이 주어진다.

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    strings = [list(input()) for _ in range(N)]
    strings_v = list(zip(*strings))
    n_strings = []
    for i in range(N):
        n_strings.append(''.join(strings[i]))
        n_strings.append(''.join(list(strings_v[i])))

    for string in n_strings:
        for i in range(N - M + 1):
            if string[i:i+M] == string[i:i+M][::-1]:
                print(f'#{tc} {string[i:i+M]}')

"""강사님 풀이
# 기본 회문
def is_p(string):
    return string == string[::-1]
 
    
# 풀이1
def find_p(N, M, arr):
    for i in range(N):
        for j in range(N - M + 1)
            h = arr[i][j:j+M]
            v = [arr[k][i] for k in range(j, j+M)]
            if h == h[::-1]:
                return h
            if v == v[::-1]:
                return v

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    result = find_p(N, M, arr)
    print(f'#{tc}', ''.join(result))
    
"""

"""
3
10 10
GOFFAKWFSM
OYECRSLDLQ
UJAJQVSYYC
JAEZNNZEAJ
WJAKCGSGCF
QKUDGATDQL
OKGPFPYRKQ
TDCXBMQTIO
UNADRPNETZ
ZATWDEKDQF
10 10
WPMACSIBIK
STWASDCOBQ
AMOUENCSOG
XTIIGBLRCZ
WXVSWXYYVU
CJVAHRZZEM
NDIEBIIMTX
UOOGPQCBIW
OWWATKUEUY
FTMERSSANL
20 13
ECFQBKSYBBOSZQSFBXKI
VBOAIDLYEXYMNGLLIOPP
AIZMTVJBZAWSJEIGAKWB
CABLQKMRFNBINNZSOGNT
NQLMHYUMBOCSZWIOBINM
QJZQPSOMNQELBPLVXNRN
RHMDWPBHDAMWROUFTPYH
FNERUGIFZNLJSSATGFHF
TUIAXPMHFKDLQLNYQBPW
OPIRADJURRDLTDKZGOGA
JHYXHBQTLMMHOOOHMMLT
XXCNJGTXXKUCVOUYNXZR
RMWTQQFHZUIGCJBASNOX
CVODFKWMJSGMFTCSLLWO
EJISQCXLNQHEIXXZSGKG
KGVFJLNNBTVXJLFXPOZA
YUNDJDSSOPRVSLLHGKGZ
OZVTWRYWRFIAIPEYRFFG
ERAPUWPSHHKSWCTBAPXR
FIKQJTQDYLGMMWMEGRUZ

#1 JAEZNNZEAJ
#2 MWOIVVIOWM
#3 TLMMHOOOHMMLT
"""