"""
다섯 종류의 카드를 입력받습니다.('0'~'9')
각각의 카드들은 다량으로 쌓여있습니다.
다섯 종류의 숫자 카드에서 4장을 뽑는다.
뽑을 때마다 전에 뽑았던 카드번호와 간격이 3이하로 차이나는 중복순열이 몇 가지인지 출력하세요.
재귀호출을 이용할 것

[입력]
12345

[출력]
497
"""


# def is_good_card(card_lst, card):
#     for i in card:
#         if i != card_lst[4]:
#             break
#     else:
#         return 1
#
#     if card[3] != card_lst[4]:
#         card[3] = card_lst[card_lst.index(card[3]) + 1]
#         print(card)
#         for i in range(3):
#             if abs(int(card[i]) - int(card[i + 1])) > 3:
#                 return is_good_card(card_lst, card)
#         else:
#             return 1 + is_good_card(card_lst, card)
#     elif card[2] != card_lst[4]:
#         card[3] = card_lst[0]
#         card[2] = card_lst[card_lst.index(card[2]) + 1]
#         print(card)
#         for i in range(3):
#             if abs(int(card[i]) - int(card[i + 1])) > 3:
#                 return is_good_card(card_lst, card)
#         else:
#             return 1 + is_good_card(card_lst, card)
#     elif card[1] != card_lst[4]:
#         card[2], card[1] = card_lst[0], card_lst[0]
#         card[1] = card_lst[card_lst.index(card[1]) + 1]
#         print(card)
#         for i in range(3):
#             if abs(int(card[i]) - int(card[i + 1])) > 3:
#                 return is_good_card(card_lst, card)
#         else:
#             return 1 + is_good_card(card_lst, card)
#     elif card[0] != card_lst[4]:
#         card[1], card[2], card[3] = card_lst[0], card_lst[0], card_lst[0]
#         card[0] = card_lst[card_lst.index(card[0]) + 1]
#         print(card)
#         for i in range(3):
#             if abs(int(card[i]) - int(card[i + 1])) > 3:
#                 return is_good_card(card_lst, card)
#         else:
#             return 1 + is_good_card(card_lst, card)
#
#
# N = [1, 2, 3, 4, 5]
#
# cnt = 0
# for i in range(5):
#     for j in range(5):
#         for k in range(5):
#             for n in range(5):
#                 num = [N[i], N[j], N[k], N[n]]
#                 for m in range(3):
#                     if abs(num[m] - num[m+1]) > 3:
#                         break
#                 else:
#                     cnt += 1
# print(cnt)
#
# n = [N[0]]*4
#
# print(is_good_card(N, n))  # 재귀가 너무 깊음

"""강사님 풀이
card = [1, 2, 3, 4, 5]
path = [0] * 4
cnt = 0


def card_cnt(level):
    global cnt

    if level == 4:
        cnt += 1
        return
    for i in range(5):
        path[level] = card[i]
        if abs(int(path[level]) - int(path[level - 1])) >= 4:
            continue
        card_cnt(level + 1)


card_cnt(0)
print(cnt)
"""