# # 1. 기본 출력
# print("Hello world")



# # 2. 데이터 타입
# a1 = 1                                          # int
# a2 = 2.3                                        # float
# a3 = 2 + 3j                                     # complex, 자주 안씀
# a4 = "Hello world"                              # str
# a5 = [1, 2, 3, 4, 5]                            # list
# a6 = (1, 2, 3, 4, 5)                            # tuple
# a7 = range(5)                                   # range
# a8 = {1, 2, 3, 4, 5}                            # set
# a9 = {"name":"KTG", "age":28, "city":"seoul"}   # dict
# a10 = None                                      # None, 자주 안씀
# a11 = True                                      # Boolean
# def a12(name):                                  # function
#     message = 'Hello' + name
#     print(message)
# a13 = lambda x, y : x + y                       # function

# for i in range(1, 14):
#     var = f'a{i}'
#     var = eval(var)
#     print(type(var))



# # 3. 연산자
# print("7/3 : ", 7/3, "\n7//3 : ", 7//3, "\n7%3 : ", 7%3) # 2.333, 2, 1
# # 나눗셈, 몫, 나머지 
# # 소숫점 끝자리는 데이터 처리 과정에서 바뀌기도 함

# print(-2 ** 4)      #- 16
# print(-(2 ** 4))    # -16
# print((-2) ** 4)    # 16



# # 4. 변수
# degrees = 36.5
# # '=' 는 할당 연산자
# # 같다'의 의미인 비교 연산자는 '=='

# print(id(degrees))
# print(id(36.5))
# # degrees 에 36.5 라는 값의 메모리 주소를 할당하였으므로 둘이 같음

# degrees = 37.5
# print(id(degrees))
# # 변수 명은 같으나 위와 다른 값을 할당하였으므로 다른 주소를 갖게 됨

# num = 10
# double = 2 * num
# print(double)   # 20

# num = 5
# print(double)   # 20
# # num 변수를 재할당 했지만, double은 재할당 하지 않았으므로 바뀌지 않았음

# # General Type
# name = "KTG"
# age = 28
# height = 182.0
# weight = 102.4

# # Boolean Type
# is_student = True

# # Constant
# SECOND = 10
# MAX_VALLUE = 100
# PI = 3.141592

# # Snake_case 형태
# person_name = "TaeGyu"

# # function 사이 2줄 간격
# def calculate_sum(x, y):
#     return x + y


# def calculate_sub(x, y):
#     return x - y



# # 입출력
# # 문자열 입력
# char = input()
# print(char)
# char = input("문자 한개를 입력하세요!!")
# print(char)

# # 숫자 입력
# num = int(input())
# print(num)

# num = input()
# num = int(num)
# print(num)

# # 공백을 기준으로 여러 문자 입력
# char1, char2 = input().split()
# print(char1, char2)

# # 공백을 기준으로 여러 숫자 입력
# num1, num2 = map(int, input().split())
# print(num1, num2)

# # split() 활용
# year, month, day = map(int, input().split('.')) # '.'을 기준으로 분리하여 입력받음
# print(year, month, day)

# # list 형식으로 입력받기
# num_list = list(map(int, input().split()))
# print(num_list)



# # 포멧코드
# name = input()
# age = int(input())
# height = float(input())

# # %-string
# print("저의 이름은 %s, 나이는 %d, 키는 %.2f" %(name, age, height))
# # %'.n'를 이용하면 소숫점 n째 자리까지 출력, 기본은 6째 자리

# # f-string
# print(f"저의 이름은 {name}, 나이는 {age}, 키는 {height:.2f}")
# # :.2f 입력시 소숫점 2째자리까지, 제거시 입력한대로 출력
# # 가장 많이 쓰이는 방법

# # .format()
# print("저의 이름은 {}, 나이는 {}, 키는 {:.2f}".format(name, age, height))
# # 2번과 마찬가지
 