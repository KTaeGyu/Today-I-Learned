"""
뉴스 기사에서 웹사이트 URL만 추출하려고 합니다.
띄어쓰기가 없는 한줄의 기사를 입력받고, 다음 조건에 맞는 URL은 총 몇개인지 출력 해 주세요
[URL조건]
1. 대소문자 구분은 없습니다.
2. 시작단어는 http:// 또는 https:// 입니다.
3. 끝 단어는 .com 또는 .co.kr 또는 .org 또는 .net 입니다.
4. 시작단어와 끝 단어 사이에는 최소 3글자 이상 있어야 합니다.

[입력]
첫 번째 줄에 URL을 찾을 기사에 해당하는 문자열이 주어집니다.
단, 문자열의 길이는 100을 넘지 않습니다.

[출력]
기사에 URL이 몇 개가 있는지 출력합니다.
"""
import sys
sys.stdin = open("input.txt", "r")

article = input().lower()
n = len(article)

start = ''
start_idx = n
end = ''
end_idx = 0
count = 0
for i in range(n):
    if article[i] == 'h':
        for j in range(8):
            start += article[i+j]
            if start == 'http://' or start == 'https://':
                start_idx = i+j+1
        else:
            start = ''

    elif article[i] == '.':
        for k in range(6):
            if i + k < n:
                end += article[i+k]
                if end == '.com' or end == '.org' or end == '.net' or end == '.co.kr':
                    end_idx = i
                    if end_idx - start_idx >= 3:
                        count += 1
                        start_idx = n
        else:
            end = ''

print(f'{count}개')
"""
ABHttp://bbq.comhttps://a.co.krBBQhttpS://KFC.org
`123456789`123456789`12345789`123456789`12345678` >> index

2개
"""
