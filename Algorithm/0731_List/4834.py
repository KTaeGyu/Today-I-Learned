# 0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.
#
# 가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오.
# 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.
#
#
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
# 다음 줄부터 테스트케이스의 첫 줄에 카드 장수 N이 주어진다. ( 5 ≤ N ≤ 100 )
# 다음 줄에 N개의 숫자 ai가 여백없이 주어진다. (0으로 시작할 수도 있다.)  ( 0 ≤ ai ≤ 9 )
#
#
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 가장 많은 카드의 숫자와 장 수를 차례로 출력한다.

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    cards = input()

    # 각 숫자의 개수를 세는 리스트(cl) 초기화
    cl = [0] * 10

    # 각 카드 숫자별 개수를 세기
    for card in cards:
        idx = int(card)
        cl[idx] += 1

    # 최댓값 찾기
    max_val = max(cl)

    # 최댓값이 중복되는 경우 최댓값 중 가장 큰 인덱스 찾기
    for i in range(len(cl) - 1, -1, -1):
        if cl[i] == max_val:
            max_idx = i
            break

    # 다른 방법들 최댓값과 최댓값을 가진 숫자 찾기
    # max_val = max(cl)
    # max_idx = 9 - cl[::-1].index(max_val)

    # max_idx = 9-list(reversed(cl)).index(max(cl))
    # max_val = max(cl)
    
    print(f'#{tc} {max_idx} {max_val}')