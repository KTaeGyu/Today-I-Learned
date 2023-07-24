## 목차

1. 데이터 구조
2. 시퀀스 데이터 구조

# 데이터 구조

## 1. 데이터 구조
- 여러 데이터를 효과적으로 사용, 관리하기 위한 구조(str, list, dict 등)

### 1-1. 자료 구조
- 컴퓨터 공학에서는 '자료 구조'라고 함
- 각 데이터의 효율적인 저장, 관리를 위한 구조를 나눠 놓은것

        자료구조    단순구조         정수
                                    실수
                                    문자
                                    문자열
                    -------------------------------------------------
                    선형 구조       순차 리스트
                                    연결 리스트      단순 연결 리스트
                                                    이중 연결 리스트
                                                    원형 연결 리스트
                                    스텍
                                    큐
                                    덱
                    -------------------------------------------------
                    비선형 구조      트리             일반 트리
                                                    이전 트리
                                    그래프           방향 그래프
                                                    무방향 그래프
                    -------------------------------------------------
                    파일 구조        순차 파일
                                    색인 파일
                                    직접 파일

<br>

- 데이터 구조 활용
  - 문자열, 리스트, 딕셔너리 등 각 데이터 구조의 매서드를 호출하여 다양한 기능을 활용하기

<br>

### 1-2. 메서드 (method)
- **객체**에 속한 **함수**
- 객체의 상태를 조작하거나 동작을 수행

<br>

#### 메서드 특징
- 메서드는 클래스(class) 내부에 정의되는 함수
- 클래스는 파이썬에서 **'타입을 표현하는 방법'**이며 이미 은연중에 사용해왔음
- 예를 들어 help 함수를 통해 str을 호출해보면 class 였다는 것을 확인 가능
```python
print(help(str))
'''
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.
 |  ...
 '''
```
- 메서드는 어딘가(클래스)에 속해 있는 *함수*이며, 각 데이터 타입별로 다양한 기능을 가진 메서드가 존재

<br>

#### 메서드 호출 방법
- 데이터 타입 객체.메서드()
```python
# 예시
'hello'.capitalize() # Hello

nums = [1, 2, 3]
numbers.append(4)

print(nums) # [1, 2, 3, 4]
```

<br>

## 2. 시퀀스 데이터 구조
#### Sequence Types
- 여러 개의 값들을 **순서대로 나열**하여 저장하는 자료형(str, list, tuple, range)
    - 특징 : 순서, 인덱싱, 슬라이싱, 길이, 반복
<br>

### 2-1. 문자열
#### 문자열 조회/탐색 및 검증 메서드

    메서드      설명
    s.find(x)   x의 첫 번째 위치를 반환. 없으면, -1을 반환
    s.index(x)  x의 첫 번째 위치를 반환. 없으면, 오류 발생
    s.isalpha() 알파벳 문자 여부
                * 단순 알파벳이 아닌 유니코드 상 Letter (한국어도 포함)
    s.isupper() 대문자 여부
    s.islower() 소문자 여부
    s.istitle() 타이틀 형식 여부

<br>

```python
# .find(x)
print('banana'.find(a)) # 1
print('banana'.find(z)) # -1

# .index(x)
print('banana'.index(a)) # 1
print('banana'.index(z)) # ValueError >> 실행이 멈춤

# .isupper(x) / .islower(x) / .isalpha(x)
string1 = 'HELLO'
print(string1.isupper()) # True
print(string1.islower()) # False
print(string1.isalpha()) # True
print(string1.istitle()) # False
```
- 공식문서에서 메서드 확인하기
  - 라이브러리 레퍼런스 탭에 들어가서 확인 가능
  - 파이썬은 bnf 표기법에 따라 표기되어있음 (따로 공부해볼 것)

<br>

#### 문자열 조작 메서드 (새 문자열 반환)

    메서드                              설명
    s.replace(old, new[,count])         바꿀 대상 글자를 새로운 글자로 바꿔서 반환
    s.strip([chars])                    시작과 끝의 공백이나 특정 문자를 제거
    s.split(sep = None, maxsplit = 1)   공백이나 특정 문자를 기준으로 분리
    'separator'.join([iterable])        구분자로 iterable을 합침
    s.capitalize()                      가장 첫번째 글자를 대문자로 변경
    s.title()                           문자열 내 띄어쓰기 기준으로 각 단어의 첫 글자 대문자 나머지는 소문자로 변환
    s.upper()                           모두 대문자로 변경
    s.lower()                           모두 소문자로 변경
    s.swapcase()                        대 소문자 서로 변경

