## 목차

1. [데이터 구조](#1-데이터-구조)
2. [시퀀스 데이터 구조](#2-시퀀스-데이터-구조)
   1. [문자열](#2-1-문자열)
   2. [리스트](#2-2-리스트)
   3. [참고](#2-3-참고)
3. [비시퀀스 데이터 구조](#3-비시퀀스-데이터-구조)
   1. [세트](#3-1-세트)
   2. [딕셔너리](#3-2-딕셔너리)
4. [복사](#4-복사)

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

<br>

## 3. 비시퀀스 데이터 구조
### 3-1. 세트
- 고유한 항목들의 정렬되지 않은 컬렉션

<br>

#### 세트 메서드

    메서드              설명
    s.add(x)            세트에 항목을 추가, 이미 있다면 변화 없음
    s.clear()           세트의 모든 항목을 제거
    s.remove(x)         세트에서 항목을 제거, 항목이 없을 경우 Keyerror
    s.pop()             세트에서 랜덤하게 항목을 반환하고, 해당 항목을 제거
    s.discard(x)        세트에서 항목을 제거
    s.update(iterable)  세트에 다른 이터러블 요소를 추가

<br>

```python
my_set = {1, 2, 3}

# .add(x)
my_set.add(4)
print(my_set) # {1, 2, 3, 4}

# .clear()
my_set.clear()
print(my_set) # set()

# .remove(x)
my_set = {1, 2, 3, 4}
my_set.remove(2)
print(my_set) # {1, 3, 4}

my_set.remove(2)
print(my_set) # KeyError

# .discard()
my_set.discard(1)
print(my_set) # {3, 4}

my_set.discard(1)
print(my_set) # 없어도 에러가 나지 않음

# .pop()
element = my_set.pop()
print(element) # 3
print(my_set) # {4}

# .update(iterable)
my_set.update([4, 5, 1, 2])
print(my_set) # {1, 2, 3, 4, 5}
```

<br>

---
### 추가 설명
#### 해시테이블 자료구조 (세트의 pop 구조)
- 데이터를 효율적으로 저장하고 검색하기 위해 사용되는 자료 구조
- 키-값 쌍을 연결하여 저장하는 방식
- 키를 해시 함수를 통해 해시 값으로 변환하고, 이 값을 인덱스로 사용하여 데이터를 저장하거나 검색
  - 이렇게 하면 데이터의 검색이 매우 빠르게 이루어짐
- 파이썬에서 세트의 요소와 딕셔너리의 키는 해시 테이블을 이용하여 중복되지 않는 고유한 값을 저장
- 세트 내의 각 요소는 해시 함수를 통해 해시 값으로 변환되고, 이 해시 값을 기반으로 해시 테이블에 저장됨
- 마찬가지로 딕셔너리의 키는 고유해야 하므로, 키를 해시 함수를 통해 해시 값으로 변환하여 해시 테이블에 저장
- 따라서 세트와 딕셔너리의 키는 매우 빠른 탐색 속도를 제공하며, 중복된 값을 허용하지 않음
#### 해시
- 임의의 크기를 가진 데이터를 고정된 크기의 고유한 값으로 변환하는 것
- 이렇게 생성된 고유한 값은 해당 데이터를 식별하는 데 사용될 수 있음
- 일종의 "지문"과 같은 역할
- 지문은 개인을 고유하게 식별하는 것처럼, 해시 값은 데이터를 고유하게 식별
- 파이썬에서는 해시 함수를 사용하여 데이터를 해시 값으로 변환하며, 이 해시 값은 정수로 표현됨
#### set의 pop메서드 예시
- set에서 임의의 요소를 제거하고 반환
- 실행할 때마다 다른 요소를 얻는다는 의미의 "무작위"가 아니라 "임의"라는 의미에서 "무작위"
    - by arbitraty the docs don't mean random
- 파이썬이 해시 함수의 동작 방식은 객체의 타입에 따라 달라짐
- 정수와 문자열은 서로 다른 타입이며, 이들의 해시값을 계산하는 방식도 다름
- 정수 타입의 경우, 정수 값 자체가 곧 해시값이 됨
  - 즉, 같은 정수는 항상 같은 해시 값을 가짐
  - 해시 테이블에 정수를 저장할 때 효율적인 방법
  - 예를 들어, hash(1)과 hash(2)는 항상 서로 다른 해시 값을 갖지만, hash(1)은 항상 동일한 해시 값을 갖게 됨
- 반면에 문자열은 가변적인 길이를 갖고 있고, 문자열에 포함된 각 문자들의 유니코드 포인트 등을 기반으로 해시 값을 계산
  - 이로 인해 문자열의 해시 값은 문자열의 내용에 따라 다르게 계산됨
#### 해시 함수
- 주어진 객체의 해시 값을 계산하는 함수
- 해시 값은 객체의 고유한 식별자로 사용할 수 있으며, 해시 테이블과 같은 자료 구조에서 빠른 검색을 위해 사용됨
  - 리스트와 딕셔너리는 해시 가능성(hashable)이 없기 때문에 '세트의 요소'나 '딕셔너리의 키'로 사용이 불가능하다.
  - 해시 충돌?

<br>

    해시테이블
    주소                           |값
    -------------------------------|---------
    해시 함수가 만듦                |
    세트 요소 or 딕셔너리 키        |
    문자열은 주소값이 랜덤           |
    정수는 해시 주소가 그대로 정수   |

<br>

- set의 pop은 에서 주소 값 순서대로 뽑는다.
- 따라서 정수는 항상 뽑는 순서가 일정 (해시 테이블의 주소 순서)
- 그러나, 문자의 경우는 랜덤 출력 (매번 실행될 때마다 해시 값이 달라짐)
---

<br>

#### 세트 집합 메서드

    메서드                  설명                                                      연산자
    set1.difference(set2)    set1 에는 있지만, 2에는 없는 항목으로 세트를 생성 후 반환   set1 - set2
    set1.intersection(set2)  set1 과 2 모두 들어있는 항목으로 세트를 생성 후 반환        set1 & set2
    set1.issubset(set2)      set1 의 항목이 모두 2 에 들어있으면 True 를 반환           set1 <= set2
    set1.isuperset(set2)     set1 가 2 의 항목을 모두 포함하면 True를 반환              set1 >= set2
    set1.union(set2)         set1 and/or 2에 들어있는 항목으로 세트를 생성 후 반환       set1 | set2

<br>

- 메서드와 연산자는 결과가 같음
```python
set1 = {0, 1, 2, 3}
set2 = {2, 3, 4, 5}

set1.difference(set2) # {0, 1, 4, 5}
set1.intersection(set2) # {2, 3}
set1.issubset(set2) # False
set1.isuperset(set2) # False
set1.union(set2) # {0, 1, 2, 3, 4, 5}
```

<br>

### 3-2. 딕셔너리
- 고유한 항목들의 정렬되지 않은 컬랙션

#### 딕셔너리 메서드

    메서드              설명
    D.clear()           딕셔너리 D의 모든 키/값 쌍을 제거
    D.get(k, v=None)    키에 연결된 값을 반환, 키가 없으면 v를 반환 (v가 없으면 None)
    D.keys()            딕셔너리의 키를 모은 객체를 반환
    D.values()          딕셔너리의 값을 모은 객체를 반환
    D.items()           딕셔너리의 키/값 쌍을 모은 객체를 반환
    D.pop(k, v)         딕셔너리에서 키를 제거하고 연결됐던 값을 반환, 없으면 v 반환 (v가 없으면 에러)
    D.setdefault(k, v)  딕셔너리에서 키와 연결된 값을 반환 (v가 없다면 여기서 끝)
                        키가 딕셔너리의 키가 아니면 값 v와 연결한 키를 딕셔너리에 추가하고 v를 반환
    D.update(other)     other 내 각 키에 대해 딕셔너리에 있는 키라면,
                        딕셔너리에 있는 그 키의 값을 other에 있는 값으로 대체.
                        othrt 에 있는 각 키에 대해 딕셔너리에 없는 키라면,
                        키/값 쌍을 딕셔너리에 추가

<br>

```python
dict = {'key1': 'value1', 'key2': 2}

# .get(k[, default])
print(dict.get('key1')) # value1
print(dict.get('key3')) # None
print(dict.get('key3', 'no_data')) # no_data

# D[k]
print(dict['key3']) # KeyError

# .keys()
print(person.keys()) # ['key1', 'key2']
for k in dict.keys():
    print(k) # key1 \n key2

# .values()
print(person.values()) # ['value1', 2]
for v in dict.values():
    print(k) # value1 \n 2

# .items()
print(person.items()) # [('key1', 'value1'), ('key2', 2)]
for k, v in dict.items():
    print(k, v) # key1 value1 \n key2 2

# .pop(k[, default])
print(dict.pop('key2')) # 2
print(dict) # {'key1': 'value1'}

print(dict.pop('key2', None)) # None
print(dict.pop('key2')) # KeyError

# .setdefault(k, v)
print(dict.setdefault('key3', 'value3')) # value3
print(dict) # {'key1': 'value1', 'key3': 'value3'}

# .update(other)
other_dict = {'key3': 3, 'key4': 'value4'}

dict.update(other_dict)
print(dict) # {'key1': 'value1', 'key3': 3, 'key4': 'value4'}

dict.update(key1=1, key4=4)
print(dict) # {'key1': 1, 'key3': 3, 'key4': 4}

# .clear()
dict.clear() 
print(dict) # {}
```

## 4. 복사
#### 데이터 타입과 복사
- 파이썬에서는 데이터 분류에 따라 복사가 달라짐
- "변경 가능한 데이터 타입"과 "변경 불가능한 데이터 타입"을 다르게 다룸
### 4-1. 변경 가능한 데이터 타입의 복사
```python
# 같은 주소가 할당됨
a = [1, 2, 3, 4]
b = a 
b[0] = 100

print(a) # [100, 2, 3, 4]
```
### 4-2. 변경 불가능한 데이터 타입의 복사
```python
# 다른 주소가 할당됨
a = 20
b = a 
b = 10

print(a) # 20
```
### 4-3. 복사 유형
1. 할당 (Assignment)
    - 리스트 할당
        ```python
        # 같은 주소
        lst1 = [1, 2, 3]
        lst2 = lst2
        
        lst2[0] = 100
        print(lst1, lst2) # [100, 2, 3] [100, 2, 3]
        ```
2. 얕은 복사 (Shallow copy)
    - 리스트 얕은 복사
        ```python
        lst1 = [1, 2, 3]
        lst2 = lst1[:] # == (lst2 = lst1.copy()) == (lst2 = list(lst1))
        
        lst2[0] = 100
        print(lst1, lst2) # [1, 2, 3] [100, 2, 3]
        ```
    - 얕은 복사의 한계
        ```python
        lst1 = [1, 2, [3, 4]]
        lst2 = lst1[:]
        
        lst2[2][0] = 100
        print(lst1, lst2) # [1, 2, [100, 4]][1, 2, [100, 4]]
        ```
3. 깊은 복사 (Deep copy)
    - 리스트 깊은 복사
        ```python
        import copy

        lst1 = [1, 2, [3, 4]]
        lst2 = copy.deepcopy(lst1)
        
        lst2[2][0] = 100
        print(lst1, lst2) # [1, 2, [3, 4]] [1, 2, [100, 4]]
        ```