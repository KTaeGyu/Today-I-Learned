# 진법 변경 (10진수 -> n진수)
print(bin(12)) #0b1100
print(oct(12)) #0o14
print(hex(12)) #0xc

# 0.6666666666666666
print(2/3)

# 1.6666666666666667
print(5/3)

a = 3.2 - 3.1 # 0.1000000000000009
b = 1.2 - 1.1 # 0.0999999999999987

print(a)
print(b)

num_a = f'{a:.1f}'
num_b = f'{b:.1f}'

print(num_a)
print(num_b)

# 1. 임의의 작은 수 활용
print(abs(a - b) <= 1e-10) #True

# 2. math 모듈 활용
import math
print(math.isclose(a, b)) # True

# 314 * 0.01
number = 314e-2

# float
print(type(number))

# 3.14
print(number)
print(314 * 10 ** -2)

# 31400.0
print(314e2)

# Hello, World!
print('Hello, World!')

# str
print(type('Hello, World!'))

# 문자열 안에 '작은따옴표'를 사용하려면 큰따옴표로 묶는다.
print("문자열 안에 '작은따옴표'를 사용하려면 큰따옴표로 묶는다.")

# 문자열 안에 "큰따옴표"를 사용하려면 작은따옴표로 묶는다.
print('문자열 안에 "큰따옴표"를 사용하려면 작은따옴표로 묶는다.')

# 철수야 '안녕'
print('철수야 \'안녕\'')

'''
이 다음은 엔터
입니다.
'''
print('이 다음은 엔터\n입니다.')

bugs = 'roaches'
counts = 13
area = 'living room'

# Debugging roaches 13 living room
print(f'Debugging {bugs} {counts} {area}')
print('Debugging {} {} {}'.format(bugs, counts, area))
print('Debugging %s %d %s' % (bugs, counts, area))

# f-string 응용
# f-string advanced 검색하여 많은 기능을 찾아볼 것
greeting = 'hi'
print(f'{greeting:.>10}') # >n : 오른쪽 정렬
print(f'{greeting:.^10}') # ^n : 가운데 정렬
print(f'{greeting:.<10}') # >n : 왼쪽 정렬
print(f'{3.141592:.4f}') # .nf : 반올림하여 소숫점 n 자리 까지 표시

my_str = 'hello'

# 인덱싱
print(my_str[1]) # e

# 슬라이싱
print(my_str[2:4]) # ll

# 길이
print(len(my_str)) # 5

# my_str = 'hello'

# # TypeError: 'str' object does not support item assignment
# my_str[1] = 'z'

my_list_1 = []

my_list_2 = [1, 'a', 3, 'b', 5]

my_list_3 = [1, 2, 3, 'python', ['hello', 'world', '!!']]

my_list = [1, 'a', 3, 'b', 5]

# 인덱싱
print(my_list[1]) # a

# 슬라이싱
print(my_list[2:4]) # [3, 'b']
print(my_list[:3]) # [1, 'a', 3]
print(my_list[3:]) # ['b', 5]
print(my_list[0:5:2]) # [1, 3, 5]
print(my_list[::-1]) # [5, 'b', 3, 'a', 1]

# 길이
print(len(my_list)) # 5

my_list = [1, 2, 3, 'python', ['hello', 'world', '!!']]

print(len(my_list)) # 5
print(my_list[4][-1]) # !!
print(my_list[-1][1][0]) # w

my_list = [1, 2, 3]
my_list[0] = 100

print(my_list) # [100, 2, 3]

my_tuple_1 = ()

my_tuple_2 = (1,) # 튜플의 자료가 1개라면 ()를 연산으로 인식할 수 있으므로 ,를 꼭 써줘야 한다.

my_tuple_3 = (1, 'a', 3, 'b', 5)

my_tuple = (1, 'a', 3, 'b', 5)

# 인덱싱
print(my_tuple[1]) # a

# 슬라이싱
print(my_tuple[2:4]) # (3, 'b')
print(my_tuple[:3]) # (1, 'a', 3)
print(my_tuple[3:]) # ('b', 5)
print(my_tuple[0:5:2]) # (1, 3, 5)
print(my_tuple[::-1]) # (5, 'b', 3, 'a', 1)

# 길이
print(len(my_tuple)) # 5

# my_tuple = (1, 'a', 3, 'b', 5)

# # TypeError: 'tuple' object does not support item assignment
# my_tuple[1] = 'Z'

x, y = (10, 20)

print(x) # 10
print(y) # 20

# 파이썬은 쉼표를 튜플 생성자로 사용하니 괄호는 생략 가능
x, y = 10, 20

my_range_1 = range(5)
my_range_2 = range(1, 10)

print(my_range_1) # range(0, 5)
print(my_range_2) # range(1, 10)

# 리스트로 형 변환 시 데이터 확인 가능
print(list(my_range_1)) # [0, 1, 2, 3, 4]
print(list(my_range_2)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

my_dict_1 = {}
my_dict_2 = {'key':'value'}
my_dict_3 = {'apple': 12, 'list': [1, 2, 3]}

print(my_dict_1) # {}
print(my_dict_2) # {'key': 'value'}
print(my_dict_3) # {'apple': 12, 'list': [1, 2, 3]}

my_dict = {'apple': 12, 'list': [1, 2, 3]}

print(my_dict['apple']) # 12
print(my_dict['list']) # [1, 2, 3]

# 값 변경
my_dict['apple'] = 100
print(my_dict) # {'apple': 100, 'list': [1, 2, 3]}

my_set_1 = set()
my_set_2 = {1, 2, 3}
my_set_3 = {1, 1, 1}

print(my_set_1)
print(my_set_2)
print(my_set_3)

my_set_1 = {1, 2, 3}
my_set_2 = {3, 6, 9}

# 합집합
print(my_set_1 | my_set_2) # {1, 2, 3, 6, 9}

# 차집합
print(my_set_1 - my_set_2) # {1, 2}

# 교집합
print(my_set_1 & my_set_2) # {3}

variable = None

print(variable) # None

bool_1 = True
bool_2 = False

print(bool_1) # True
print(bool_2) # False
print(3 > 1) # True
print('3' != 3) # True

# 불변과 가변
my_str = 'hello'
# TypeError: 'str' object does not support item assignment
# my_str[0] = 'z'

my_list = [1, 2, 3]
my_list[0] = 100
# [100, 2, 3]
print(my_list)

list_1 = [1, 2, 3]
list_2 = list_1

list_1[0] = 100
print(list_1) # [100, 2 ,3]
print(list_2) # [100, 2 ,3]

x = 10
y = x

x = 20
print(x) # 20
print(y) # 10


## Practice

greeting = "hello world"

print(greeting[6])
print(greeting[:5])
print(greeting[6:])
print(greeting[::-1])
print(len(greeting))
for i in range(len(greeting)):
    print(greeting[i], end="")
print()
print(''.join(greeting[i] for i in range(len(greeting))), end="")
print()