# Function

<br>

## 목차

1. [함수](#함수)
2. [매개변수와 인자](#2-매개변수와-인자)
3. [함수와 Scope](#3-함수와-scope)
4. [재귀 함수](#4-재귀-함수)
5. [유용한 함수](#5-유용한-함수)
6. [Packing & Unpacking](#6-packing--unpacking)
7. [모듈](#7-모듈)
8. [모듈 활용](#8-모듈-활용)
9. [파이썬 표준 라이브러리](#9-파이썬-표준-라이브러리)
10. [Additional](#10-additionals)

<br>

## 1. [함수](#목차)
- **특정 작업**을 수행하기 위한 **재사용 가능**한 **코드 묶음**<br>
- [x] [Additional](#돌아가기_1)

<br>

- 함수를 사용하는 이유
  - 두 수의 합을 구하는 함수를 정의하고 사용함으로써 코드의 중복을 방지
  - **재사용성**이 높아지고, 코드의 **가독성과 유지보수성** 향상
  ```python
  # 두 수의 합을 구하는 코드
  num1 = 5
  num2 = 3
  sum_result = num1 + num2
  print( sum_result ) # 8
  ```
  ```python
  # 두 수의 합을 구하는 함수
  def get_sum(num1, num2):
    return num1 + num2

  # 함수 사용하여 결과 출력
  num1 = 5
  num2 = 3
  sum_result = get_sum(num1, num2)
  print( sum_result ) # 8
  ```

<br>

### 1.1 내장함수
- 파이썬이 기본적으로 제공하는 함수 (별도의 import 없이 바로 사용 가능)
<br>

---

- 내장 함수 예시
  - 절대값을 만드는 함수 abs
  ```python
  # abs 함수 호출의 반환 값을 result에 할당
  
  result = abs(-1)

  print(result) # 1
  ```
- python documentation 을 검색하여 내장함수를 볼 수 있음
  - 자습서 : 기본적인 내용
  - 라이브러리 레퍼런스 : 조금 더 자세한 내용

<br>

### 1.2 함수 호출
- 함수를 실행하기 위해 함수의 이름을 사용하여 해당 함수의 코드 블로글 실행하는 것
```python
function_name(arguments)
```

---

- 함수 구조
  1. INPUT (=parameter) 
  2. Docstring (함수에 대한 설명), function body 
  3. OUTPUT (= return)
  ```python
  def make_sum(parm1, parm2):
    """이것은 두 수를 받아
    두 수의 합을 반환하는 함수입니다.

    >>> make_sum(1, 2)
    3
    """
    return parm1 + parm2
  ```

<br>

- 함수의 정의와 호출
  ```python
  def greet (name):
    """입력된 이름 값에
    인사를 하는 메세지를 만드는 함수
    """
    message = 'Hello, ' + name
    return message

  # 함수 호출
  result = greet('Alice')
  print(result)
  ``` 
  - 함수 정의(정의)
    - 함수 정의는 def 키워드로 시작
    - def 키워드 이후 함수 이름 작성
    - 괄호안에 매개변수를 정의할 수 있음
    - **매개변수(parameter)** 는 함수에 전달되는 값을 나타냄
  - 함수 body
    - 콜론(:) 다음에 들여쓰기 된 코드 블록
    - 함수가 실행 될 때 수행되는 코드를 정의
    - Docstring은 함수 body 앞에 선택적으로 작성 가능한 함수 설명서
  - 함수 반환 값
    - 함수는 **필요한 경우** 결과를 반환할 수 있음
    - return 키워드 이후에 반환할 값을 명시
    - return 문은 함수의 실행을 종료하고, 결과를 호출 부분으로 반환
    - 참고로, print()는 return이 없음 (None이 return됨)

<br>

## 2. [매개변수와 인자](#목차)
- 매개변수(parameter) : 함수를 **정의**할 때, 함수가 받을 값을 나타내는 변수
- 인자(argument) : 함수를 **호출**할 때, 실제로 전달되는 값
- [x] [Additional](#돌아가기_2)

---

- 매개변수와 인자 예시
```python
def add_numbers(x, y): # x, y는 매개변수
    result = x + y
    return result

a = 2
b = 3
sum_result = add_numbers(a, b) # a, b 는 인자
print(sum_result)
```

<br>

### 2.1 Positional Arguments (위치인자)
- 함수 호출 시 인자의 위치에 따라 전달되는 인자
  - **위치 인자는 함수 호출 시 반드시 값을 전달해야 함**
  ```python
  def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

  greet('Alice', 25) # 안녕하세요, Alice님! 25살이시군요.
  ```

<br>

### 2.2 Default Argument Values (기본 인자 값)
- 함수 정의에서 매개변수에 기본 값을 할당하는 것
- 함수 호출 시 인자를 전달하지 않으면, 기본값이 매개변수에 할당됨
```python
def greet(name, age=30):
  print(f'안녕하세요, {name}님! {age}살이시군요.')

greet('Bob') # 안녕하세요, Bob님! 30살이시군요.
greet('Charlie', 40) # 안녕하세요, Charlie님! 40살이시군요.
```

### 2.3 Keyword Arguments (키워드 인자)
- 함수 호출 시 인자의 이름과 함께 값을 전달하는 인자
- 매개변수와 인자를 일치시키지 않고, 특정 매개변수에 값을 할당할 수 있음
- 인자의 순서는 중요하지 않으며, 인자의 이름을 명시하여 전달
  - **단, 호출 시 키워드 인자는 위치 인자 뒤에 위치해야 함**
  ```python
  def greeting(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')
  
  greet(name='Dave', age=35) # 안녕하세요, Dave님! 35살이시군요.
  greet(age=35, 'Dave') # SyntaxError: positional argument follows keyword argument
  ```

<br>

### 2.4 Arbitrary Argument List (임의의 인자 목록)
- 정해지지 않은 개수의 인자를 처리하는 인자
- 함수 정의 시 매개변수 앞에 '*'(asterisk) 를 붙여 사용하며, 여러개의 인자를 tuple로 처리
```python
def calculate_sum(*args):
    print(args)
    total = sum(args)
    print(f'합계: {total}')

"""
(1, 2, 3)
합계: 6
"""
calculate_sum(1, 2, 3)
```

<br>

### 2.4 Arbitrary Keyword Argument Lists (임의의 키워드 인자 목록)
- 정해지지 않은 개수의 키워드 인자를 처리하는 인자
- 함수 정의 시 매개변수 앞에 '**'를 붙여 사용하며, 여러개의 인자를 dictionary로 묶어 처리
```python
def print_info(**kwargs):
    print(kwargs)

print_info(name='Eve', age=30) # {'name': 'Eve', 'age': 30}
```

<br>

### 2.5 함수 인자 권장 작성순서
- 위치 > 기본 > 가변 > ~~키워드~~ > 가변 키워드
  - 키워드인자와 위치인자는 함께 사용할 수 없음
- 호출 시 인자를 전달하는 과정에서 혼란을 줄일 수 있도록 함
  - **단, 모든 상황에 적용되는 절대적인 규칙은 아니며, 상황에 따라 유연하게 조정될 수 있음**
  ```python
  def func(pos1, pos2, default_arg='default', *args, ~~kwd~~, **kwargs):
    ...
  ```

## 3. [함수와 Scope](#목차)
- [x] [Additional](#돌아가기_3)
- Python의 범위(Scope)
  - 함수는 코드 내부에 **local scope**를 생성하며, 그 외의 공간인 **global scope**로 구분
  - scope
    - global scope : 코드가 어디에서든 참조할 수 있는 공간
    - local scope : **함수가 만든** scope (함수 내부)에서만 참조 가능
  - variable
    - global variable : global scope 에 정의된 변수
    - local variable : local scope 에 정의된 변수
- Scope 예시
  - num은 local scope에 존재하기 때문에 global에서 사용할 수 없음
  - 이는 변수의 **수명주기**와 연관이 있음 
  ```python
  def func():
    num = 20 # local
    print('local', num)

  func()

  print (num) # NameError: name 'num' is not defined
  
  num = 3 # global
  print (num) # 3
  ```
- 변수 수명주기(lifecycle)
  - 변수의 수명주기는 변수가 선언되는 위치와 스코프에 따라 결정됨
  1. built-in scope
     - 파이썬이 실행된 이후부터 영원히 유지
  2. global scope
     - 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
  3. local scope
     - 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지
- 이름 검색 규칙(Name Resolution)
  - 파이썬에서 사용되는 이름(식별자)들은 특정한 이름공간(namespace)에 저장되어 있음
  - 아래와 같은 순서로 이름을 찾아 나가며, LEGB Rule이라고 부름
    1. Local scope: 지역 범위(현재 작업 중인 범위)
    2. Enclosed scope: 지역 범위 한 단계 위 범위
    3. Global scope: 최상단에 위치한 범위
    4. Built-in scope: 모든 것을 담고 있는 범위(정의하지 않고 사용할 수 있는 모든 것)
    > local < Enclosed < Global < Built-in
  - **함수 내에서는 바깥 Scope의 변수에 접근 가능하나 수정은 할 수 없음**
  ```python
  num = 3 # global

  def func():
    print(num) # 바깥에서 찾아올 수 있으나, 좋은 방법은 아님

  func() # 3
  ```
- LEGB Rule 예시
  - sum이라는 이름을 global scope에서 사용하게 되면서 기존에 built-in scope에 있던 내장함수 sum을 사용하지 못하게 됨
  - sum을 참조 시 LEGB Rule에 따라 global에서 먼저 찾기 때문
  ```python
  print(sum[1, 2, 3]) # 6
  
  sum = 10

  print(sum) # 10

  print(sum[1, 2, 3]) # TypeError: 'builtin_function_or_method' object is not subscriptable 
  ```
  ```python
  a = 1
  b = 2

  def enclosed():
    a = 10
    c = 3

    def local(c):
        print(a, b, c) 
    
    local(500) # 10, 2, 500
    print(a, b, c) 

  enclosed() # local(500)\n 10, 2, 3
  print(a, b) # 1 2
  ```
- 'global' 키워드
  - 변수의 스코프를 전역 범위로 지정하기 위해 사용
  - 일반적으로 함수 내에서 전역변수를 수정하려는 경우에 사용
  ```python
  num = 0 # 전역 변수

  def increment():
    global num # num를 전역 변수로 선언
    num += 1
  
  print(num) # 0
  increment()
  print(num) # 1
  ```
- 'global' 키워드 주의사항
  - global 키워드 선언 전에 접근시
  ```python
  num = 0

  def increment():
    # SyntaxError: name 'num' is used prior to global declaration
    print(num)
    global num
    num += 1
  ```
  - 매개변수에 global 사용 불가
  ```python
  num = 0

  def increment(num):
    # SyntaxError: name 'num' is parameter and global
    global num
    num += 1
  ```
- global 키워드는 가급적 사용하지 않는 것을 권장
- 함수로 값을 바꾸고자 한다면 항상 **인자**로 넘기고 함수의 **반환 값**을 사용하는 것을 권장

<br>

## 4. [재귀 함수](#목차)
- [x] [Additional](#돌아가기_4)
- 재귀 함수 특징
  - 특정 알고리즘 식을 표현할 때 변수의 사용이 줄어들며, 코드의 가독성이 높아짐
  - 1개 이상의 base case(종료되는 상황)가 존재하고, 수렴하도록 작성
- 재귀 함수 예시 - 팩토리얼
  - n! = n*(n-1)! = n*(n-1)*(n-2)! ...
  - f(4) = 4*f(3) = ...
  ```python
  def factorial(n):
    # 종료 조건: n이 0이면 1을 반환
    if n == 0:
        return 1
    # 재귀 호출: n과 n-1의 팩토리얼을 곱한 결과를 반환
    return n * factorial(n - 1)

  # 팩토리얼 계산 예시
  result = factorial(5)
  print(result) # 120
  ```
  - factorial 함수는 자기 자신을 재귀적으로 호출하여 입력된 숫자 n의 팩토리얼을 계산
  - 재귀 호출은 n이 0이 될 때까지 반복되며, 종료 조건을 설정하여 재귀 호출이 멈추도록 함
  - 재귀 호출의 결과를 이용하여 문제를 작은 단위의 문제로 분할하고, 분할된 문제들의 결과를 조합하여 최종 결과를 도출
- **재귀 함수 주의사항**
  1. 종료 조건을 명확히
  2. 반복되는 호출이 종료 조건을 향하도록

<br>

## 5. [유용한 함수](#목차)
- [x] [Additional](#돌아가기_5)

### map(function, iterable)
- 순회 가능한 데이터구조(iterable: 반복 가능한 객체)의 모든 요소에 함수를 적용하고, 그 결과를 map object로 반환
```python
numbers = [1, 2, 3]
result = map(str, numbers)

print(result) # <map object at 0x000001DD74D513D0>
print(list(result)) # ['1', '2', '3']

result = []
# map을 사용하지 않는 방법
for number in numbers:
    result.append(str(number))

print(result) # ['1', '2', '3']
```
```python
# map 활용법
## 1
def my_func(x):
    result = x * 2
    return result

result2 = map(my_func, numbers) # 각각에 내가 정의한 함수를 적용

## 2
sys.stdin = open('input.txt')

T = int(input())

K, N, M = map(int, input().split())

print(K, N, M) # [3, 6, 9]

## map을 사용하지 않으면?
result = input().split() 

print(result) # ['3', '6', '9']
```

<br>

### zip(*iterables)
- 임의의 iterable을 모아 튜플을 원소로 하는 zip object를 반환
```python
# 예시_1
girls = ['jane', 'ashley']
boys = ['peter', 'jay']
pair = zip(girls, boys)

print(pair) # <zip object at 0x0000022C5E61EF80>
print(list(pair)) # [('jane', 'peter'), ('ashley', 'jay')]

# 예시_2
name = ['Alice', 'Bob', 'Charlie']
ages = [30, 25, 35]
cities = ['New York', 'London', 'Paris']

for name, age, city in zip(names, ages, cities):
    print(f'{name}is {age} yearsold and lives in {city}.')

# 두 개의 리스트를 딕셔너리로 변환하기
keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict = dict(zip(keys, values))
print(my_dict) # {'a': 1, 'b': 2, 'c': 3}
```

<br>

### lambda 함수
- 이름 없이 정의되고 사용되는 **익명 함수**
- lambda 함수 구조
  - lambda 키워드
    - 람다 함수를 선언하기 위해 사용되는 키워드이다.
  - 매개변수
    - 함수에 전달되는 매개변수들
    - 여러 개의 매개변수가 있을 경우 쉼표로 구분
  - 표현식
    - 함수의 실행되는 코드 블록으로, 결과값을 반환하는 표현식으로 작동함
```python
lambda 매개변수: 표현식
```
- lambda 함수 예시
  - 간단한 연산이나 함수를 한 줄로 표현할 때 사용
  - 함수를 매개변수로 전달하는 경우에도 유용하게 활용
```python
# lambda 함수 (좋은 예시는 아님)
addition = lambda x, y: x + y

result = addition(3, 5)
print(result) #8

# lambda 함수 없이 플이
def addition(x, y):
    return x + y

result = addition(3, 5)
print(result) # 8
```
```python
# lambda 실제 사용
# map + lambda
number = [1, 2, 3, 4, 5]

result = list(map(lambda x: x * 2, numbers))

print(result) # [2, 4, 6, 8, 10]

# lambda 함수 없이
def double_number(x):
    return x * 2

result = list(map(double_number, numbers))

print(result) # [2, 4, 6, 8, 10]
```

<br>

## 6. [Packing & Unpacking](#목차)

## 7. [모듈](#목차)

## 8. [모듈 활용](#목차)

## 9. [파이썬 표준 라이브러리](#목차)

## 10. [Additionals](#목차)

### [돌아가기_1](#1-함수)
- 함수의 정의 및 선언 방법
  - **매개변수**와 **반환 값**은 있을 수도, 없을 수도 있다. (총 4가지 유형)
```python
def 함수명(매개변수):
    code... # 함수 바디
    ...
    return 반환값
```
- 함수 호출
```python
함수명(인자)
```
```python
def get_sum(num1, num2):
    return num1 + num2

num1 = 5
num2 = 3
sum_result = get_sum(num1, num2)
print( sum_result ) # 8

#1. 매개변수가 없는 함수로 변형 -> 출력 결과는 같게
def get_sum_1():
    num1, num2 = 5, 3
    return num1 + num2

result = get_sum_1()
print(result) # 8

#2. 반환 값이 없는 함수로 변형 -> 출력 결과는 같게
def get_sum_2(num1, num2):
    result = num1 + num2
    print(result)

get_sum_2(5, 3) # 8
```
- 파이썬 내장함수는 **공식 문서**에서 **꼭** 공부해볼 것

<br>


### [돌아가기_2](#2-매개변수와-인자)
```python
# 위치(positional) 인자 (para/ arg): 정해진 위치에서 할당됨
def greet(name, age):
    print(f'{name} : {age}')

greet('Alice', 25) # Alice : 25
```
```python
# 기본(Default) 인자 값 (para = defalt): 위치에 값이 없을 경우 자동으로 들어가는 값, 반드시 뒤에서부터 할당해야 한다.
def greet(name, age = 40):
    print(f'{name} : {age}')

greet('Alice') # Alice : 40
greet('Alice', 25) # Alice : 25
```
```python
# 키워드(keyword) 인자 (key/ key = value): 인자에 키워드를 주어 순서를 바꿔도 상관이 없도록 함
def greet(name, age):
    print(f'{name} : {age}')

greet(name = 'Alice', age = 25) # Alice : 25
greet(age = 25, name = 'Alice') # Alice : 25
```
```python
# 가변 인자 목록 (*para/ arg1, arg2): 여러개의 인자를 튜플로 처리
def greet(*args): # input : 1 2 3 4 5
    print(args) # (1, 2, 3, 4, 5) : 튜플
    total = sum(args)
    print(f'합계 : {total}') # 합계 : 15
```
```python
# 가변 키워드 인자 목록 (**kwargs/ arg1 = value1, arg2 = value2): 여러개의 인자를 딕셔너리 형식으로 처리
def info(**kwargs):
    print(kwargs) # {name:'Eve', 'age':30, 'height':175.3}

info(name='Eve', age=30, height=175.3)
```

<br>

### [돌아가기_3](#3-함수와-scope)
- Scope
```python
# built-in scope : 내장함수 (len(), print(), input(), ...)

# global variable
z = 0

def outer():
    # local variable
    x = 1 
    print(x + z, end ='') # 1

    def inner():
        # local variable
        y = 2
        print(x + y + z) # x: enclosed variable
    
    inner() # 3

outer() # 13
```
- 실습
```python
a, b, c, = 1, 2, 3

def enclosed():
    a, b, c, = 4, 5, 6
    def local(c):
        print(a, b, c)

    local(500) # 4, 5, 500
    print(a, b, c) # 4, 5 ,6

enclosed()
print(a, b, c) # 1, 2, 3
```
```python
## global 키워드
a, b, c, = 1, 2, 3

def enclosed():
    global a, b, c # a, b, c 를 이제부터 글로벌 변수로 다루겠다는 뜻
    a, b, c, = 4, 5, 6
    def local(c):
        print(a, b, c)

    local(500) # 4, 5, 500
    print(a, b, c) # 4, 5 ,6

enclosed()
print(a, b, c) # 1, 2, 3
```

<br>

### [돌아가기_4](#4-재귀-함수)
- 재귀함수는 **1. 종료 조건을 명확히**, **2. 반복되는 호출이 종료 조건을 향하도록** 작성
```python
def my_sum(n):
    result += n
    return my_sum(n-1)

my_sum(5)
```

<br>

### [돌아가기_5](#5-유용한-함수)
```python
# map(function, iterables)
a = map(int, input().split())
```
```python
# zip(*iterables)
names = ['a', 'b', 'c']
ages = [1, 2, 3]
cities = ['A', 'B', 'C']

for name, age, city in zip(names, ages, cities)
    print(f'{name} : {age} : {city}') # a : 1 : A / b : 2 : B / c : 3 : C
```
- lambda 함수
  1. 1회성이므로 함수 명이 필요 없다.
  2. 표현식의 결과가 반환됨
```python
# lambda 매개변수 : 표현식

# map() 함수를 사용하여 numbers 리스트의 각 요소가 제곱된 값들로 이루어진 새로운 리스트 생성
numbers = [1, 2, 3, 4, 5]

result = map(lambda x : x**2, numbers)

print(list(result))
```