<br>

```python
text = 'Hello, world!'

# s.replace(old, new[,count])
new_text = text.replace('world', 'Python')
print(new_text) # Hello, Python!

# s.strip([chars])
new_text = text.strip('!')
print(new_text) # Hello, world

# s.split(sep = None, maxsplit = 1)
new_text = text.split(',')
print(new_text) # ['Hello', 'world!']

# 'separator'.join([iterable])
words = ['Hello', 'world!']
new_text = '-'.join(words)
print(new_text) # Hello-world!

# .capitalize(), .title(), .upper(), .swapcase()
print(text.capitalize()) # Hello, world!
print(text.title()) # Hello, World!
print(text.upper()) # HELLO, WORLD!
print(text.swapcase()) # hELLO, WORLD!
```
- 메서드는 이어서 사용 가능
```python
# chained methon
text = 'Hello, world!'

new_text = text.replace('world', 'Python').swapcase()
print(new_text) # hELLO, pYTHON!
```
<br>

### 2-2. 리스트
#### 리스트 값 추가 및 삭제 메서드

    메서드          설명
    L.append(x)     리스트 마지막 항목에 x를 추가
    L.extend(m)     Iterable m의 모든 항목들을 리스트 끝에 추가
    L.insert(i, x)  리스트 인덱스 i에 항목 x를 삽입
    L.remove(x)     리스트 가장 왼쪽에 있는 항목(첫 번째)x를 제거
                    항목이 없을 경우 ValueError
    L.pop(i)        리스트의 인덱스 i에 있는 항목을 반환 후 제거
                    i가 없으면 가장 오른쪽 항목에 적용
    L.clear()       리스트의 모든 항목 삭제

<br>

```python
my_list = [1, 2, 3]

# 추가
my_list.append(4) # 이를 바로 출력하면 함수의 Return이 없으므로 None을 출력함
print(my_list) # [1, 2, 3, 4]

my_list.extend([5, 6]) # append 는 하나의 요소로 인식, [1, 2, 3, 4, [5, 6]]
print(my_list) # [1, 2, 3, 4, 5, 6]

my_list.insert(0, 0)
print(my_list) # [0, 1, 2, 3, 4, 5, 6]

# 삭제
my_list.remove(0)
print(my_list) # [1, 2, 3, 4, 5, 6]

item = my_list.pop()
print(my_list) # [1, 2, 3, 4, 5]
print(item) # 6

my_list.clear()
print(my_list) # []
```

<br>

#### 리스트 값 추가 및 삭제 메서드

    문법                        설명
    L.index(x, start, end)      리스트에 있는 항목 중 가장 왼쪽에 있는 항목 x 의 인덱스를 반환
    L.reverse()                 리스트를 순서를 거꾸로 뒤집음
    L.sort()                    리스트를 정렬 (매개변수 이용가능)
    L.count(x)                  리스트에서 항목 x의 개수를 반환

<br>

```python
my_list = [3, 2, 1]

print(my_list.index(2)) # 1
print(my_list.count(3)) # 0

my_list.sort()
print(my_list) # [1, 2, 3]

my_list.sort(reverse=True)
print(my_list) # [3, 2, 1]



my_list.reverse()
print(my_list) # [1, 2, 3] # 정렬은 안됨
```

<br>

### 2-3. 참고
#### 문자열에 포함된 문자들의 유형을 판별하는 메서드
- isdecimal()   문자열이 모두 숫자 문자(0~9)로만 이루어져 있어야 True
- isdigit()     유니코드 숫자도 True로 인식
- isnumeric()   분수, 지수, 루트 기호도 숫자로 True로 인식

#### sort 메서드 vs sorted 함수
```python
my_list = [3, 2, 1]

print(sorted(my_list)) # [1, 2, 3], 원본은 건드리지 않고 복사본을 반환

print(my_list.sort()) # None, 반환 없이 원본을 변화시킴
```