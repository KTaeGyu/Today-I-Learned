# markdown

1. 가이드 문서
- [Markdown Guide](https://www.markdownguide.org/basic-syntax/)

2. 마크다운 에디터
- [Typora(유료)](https://typora.io)

- [MarkText(무료)](https://github.com/marktext/marktext#download-and-installation)

- [Markdown All in One()](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
  
## markdown 이란?

* markdown : 일반 텍스트로 문서를 작성하는 간단한 방법
  * 주로 개발자들이 텍스트와 코드를 작성해 문서화하기 위해 사용
  * CLI 의 일종
  
<br>

* CLI : 명령어를 통해 사용자와 컴퓨터가 상호 작용하는 방식
  * CLI = Command Line Interface

<br>

* GUI : 그래픽을 통해 사용자와 컴퓨터가 상호작용 하는 방식
  * GUI = Graphic User Interface

## markdown 기본 사용법

* 헤더 : \#
  * \# 의 수가 많아지면 헤더의 크기가 작아진다.
    # 헤더1
    ## 헤더2
    ### 헤더3
* ordered list : 1\., 2\., ... 
  1. tap 을 눌러 들여쓰기
  2. Shift + tap 을 눌러 내어쓰기
  3. Enter 를 두번 눌러 들여쓰기 탈출
  4. 숫자가 달라져도 순서대로 표시됨
<br><br>

- unordered list : *, -, +
  + 셋 중 어떤 기호를 써도 똑같이 표시됨
<br><br>

* check list : - [ ], -[x]
  - [ ] \- [ ] 는 빈 체크리스트
  - [x] \- [x] 는 채워진 체크리스트
<br><br>

* code block : \```code\```
  * Python, Java, C 등을 표시할 수 있다.
  * 해당 언어에서 사용하는 색을 그대로 표시해주므로 가독성이 좋음
```python
print('hello')
```

```c
#include<stdio.h>
int main()
{
    printf("hello word\n");
    return 0;
}
```


* URL hyperlink : [text]\(URL)
 
    [google](https://www.google.com/)

    [naver](https://www.naver.com/)



* Image : ![text]\(URL)

    ![이미지](https://picsum.photos/200/300)

<br>

* text modify : 
  * 기울임 : \*text* or \_sentence_
  
    *기울어진 단어 입니다.*
  * 굵게 : \*\*text** or \_\_sentence\_\_
   
    **굵어진 단어 입니다.**
  * 기울임 및 굵게 : \*\**text*** or \_\_\_sentence\_\_\_
   
    ***굵고 기울어진 단어 입니다.***
  * 취소선 : \~~text~~
  
    ~~취소된 단어 입니다.~~

* horizon : ---
---