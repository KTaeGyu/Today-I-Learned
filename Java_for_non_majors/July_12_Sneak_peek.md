
# Java_Sneak_peek

<br>

## 목차

- [변수](#1-변수)
- [데이터 타입](#2-데이터-타입)
- [연산자](#3-연산자)
- [조건문](#4-조건문)
- [반복문](#5-반복문)

<br>

## 1. [변수](#목차)

- 변수 : 데이터를 담아두는 상자
- 변수 선언

        자료형 변수명; (선언)
        변수명 = 값; (할당)
        
        자료형 변수명 = 값; (초기화)

- 변수 작명 규칙

        1. 알파벳 문자와 숫자, '$', '_' 로 이루어진다. (한글이름도 가능)
        2. 중간에 공백 X
        3. 첫번째 문자는 반드시 알파벳, '$' '_' 로 시작
        4. 대/소문자 구별
        5. 자바 언어 키워드 사용 X

<br>

## 2. [데이터 타입](#목차)

1. Primitive Data Type (기초형)

    : 기본적(일반적)인 값을 기억하는 변수의 type

        논리형 /boolean : true, false
        문자형 /char : 16비트 유니코드, 수치로는 0 ~ 65535
        정수형 /byte : 8비트, -128 ~ 127
            /short : 16비트, -32,768 ~ 32,767
            /int : 32비트, -2^31 ~ 2^31-1
            /long : 64비트, -2^63 ~ 2^63-1
        실수형 /float : 32비트, IEEE 754-1985표준
            /double : 64비트, IEEE 754-1985표준

2. Type Casting
   - Automatic promotions (implict Type Casting)
       - 작은 크기의 타입은 큰 크기의 타입으로 자동으로 형변환 된다.
       - 정수형은 실수형으로 자동형변환 된다.
         - logn var = 100;
         - float fvar = var;
         - int kvar = 'A';
   - Explicit Type Casting
     - 큰 크기의 타입을 작은 크기의 타입으로 변경할 경우
     - 실수형을 정수형의 타입으로 변경할 경우
     - identifier = (target_type) value;
       - float fvar = 100;
       - long var = (long)fvar;

## 3. [연산자](#목차)

    우선순위 /연산자         /연산대상              /연산내용
    1       /[]             /모든 데이터형          /배열요소 지정
            /.              /레퍼런스               /객체 맴버 지정
            /++, --         /정수형                /값 증가, 값 감소
            /+, -           /정수형, 실수형         /부호에 사용
            /~              /정수형                /비트 반전
            /!              /논리형                /논리 반전
            /new            /레퍼런스형             /객체 생성
            /(type)         /모든 데이터 형         /캐스팅 연산자
    2       /*, /, %        /정수형, 실수형         /곱셈, 나눗셈, 나머지
    3       /+, -           /정수형, 실수형         /덧셈, 뺄셈
    4       /<<, >>, >>>    /정수형                 /비트단위 좌우 이동, 비트 비부호화 우이동
    5       /<, <=, >, >=   /정수형, 실수형         /값 대소 비교
    6       /==, !=         /기본 데이터형          /값 비교
    7       /&              /정수형, 논리형         /비트 AND, 논리 AND
    8       /^              /정수형, 논리형         /비트 XOR, 논리 XOR
    9       /|              /정수형, 논리형         /비트 OR, 논리 OR
    10      /&&             /논리형                 /조건 AND
    11      /||             /논리형                 /조건 OR
    12      /?:             /논리형, 모든 데이터형   /조건 삼항
    13      /=, *=, /=, %=  /변수, 모든 데이터형     /대입/할당 연산
            /+=, -=, <<=
            />>=, >>>=
            /&=, ^=, |=

<br>

## 4. [조건문](#목차)

### 4.1 [조건문 (if)](#목차)

---

```java
// expression
if (boolean_expression) {
    Statements
    ..
} else if {
    Statements
    ..
} else if {
    Statements
    ..
} else {
    Statements
    ..
}
```

```java
// case_1

int i = 10;
if( (i % 2) == 0 ) {
    System.out.println( i + "는 짝수" );
}
```
```java
// case_2

boolean flag = true;
if (flag) {
    System.out.println( "참" );
} else {
    System.out.println( "거짓" );
}
```
```java
// case_3

int num = (랜덤한 숫자);
if ( num == (내가 말한 숫자) ) {
    System.out.println( "정답입니다." );
} else {
    if( ( num > (내가 말한 숫자) ) == 0 ) {
    System.out.println( "Up" );
    } else {
    System.out.println( "Down" );
    }
}
```
```java
// case_4

int num = (랜덤한 숫자);
if ( num == (내가 말한 숫자) ) {
    System.out.println( "정답입니다." );
} else if( ( num > (내가 말한 숫자) ) == 0 ) {     
    System.out.println( "Up" );
} else {
    System.out.println( "Down" );
}
```

<br>

### 4.2 [조건문 (switch)](#목차)

---

- 여러가지 값 비교 시 사용
- expr은 반드시 정수형(int, byte, short, char)이어야 함
```java
// expression
switch (expr) {
    case 값1:
        statements;
        break;
    case 값2:
        statements;
        break;
    case 값3:
        statements;
        break;
    default:
        statements;
}
```

<br>

## 5. [반복문](#목차)

### 5.1 [Loop (for)](#목차)

---

```java
// expression
for ( init_expr; boolean_testexpr; alter_expr ) {
    Statement or block;
}

for ( type item : items ) {
    Statement or block;
    ..
}
```
```java
// case_1
int[] nums = {1, 2, 3, 4, 5, 6};

for  (int i = 0; i < nums.length; i++) {
    System.out.println(nums[i])
}
```
```java
// case_2
int[] nums = {1, 2, 3, 4, 5, 6};

for  (int n = nums) {
    System.out.println(n)
}
```

<br>

### 5.2 [Loop (while)](#목차)

---

- 반복문에서 사용되는 문장들
  - break;
  - continue;
  - label;
  - break label;
  - Continue label;
```java
// expression
while (boolean) {
    Statement or block;
    ...
}

do {
    Statement or block;
    ..
} while (boolean);
```

<br>