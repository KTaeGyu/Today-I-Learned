# # 조건문 실습
# # 1
# num = int(input())

# if num > 0:
#     if num % 2 == 1:
#         print("ODD")
#     else:
#         print("EVEN")
# else:
#     pass

# # 2
# year = int(input())

# if year % 400 == 0:
#     print("윤년")
# elif year % 100 == 0:
#     print("평년")
# elif year % 4 == 0:
#     print("윤년")
# else:
#     print("평년")






# # for 실습
# # 1
# for i in range(2, 10):
#     print(f"< {i}단 >")
#     for j in range(1, 10):
#         print(f'{i} * {j} = {i*j}')

# # 2
# n = int(input())

# print(f'n : {n}')
# for i in range(n):
#     for j in range(i+1):
#         print('*', end = '') 
#     print()







# # while 실습
# # 1
# i = 0
# while i < 10:
#     i += 1
#     if i % 2 == 0:
#         continue
#     print(i, end = ' ')
# print()

# # 2
# while True:
#     ans = input("shall we close? (y/n)")
#     if ans == 'y':
#         print('the end')
#         break

# # 3
# num = int(input())
# cnt = 0
# while num > 0:
#     num //= 10
#     cnt += 1
# print(cnt)








# # 2 차원 리스트 실습
# # 1
# from math import sqrt
# num_list = [1, 4, 9, 16, 25]
# sqrt_list = [sqrt(num) for num in num_list]
# print(sqrt_list)

# sqrt_list_2 = []
# for number in num_list:
#     sqrt_list_2.append(sqrt(number))
# print(sqrt_list_2)

# 2 if
from math import sqrt
num_list = [1, 4, 9, 16, 25]
sqrt_list = [sqrt(num) for num in num_list if num % 2 == 0]
print(sqrt_list)







# # pip 실습
# url = 'https://random-data-api.com/api/v2/users'

# response = requests.get(url).json()

# print(response)
# print(response['address']['country'])
# print(response.get('address').get('country'))