## 목차

# Java 기본 문법

## 1. Java 기본

### 1-1. CS 기본
#### 운영체제와 프로그램
- 프로그램 (Program): 컴퓨터에서 실행될 때 특정 작업(specific task)을 수행하는 일련의 명령어 들의 모음(집합)
- 운영체제 (Operating System, OS): 시스템 하드웨어를 관리할 뿐 아니라 응용 소프트웨어를 실행하기 위하여 하드웨어 추상화 플랫폼과 공통 시스템 서비스를 제공하는 시스템 소프트웨어

<br>

#### 컴퓨터의 자료표현
- 비트 (Bit)
- 바이트 (Byte)
- 2진수 (Binary)

<br>

#### 자바 가상 머신(JVM)
- 자바 바이트코드를 실행할 수 있는 주체
- 자바 바이트코드는 플랫폼에 독립적이며 모든 JVM은 자바 가상 머신 규격에 정의된 대로 자바 바이트코드를 실행

      JAVA 원시 프로그램(Class) >> 컴파일 >> 자바바이트코드 >> JVM (Mac or window or Linux)

<br>

### 1-2. Java 기초
#### Hello SSAFY를 출력하여 보자.
```java
import java.lang.*;
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello SSAFY!!!")
    }
}
```

<br>

#### main method
- 실행 명령인 java 를 실행 시 가장 먼저 호출되는 부분
- 만약, Application 에서 main() 메소드가 없다면 절대로 실행 될 수 없음
- Application의 시작 -> 특정 클래스의 main() 실행
- 형태 (고정된 형태)
```java
    public static void main(String[] args) { }
```

<br>

#### 주석
- //내용 : 해당 기호가 있는 위치부터 그 줄 끝까지 주석처리
- /\*내용\*/ : 해당 범위의 내용 주석처리
- /\*\*내용\*/ : Documentation API 를 위한 주석 처리
```java
// 해당 줄을 주석처리 합니다.
/*
    해당 범위의 내용을 주석처리 합니다
    */
/**
 * Documentation API를 위한 주석처리 입니다.
 */
```

<br>

#### 출력문
- print
- println
- printtf
  - %d : 정수
  - %f : 실수
  - %c : 문자
  - %s : 문자열
  
<br>

## 2. 변수와 자료형

### 2-1. 변수
- 정의
  - 데이터를 저장할 메모리의 위치를 나타내는 이름
  - 메모리 상에 데이터를 보관할 수 있는 공간을 확보
  - 적절한 메모리 공간을 확보하기 위해서 변수의 타입 등장
  - '='를 통해서 CPU에게 연산작업을 의뢰
- 메모리 단위
  - 0과 1을 표현하는 bit
  - 8bit = 1byte

<br>
- 작성규칙
  - 대소문자를 구분한다.
  - 공백은 허용되지 않는다.
  - 숫자로 시작할 수 없다.
  - '$'와 '_'를 변수이름에 사용할 수 있다. 이외의 특수문자는 허용하지 않는다.
  - 예약어(keyword, : 자바문법을 위해서 미리 지정되어 있는 단어)는 사용할 수 없다.
  - 합성어의 경우 주로 camelCase를 활용한다.
  - 한글을 이용한 변수 작명 가능 ( 권장X )

<br>

- 자바 예약어 목록

        abstract    default     if          private     throw
        boolean     do          implements  protected   throws
        break       double      import      public      transient
        byte        else        instanceof  return      try
        case        extends     int         short       void
        catch       final       interface   static      volatile
        char        finally     long        super       while
        class       float       native      switch
        const       for         new         synchronized
        continue    goto        package     this

<br>

### 2-2. 자료형 (Data type)
- 기본 자료형(Primitive Type)과 참조 자료형(Reference Type, 기본 자료형 8가지 외 모든 것)

<br>

#### 기본 자료형 : 미리 정해진 크기의 Memory Size 표현, 변수 자체에 값 저장

    타입    세부 타입   데이터형     크기    기본값          값의 범위
    논리형              boolean             false          true/false
    문자형              char       2byte    null(\u0000)   0 ~ 65,535
    숫자형  정수형       byte       1byte   (byte)0        -128 ~ 127
                        short      2byte   (short)0       -32,768~32,767
                        int        4byte    0             -2^31 ~ 2^31-1
                        long       8byte    0L            -2^63 ~ 2^63-1
            실수형      float       4byte   0.0f
                        double     8byte    0.0d

<br>

### 2-3. 변수와 자료형
- 선언
  - 자료형 변수명;
  - Ex : int age; String name;
- 저장(할당)
  - 변수명 = 저장할 값;
  - Ex : age = 30; name = "철수";
- 초기화
  - 자료형 변수명 = 저장할 값;
  - Ex : int age = 30;

### 2-4. 형변환
- 자동 (묵시적, 암묵적) 형변환이 가능한 방향

      byte >> short >> int >> long >> float >> double
      char >> int

<br>

## 3. 연산자

## 4. 제어문 (조건문 & 반복문)