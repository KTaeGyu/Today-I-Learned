## 목차

1. [조건문](#1-조건문-conditional-statement)
2. [반복문](#2-반복문-loop-statement)
3. [참고](#3-참고)
4. [Additional](#4-additional)

<br>

# 제어문 (Control Statement)
- 코드의 실행 흐름을 제어하는데 사용되는 구문
- 조건에 따라 코드 블록을 실행하거나 **반복**적으로 코드를 실행

<br>

## 1. [조건문 (Conditional Statement)](#목차)
- 주어진 조건식을 평가하여 해당 조건이 참(True)인 경우에만 코드 블록을 실행하거나 건너뜀

<br>

- 파이썬 조건문에 사용되는 키워드 : **if / elif / else**

<br>

### 1-1. 'if' Statement
---
- if statement의 기본 구조
```python
if 표현식:
    코드블록
elif 표현식:
    코드블록
else:
    코드블록
```
- 조건문 예시
```python
a = 5

if a > 3:
    print('3 초과') # 3 초과
else:
    print('3 이하')

print(a) # 5
```
- 복수 조건문 예시
  - 조건식을 동시에 검사하는 것이 아니라 **순차적**으로 비교
```python
dust = 35

if dust > 150:
    print('매우 나쁨')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')
```
- 중첩 조건문 예시
```python
dust = 35

if dust > 150:
    print('매우 나쁨')
    if dust >300:
        print('위험해요! 나가지 마세요!')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')
```
- Practice
```python
num = int(input("숫자를 입력하세요 : "))

if num % 2 == 1: 
# if num % 2: 이라고 써도 1 == True 이므로 동작한다. 다만, 명시적이지 못하므로 비추천
    print('홀수입니다.')
else:
    print('짝수입니다')
```


## 2. [반복문 (Loop Statement)](#목차)
- 주어진 코드 블록을 여러 번 반복해서 실행하는 구문
    - 특정 작업을 반복적으로 수행
    - 주어진 조건이 참인 동안 반복해서 수행
- 파이썬 반복문에서 사용되는 키워드 : **for / while**

<br>

### 2-1. 'for' Statement
- **임의의 시퀀스의 항목**들을 그 시퀀스에 들어있는 순서대로 반복
    - 시퀀스의 길이만큼 반복하므로 종료 조건을 따로 필요로하지 않는다.
---
- for state의 기본 구조
```python
for 변수 in 반복 가능한 객체:
    코드블록
```
    반복 가능한 객체 (iterable)
    - 반복문에서 순회할 수 있는 객체
    - 즉, 시퀀스 객체 뿐만 아니라 dict, set 등도 포함
- for 문 원리
  - 리스트 내 첫 항목이 반복 변수에 할당되고 코드블록이 실행됨
  - 다음으로 반복 변수에 리스트의 2번째 항목이 할당되고 코드블록이 다시 실행됨
  - ...마지막으로 반복 변수에 리스트의 마지막 요소가 할당되고 코드블록이 실행됨
```python
items = ['apple', 'banana', 'coconut']

for item in items:
    print(item, end = " ") # apple banana coconut
```
- 문자열 순회
```python
country = 'Korea'

for char in country:
    print(char, end = " ") # K o r e a
```
- range 순회
```python
for i in range(5):
    print(i, end = " ") # 0 1 2 3 4
```
- 리스트 순회
```python
numbers = [4, 6, 10, -8, 5]

for i in range(len(numbers)): # index 로 접근해서 각각 요소에 코드블록을 적용했음
    numbers[i] = numbers[i] * 2

print(numbers) # [8, 12, 20, -16, 10]
```
- 중첩된 반복문 **\*매우 중요**
  - 안쪽 반복문은 outers 리스트의 각 항목에 대해 한 번씩 실행됨
  - print가 호출되는 횟수 => len(outers) * len(inners)
```python
outers = ['A', 'B']
inners = ['C', 'D']

for outer in outers:
    for inner in inners:
        print(outer, inner, end = " / ") # A C / A D / B C / B D
```
- 중첩 리스트 순회
  - 안쪽 리스트 요소에 접근하려면 바깥 리스트를 순회하면서 중첩 반복을 사용해 각 안쪽 반복을 순회
```python
elements = [['A', 'B'], ['C', 'D']]

for elem in elements:
    for item in elem:
        print(item, end = ' ') # A B C D
```

<br>

### 2-2. 'while' Statement
- 주어진 조건이 참(True)인 동안 코드를 반복해서 실행 (종료 조건 필수)
  - 즉, 조건식이 거짓(False)가 될 때까지 반복 
---
- while statement의 기본 구조
```python
(초기식)
while (조건식):
    코드 블록
    (증감식)
```
- while 반복문 예시
```python
a = 0

while a < 3:
    print(a, end = ' ') # 0 1 2
    a += 1

print('끝') # 끝
```
- 사용자 입력에 따른 반복
  - while문을 사용한 특정 입력 값에 대한 종료 조건 활용하기
```python
number = int(input('양의 정수를 입력해 주세요.: '))

while number <= 0:
    if number < 0:
        print('음수를 입력했습니다.')
    else:
        print('0은 양의 정수가 아닙니다.')
    
    number = int(input('양의 정수를 입력해 주세요.: '))

print('잘했습니다!')
```
- while 문은 반드시 **종료 조건**이 필요

<br>

### 정리
---
- 파이썬 반복문에 사용되는 키워드:
  - for : iterable의 요소를 하나씩 순회하며 반복
  - while : 주어진 조건식이 참인 동안 반복

<br>

- 적절한 반복문 활용하기
  - for
    - 반복 횟수가 명확하게 정해져 있는 경우에 유용
    - 예를 들어 리스트, 튜플, 문자열 등과 같은 시퀀스 형식의 데이터를 처리할 때
  - while
    - 반복 횟수가 불명확하거나 조건에 따라 반복을 종료해야 할 때 유용
    - 예를 들어 사용자의 입력을 받아서 특정 조건이 충족될 때까지 반복하는 경우

<br>

### 2-3. 반복 제어
- for문과 while은 매 반복마다 본문 내 모든 코드를 실행하지만, 때때로 일부만 실행하는 것이 필요할 때가 있음
---
- break : 반복을 즉시 중지
- continue : 다음 반복으로 건너뜀
  
<br>

**break 예시**
- 프로그램 종료 조건 만들기
```python
number = int(input('양의 정수를 입력해 주세요.: ')) # -9999

while number <= 0:
    if number == -9999:
        print('프로그램을 종료합니다.') # 프로그램을 종료합니다.
        break

    if number < 0:
        print('음수를 입력했습니다.')
    else:
        print('0은 양의 정수가 아닙니다.')
    
    number = int(input('양의 정수를 입력해 주세요.: '))

print('잘했습니다!') # 잘했습니다!
```
- 리스트에서 짝수 찾기
```python
numbers = [1, 3, 5, 6, 7, 8, 10, 11]
found_even = False

for num in numbers:
    if num % 2 == 0:
        print('첫 번째 짝수를 찾았습니다:', num)
        found_even = True
        break

if not found_even: # if found_even == False
    print('짝수를 찾지 못했습니다.')    
```
- 리스트에서 홀수만 출력하기
  - **현재 반복문의 남은 코드를 건너뛰고 다음 반복으로 넘어감**
```python
numbers = [1, 3, 5, 6, 7, 8, 10, 11]

for num in numbers:
    if num % 2 == 0:
        continue
    print(num, end = ' ') # 1 3 5 7 11

# 다른 방법
for num in numbers:
    if num % 2 == 1:
        print(num, end = ' ') # 1 3 5 7 11 

# continue, break 는 코드가 복잡해지는 단점이 있음
```
- break와 continue 주의사항
  - break와 continue를 남용하는 것은 코드의 가독성을 저하시킬 수 있음
  - **특정한 종료 조건**을 만들어 break을 대신하거나, **if 문을 사용**해 continue 처럼 코드를 건너 뛸 수도 있음
  - 약간의 시간이 들더라도 가능한 코드의 가독성을 유지하고 코드의 의도를 명확하게 작성하도록 노력하는 것이 중요

<br>

### 2-4. List Comprehension
- 간결하고 효율적인 리스트 생성 방법
---

- List Compregension 구조
```python
# 1
[expression for 변수 in iterable]
# 2
list(expression for 변수 in iterable)
```
- List conprehension 활용
```python
# 기존 방식
numbers = [1, 2, 3, 4, 5]
squared_numbers = []

for num in numbers:
    squared_numbers.append(num**2)

print(squared_numbers) # [1, 4, 9, 16, 25]
```
```python
# List comprehension
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num**2 for num in numbers]

print(squared_numbers) # [1, 4, 9, 16, 25]
```

<br>

- [참고] List comprehension 과 if 조건문
```pytho
[expresion for 변수 in iterable if 조건식]

list(expresion for 변수 in iterable if 조건식)
```
```python
# 기존 방식
result = []
for i in range(10):
    if i % 2 == 1:
        result.append(i) # [1 3 5 7 9]
```
```python
# List comprehension
result = [i for i in range(10) if i % 2 == 1] # [1 3 5 7 9]
```

<br>

- Comprehension 남용 시 가독성이 떨어질 수 있다.
  - "Simple is better than complex"
  - "Keep it simple, stupid"

<br><br>

---
- Practice
```python
numbers = ['1', '2', '3']

# 1. for
new_numbers = []
for number in numbers:
    new_numbers.append(int(number))
print(new_numbers) # [1, 2, 3]

# 2. map
new_numbers = list(map(int, numbers))
print(new_numbers) # [1, 2, 3]

# List comprehension
new_numbers = [int(number) for number in numbers]
print(new_numbers) # [1, 2, 3]
```

<br>

## 3. [참고](#목차)

### 3-1. pass
- 아무런 동작도 수행하지 않고 넘어가는 역할
- 문법적으로 문장이 필요하지만 프로그램 실행에는 영향을 주지 않아야 할 때 사용
---
- pass 예시
  1. 코드 작성 중 미완성 부분
       - 구현해야 할 부분이 나중에 추가될 수 있고, 코드를 컴파일하는 동안 오류가 발생하지 안음
    ```python
    def my_function():
       pass
    ```
  2. 조건문에서 아무런 동작을 수행하지 않아야 할 때
    ```python
    if condition:
        pass # 아무런 동작도 수행하지 않음
    else
        #다른 동작 수행
    ```
  3. 무한 루프에서 조건이 충족되지 않을 때 pass를 사용하여 루프를 계속 진행하는 방법
    ```python
    while True:
        if condition:
            break
        elif condition:
            pass
        else:
            print('..')
    ```

<br>

### 3-2. enumerate(iterable, start=0)
- iterable 객체의 각 요소에 대해 인덱스와 함께 반환하는 내장함수

<br>

- enumerate 예시
```python
fruits = ['apple', 'banana', 'cherry']

print(enumerate(fruits)) # <enumerate object at 0x0000021450EF4080>
print(list(enumerate(fruits))) # [(0, 'appele'), [1, 'banana'], [2, 'cherry']]

for index, fruit in enumerate(fruits):
    print(f'인덱스 {index}: {fruit}') # 인덱스 0: apple...
```

<br><br>

- 성능, 최적화
  - 외부요인과 상황에 따라 성능이 다르기 때문에 일반화가 어렵다.<br>
  - 여러 주장이 있으나, 일반적으로는 compre 가 빠르다고 한다. 하지만 다른 함수나 내장함수에 따라 map이 더 빠른 경우도 많다. 파이썬 3 버전 후반에 for 성능에 비약적인 향상이 있었다. 즉, 극단적인 차이는 없다.
  - 따라서, 성능보다 가독성에 초점을 두고 공부를 할 것
    - "작은 효율성에 대해서는, 말하자면 97% 정도에 대해서는, 잊어버려라. 섣부른 최적화는 모든 악의 근원이다." - Donald Knuth
```python
numbers = ['1', '2', '3']

# 1. for
new_numbers = []
for number in numbers:
    new_numbers.append(int(number))
print(new_numbers) # [1, 2, 3]

# 2. map
new_numbers = list(map(int, numbers))
print(new_numbers) # [1, 2, 3]

# List comprehension
new_numbers = [int(number) for number in numbers]
print(new_numbers) # [1, 2, 3]
```
<br>

## 4. [Additional](#목차)
