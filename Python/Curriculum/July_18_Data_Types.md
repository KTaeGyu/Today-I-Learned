# Data Types

## 목차

1. Data Types
2. Numeric Types
3. Sequence Types
4. Non-sequence Types
5. Other Types
6. Collection
7. Type conversion
8. Operator
9. Additionals (가변과 불변 데이터의 메모리 참조 특징)

## 1. Data Types

- 데이터 타입 : 값의 종류와 그 값에 적용 가능한 연산과 동작을 결정하는 속성

- 데이터 타입 분류

        Numeric Type        /int, float, complex
        Text Sequence Type  /str
        Sequence Type       /list, tuple, range
        Non-sequence Type   /set, dict
        기타                /Boolean, None, Function

<br>

- 데이터 타입이 필요한 이유
  - 값들을 구분하고, 어떻게 다뤄야 하는지를 알 수 있음
  - 각 데이터 타입 값들은 각자에게 적합한 함수를 가짐
  - 타입을 명시적으로 지정하면 코드를 읽는 사람이 변수의 의도를 더 쉽게 이해할 수 있고, 잘못된 데이터 타입으로 인한 오류를 미리 예방

## 2. Numeric Type

### 2-1. int : 정수 자료형

---

- 진수 표현
  - 2진수 (binary) : 0b
  - 8진수 (octal) : 0o
  - 16진수 (hexadecimal) : 0x
    ```python
    print(0b10) # 2
    print(0o30) # 24
    print(0x10) # 16

    # 진법 변경 (10진수 -> n진수)
    print(bin(12)) #0b1100
    print(oct(12)) #0o14
    print(hex(12)) #0xc
    ```

### 2-2. float : 실수 자료형

---

- **유한 정밀도** : 프로그래밍 언어에서 float는 실수에 대한 근삿값
  - 컴퓨터 메모리 용량이 한정돼 있고 한 숫자에 대해 저장하는 용량이 제한됨
  - 0.6666666666666666과 1.6666666666666667은 제한된 양의 메모리에 저장할 수 있는 2/3과 5/3에 가장 가까운 값

    ```python
    # 0.6666666666666666
    print(2/3)

    # 1.6666666666666667
    print(5/3)
    ```

- 실수 연산 시 주의사항
  - 컴퓨터는 2진수를 사용, 사람은 10진법을 사용
  - 이때 10진수 0.1은 2진수로 표현하면 0.0001100110011... 같이 무한대로 반복
  - 무한대 숫자를 그대로 저장할 수 없어서 사람이 사용하는 10진법의 근사값만 표시
  - 0.1의 경우 3602879701896397 / 2 ** 55 이며 0.1에 가깝지만 정확히 동일하지는 않음
  - 이런 과정에서 예상치 못한 결과가 나타남
  - 이런 증상을 **Floating point rounding error** 라고 함

<br>

- 실수 연산 시 해결책
  - 두 수의 차이가 매우 작은 수보다 작은지를 확인 (True / Flase 로 확인)
  - math 묘율 활용 (isclose(), 위 방법보다 정확함)

    ```python
    a = 3.2 - 3.1 # 0.1000000000000009
    b = 1.2 - 1.1 # 0.0999999999999987

    # 1. 임의의 작은 수 활용
    print(abs(a - b) <= 1e-10) #True

    # 2. math 모듈 활용
    import math
    print(math.isclose(a, b)) # True
    ```

- 지수 표현 방식
  - e 또는 E를 사용한 지수 표현
    ```python
    # 314 * 0.01
    number = 314e-2

    # float
    print(type(number))

    # 3.14
    print(number)

    # 31400.0
    print(314e2)
    ```

## 3. Sequence Type

- 여러 개의 값들을 **순서대로 나열**하여 저장하는 자료형
  - str, list, tuple, range

<br>

- Sequence Types 특징

      1. 순서 (Sequence)
          - 값들이 순서대로 저장 (정렬X)
      2. 인덱싱 (Indexing)
          -  각 값에 고유한 인덱스(번호)를 가지고 있으며, 인덱스를 사용하여 특정 위치의 값을 선택하거나 수정할 수 있음
      3. 슬라이싱 (Slicing)
          - 인덱스 범위를 조절해 부분적인 값을 추출할 수 있음
      4. 길이 (Length)
          - len() 함수를 사용하여 저장된 값의 개수(길이)를 구할 수 있음
      5. 반복 (Iteration)
          - 반복문을 사용하여 저장된 값들을 반복적으로 처리할 수 있음

<br>

### 3-1. str : 문자열

- 문자들의 순서가 있는 변경 불가능한 시퀀스 자료형

---

<br>

- 문자열 표현
  - 문자열은 단일 문자나 여러 문자의 조합으로 이루어짐
  - 작은따옴표(') 또는 큰따옴표(") 로 감싸서 표현
    ```python
    # Hello, World!
    print('Hello, World!')

    # str
    print(type('Hello, World!'))
    ```

<br>

- 문자열의 시퀀스 특징
    ```python
    my_str = 'hello'

    # 인덱싱
    print(my_str[1]) # e

    # 슬라이싱
    print(my_str[2:4]) # ll

    # 길이
    print(len(my_str)) # 5
    ```

<br>

- 중첩 따옴표
  - 따옴표 안에 따옴표를 표현할 경우
    - 작은따옴표가 들어있는 경우는 큰따옴표로 문자열 생성
    - 큰따옴표가 들어있는 경우는 작은따옴표로 문자열 생성
    ```python
    # 문자열 안에 '작은따옴표'를 사용하려면 큰따옴표로 묶는다.
    print("문자열 안에 '작은따옴표'를 사용하려면 큰따옴표로 묶는다.")

    # 문자열 안에 "큰따옴표"를 사용하려면 작은따옴표로 묶는다.
    print('문자열 안에 "큰따옴표"를 사용하려면 작은따옴표로 묶는다.')
    ```

#### 3-1-1. Escape sequence
- 역슬래시(backslash)뒤에 특정 문자가 와서 특수한 기능을 하는 문자 조합
- 파이썬의 일반적인 문법 규칙을 잠시 탈출한다는 의미

        예약문자    내용(의미)
        \n          줄바꿈
        \t          탭
        \\          백슬래시
        \'          작은따옴표
        \"          큰따옴표

    ```python
    # 철수야 '안녕'
    print('철수야 \'안녕\'')

    '''
    이 다음은 엔터
    입니다.
    '''
    print('이 다음은 엔터\n입니다.')
    ```

#### 3-1-2. String Interpolation : 문자열 내에 변수나 표현식을 삽입하는 방법
- f-string
  - 문자열에 f 또는 F 접두어를 붙이고 표현식을 {expression}로 작성하여 문자열에 파이썬 표션식의 값을 삽입할 수 있음
    ```python
    bugs = 'roaches'
    counts = 13
    area = 'living room'

    # Debugging roaches 13 living room
    print(f'Debugging {bugs} {counts} {area}')
    print('Debugging {} {} {}'.format(bugs, counts, area)) # 이전 방법
    print('Debugging %s %d %s' % (bugs, counts, area)) # 더 이전 방법

    # f-string 응용
    # f-string advanced 검색하여 많은 기능을 찾아볼 것
    greeting = 'hi'
    print(f'{greeting:>10}') # >n : 오른쪽 정렬
    print(f'{greeting:^10}') # ^n : 가운데 정렬
    print(f'{3.141592:.4f}') # .nf : 반올림하여 소숫점 n 자리 까지 표시
    ```

<br>

#### 참조1. 인덱스
- 시퀀스 내의 값들에 대한 고유한 번호로, 각 값의 위치를 식별하는 데 사용되는 숫자

---

        "   h   e   l   l   o   "
    index   0   1   2   3   4
    index   -5  -4  -3  -2  -1

<br>

#### 참조2. 슬라이싱
- 시퀀스의 일부분을 선택하여 추출하는 작업
  - 시작 인덱스와 끝 인덱스를 지정하여 해당 범위의 값을 포함하는 새로운 시퀀스를 생성

---
          0   1   2    3    4
        "   h   e   (l   l)   o   "
    index   0   1   (2   3)   4
    index   -5  -4  -3   -2  -1
```python
my_str[2:3] # ll
```
---
          0    1   2    3    4
        "   (h   e   l)   l    o   "
    index   (0   1   2)   3    4
    index   -5  -4  -3   -2   -1
```python
my_str[:3] # hel
```
---
          0   1   2   3    4
        "   h   e   l   (l   o)   "
    index   0   1   2   (3   4)
    index   -5  -4  -3  -2  -1
```python
my_str[3:] # lo
```
---
          0   1   2    3    4
        "  (h)  e  (l)  l  (o)   "
    index  (0)  1  (2)  3  (4)
    index  -5  -4  -3  -2  -1
```python
my_str[0:5:2] # hlo : step 기능
```
---
          0   1   2    3    4
        "  (h   e   l   l   o)  "
    index   0   1   2   3   4
    index (-5  -4  -3  -2  -1)
```python
my_str[::-1] # olleh : step을 이용한 문자열 뒤집기
```
---
- 문자열은 불변 (변경 불가)
    - 때문에 문자열을 변경하는 문제는 새로운 문자열을 만드는 식으로 풀어야 함
    ```python
    my_str = 'hello'

    # TypeError: 'str' object does not support item assignment
    my_str[1] = 'z'
    ```

<br>

### 3-2. list : 리스트
- 여러 개의 값을 순서대로 저장하는 **변경 가능한** 시퀀스 자료형

---

- 리스트 표현
  - 0개 이상의 객체를 포함하며 데이터 목록을 저장
  - 대괄호([])로 표기
  - 데이터는 어떤 자료형도 저장할 수 있음
    ```python
    my_list_1 = []

    my_list_2 = [1, 'a', 3, 'b', 5]

    my_list_3 = [1, 2, 3, 'python', ['hello', 'world', '!!']]
    ```

<br>

- 리스트의 시퀀스 특징
    ```python
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
    ```
<br>

- 중첩된 리스트 접근
  - 출력값 예상해보기
    ```python
    my_list = [1, 2, 3, 'python', ['hello', 'world', '!!']]

    print(len(my_list)) # 5
    print(my_list[4][-1]) # !!
    print(my_list[-1][1][0]) # w
    ```

<br>

- 리스트는 가변 (변경 가능)
    ```python
    my_list = [1, 2, 3]
    my_list[0] = 100

    print(my_list) # [100, 2, 3]
    ```

<br>

### 3-3. tuple : 튜플
- 여러 개의 값을 순서대로 저장하는 **변경 불가능한** 시퀀스 자료형

---

- 튜플 표현
  - 0개 이상의 객체를 포함하며 데이터 목록을 저장
  - 소괄호(())로 표기
  - 데이터는 어떤 자료형도 저장할 수 있음
    ```python
    my_tuple_1 = ()

    my_tuple_2 = (1,) # 튜플의 자료가 1개라면 ()를 연산으로 인식할 수 있으므로 ,를 꼭 써줘야 한다.

    my_tuple_3 = (1, 'a', 3, 'b', 5)
    ```

<br>

- 튜플의 시퀀스 특징
    ```python
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
    ```

<br>

- 튜플은 불면 (변경 불가)
    ```python
    my_tuple = (1, 'a', 3, 'b', 5)

    # TypeError: 'tuple' object does not support item assignment
    my_tuple[1] = 'Z'
    ```

<br>

- 튜플은 어디에 쓰일까?
  - 튜플의 불변 특성을 사용한 안전하게 여러개의 값을 전달, 그룹화, 다중 할당 등 **개발자가 직접 사용하기 보다 '파이썬 내부 동작'에서 주로 사용됨**
    ```python
    x, y = (10, 20)

    print(x) # 10
    print(y) # 20

    # 파이썬은 쉼표를 튜플 생성자로 사용하니 괄호는 생략 가능
    x, y = 10, 20
    ```

<br>

### 3-4. range
- 연속된 정수 시퀀스를 생성하는 변경 불가능한 자료형

---

- range 표현
  - range(n)
    - 0부터 n-1까지의 숫자 시퀀스
  - range(n, m)
    - n부터 m-1까지의 숫자 시퀀스
    ```python
    my_range_1 = range(5)
    my_range_2 = range(1, 10)

    print(my_range_1) # range(0, 5)
    print(my_range_2) # range(1, 10)
    ```
  - 주로 반복문과 함께 사용 예정
    ```python
    # 리스트로 형 변환 시 데이터 확인 가능
    print(list(my_range_1)) # [0, 1, 2, 3, 4]
    print(list(my_range_2)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ```

## 4. Non-sequence Types

<br>

### 4-1. dict : 딕셔너리
- key - value 쌍으로 이루어진 **순서와 중복이 없는 변경 가능한** 자료형

---

- 딕셔너리 표현
  - key는 변경 불가능한 자료형만 사용 가능 (str, int, float, tuple, range...)
  - value는 모든 자료형 사용 가능
  - 중괄호({})로 표기
    ```python
    my_dict_1 = {}
    my_dict_2 = {'key':'value'}
    my_dict_3 = {'apple': 12, 'list': [1, 2, 3]}

    print(my_dict_1) # {}
    print(my_dict_2) # {'key': 'value'}
    print(my_dict_3) # {'apple': 12, 'list': [1, 2, 3]}
    ```
<br>

- 딕셔너리 사용
  - key를 통해 value에 접근
    ```python
    my_dict = {'apple': 12, 'list': [1, 2, 3]}

    print(my_dict['apple']) # 12
    print(my_dict['list']) # [1, 2, 3]

    # 값 변경
    my_dict['apple'] = 100
    print(my_dict) # {'apple': 100, 'list': [1, 2, 3]}
    ```

<br>

### 4-2. set : 세트
- **순서와 중복이 없는 변경 가능한** 자료형

---

- 세트 표현
  - 수학에서의 집합과 동일한 연산 처리 가능
  - 중괄호({})로 표기
    ```python
    my_set_1 = set() # dict과 곂치기 때문에 빈 set는 set()로 표기한다.
    my_set_2 = {1, 2, 3}
    my_set_3 = {1, 1, 1} # 중복이 없기 때문에 하나로 표시됨

    print(my_set_1) # set()
    print(my_set_2) # {1, 2, 3}
    print(my_set_3) # {1}
    ```

<br>

- 세트의 집합 연산
    ```python
    my_set_1 = {1, 2, 3}
    my_set_2 = {3, 6, 9}

    # 합집합
    print(my_set_1 | my_set_2) # {1, 2, 3, 6, 9}

    # 차집합
    print(my_set_1 - my_set_2) # {1, 2}

    # 교집합
    print(my_set_1 & my_set_2) # {3}
    ```

## 5. Other Types

<br>

### 5-1. None
- 파이썬에서 '값이 없음'을 표현하는 자료현

---

- None 표현
    ```python
    variable = None

    print(variable) # None
    ```
<br>

### 5-2. Boolean
- 참(True)과 거짓(False)을 표현하는 자료형

---

- 불리언 표현
  - 비교 / 논리 연산의 평가 결과로 사용됨
  - 주로 조건/ 반복문과 함께 사용
    ```python
    bool_1 = True
    bool_2 = False

    print(bool_1) # True
    print(bool_2) # False
    print(3 > 1) # True
    print('3' != 3) # True
    ```
<br>

## 6. Collection

- 여러 개의 항목 또는 요소를 담는 자료 구조
  - str, list, tuple, set, dict

        컬렉션 정리
        컬렉션  변경 가능 여부  나열 여부
        str          X            O (시퀀스)
        list         O            O
        tuple        X            O
        set          O            X(논시퀀스)
        dict         O (key:X)    X

<br>

- 불변과 가변의 차이
    ```python
    my_str = 'hello' # 하나의 메모리 주소에 문자열을 모두 넣는다
    my_str[0] = 'z' # TypeError: 'str' object does not support item assignment
 
    my_list = [1, 2, 3] # 각각의 메모리 주소에 넣는다 (객체들의 참조를 모아놓은 컬렉션)
    my_list[0] = 100
    print(my_list) # [100, 2, 3]
    ```

<br>

## 7. Type Conversion
### 7-1. 암시적 형변환
### 7-2. 명시적 형변환

## 8. Operator
### 8-1. 산술 연산자
### 8-2. 복합 연산자
### 8-3. 비교 연산자
### 8-4. 논리 연산자
### 8-5. 맴버십 연산자
### 8-6. 시퀀스형 연산자

## 9. Additional (가변과 불변 데이터의 메모리 참조 특징)

```python
## 가변데이터 list
list_1 = [1, 2, 3]
list_2 = list_1

list_1[0] = 100
print(list_1) # [100, 2 ,3]
print(list_2) # [100, 2 ,3]
# list_2는 list_1과 같은 주소를 보고 있기 때문에 요소가 같이 변경된다.
# 복사 시 위와 같은 문제가 가변 데이터들의 특징이다.


## 불변데이터 str
x = 10
y = x

x = 20
print(x) # 20
print(y) # 10
# x는 주소를 바꾸지만, y는 처음에 바라보던 주소를 그대로 보고 있게 된다.
# 불변 데이터의 특징이다.
```