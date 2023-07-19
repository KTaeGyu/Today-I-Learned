## 목차

[1. HTML](#1-html) <br>
[2. CSS](#2-css) <br>

# 1. [HTML](#목차)

- **HTML** : **H**yper **T**ext **M**arkup **L**anguage
  - Markup Language != Programming Language
  - Markup Tag 의 집합
  - **W3C**(**W**orld**W**ide**W**eb **C**onsortium)에서 표준관리

<br>

- Syntax
  - Element(요소)
    - content 의 type 을 지정
    - Element_name 은 표준으로 정의
  - Attribute(속성)
    - 생략가능
    - Element 의 속성지정
    - attribute_name 과 value set 을 표준으로 정의
  - Comments(주석)
    - <!-- -->
    - 브라우저에선 표시되지 않음
    - 더 읽고 이해하기 쉬움
  - Block level element
    - 새로운 행에 표시
    - 좌우 양쪽으로 최대한 늘어나 가능한 모든 너비를 차지함
    - Ex : \<div\>, \<p\>, \<h1\>, \<form\>, \<table\>, \<li\> ...
  - Inline level element
    - 새로운 행에 표시 되지 않음
    - 필요한 너비만 차지함
    - Ex : \<span\>, \<a\>, \<img\>, \<input\>, \<label\> ...

<br>

- Sections
  - \<article\>
    - 문서의 독립적인 부분을 구성하는 섹션
    - 위젯 등 독립적인 아이템
    - Ex : News, Blog Post, Article
    - article 요소를 중첩할 경우 외부 article 요소와 연관된 내용
  - \<section\>
    - 일반적인 문서 또는 프로그램의 섹션
    - 제목으로 시작하는 컨텐츠의 의미적 그룹
  - \<nav\>
    - 네비게이션 링크로 구성된 섹션
    - 다른 페이지 또는 동일 페이지의 다른 섹션 연결
  - \<aside\>
    - 문서의 주 내용과 관련성이 낮은 내용
    - 일반적으로 사이드바 형태로 표현
    - Ex : 사이트 링크, 광고, nav 요소 그룹
  - \<footer\>
    - 꼬리말
    - 가장 가까운 선행하는 \<section\>의 footer
    - 작성자, 연관 링크, 저작권 등
    - \<address\> 또는 \<nav\> 등의 요소를 포함

<br>

- Grouping
    - \<pre\>
        - Preformatted text
        - Block level elements
        - 공백 문자와 줄 바꿈 문자를 보존
    - \<ol\>
        -  Ordered list
        -  Block level element
        -  Attributes
            -  start = *number*
            -  type = {1|A|a|I|i}
    -  \<ul\>
        -  Unordered list
        -  Block level element
    -  \<li\>
        -  List item
        -  \<ol\> 또는\<ul\> 안에서 하나의 item 을 표현
        -  Attributes
           -  value = *number*, only within \<ol\>
    -  \<div\>
        -  Block level element
        -  Grouping block level elements
        -  No visual changes
- Text Level
    -  \<a\>
        -  Anchor
        -  Hyper link to another page
        -  Inline level element
        -  Attributes
            -  href = URL
            -  targer = {_blank | _parent | _self | _top | *framename*}
            -  hreflag = *language_code*
    - \<span\>
        - Inline level element
        - Grouping inline level elements
        - No visual changes
- Embedded
    - \<img\>
        - Defines an image
        - Inline level element
        - Attributes
            - src = *URL*
            - alt = text, 대체 text
            - height = *pixels* or %
            - width = *pixels* or %
            - usemap = *#map_name*
            - ismap = ismap
    - \<audio\>
        - Audio 콘텐츠 재생
        - Attributes
            - src = *URL*
            - autoplay = autoplay, 자동 재생 여부
            - loop = loop, 반복 재생 여부
            - controls = controls, control 표시 여부
            - preload = {auto | metadata | none}
    - \<video\>
        - Video 콘텐츠 재생
        - Attributes
            - src = *URL*
            - autoplay = autoplay, 자동 재생 여부
            - loop = loop, 반복 재생 여부
            - controls = controls, control 표시 여부
            - preload = preload
            - poster = *URL*, 재생 이전에 표시될 이미지
            - audio = muted
            - width = *pixels*
            - height = *pixels*
    - \<source\>
        - Media 요소의 대체 미디어 자원 지정
        - 다양한 format을 지정하여 fallback 지원
        - Attribute
            - src = *URL*
            - media = *media query*
            - type = *MIME_TPYE*
- Forms
    - \<form\>
        - Block level element
        - 사용자 입력 Data를 Server로 전송
        - Input 요소를 포함
        - Attributes
            - action = *URL*, HTTP Request URL
            - method = {get | post}, HTTP Request Method
            - target = {_blank | _self | _parent | _top | *frame_name*}, Result target
            - accept = *MIME_TYPE*
            - accept-charset = *charset*
            - enctype = {text/plain | multipart/form-data | application/x-www-form-urlencoded}
            - name = *form_name*
    - \<input\>
        - User input
        - Inline level element
        - Elements for user input fields
        - Depending on the type attribute
        - Attributes
            - type = {text | button | checkbox | radio | password | file | image | submit | reset | hidden}
            - name = name, HTTP Request parameter name
            - value = value, HTTP Request parameter value
            - disabled = disabled
            - alt = text, alternate text
    - New input type

            유형                설명                   코드
            이메일 주소         이메일 주소 입력       \<input type="email"\>
            웹 주소             웹페이지 주소 입력     \<input type="url"\>
            숫자(스핀박스)      숫자를 ^v를 눌러 선택   \<input type="number"\>
            숫자(슬라이드막대)   슬라이드 막대로 선택   \<input type="range"\>
            날씨/시간           시간이나 날짜를 선택    \<input type="date"\>
                                                     \<input type="month"\>
                                                     \<input type="weel"\>
                                                     \<input type="time"\>
                                                     \<input type="datetime"\>
                                                     \<input type="datetime-local"\>
            검색상자            입력한 값을 전송       \<input type="search"\>
            색상선택            색상을 선택            \<input type="color"\>

<br>

# 2. [CSS](#목차)

- Cascading Style Sheets
- HTML Element(Markup)의 시각적 표현(Appearance) 정의
- CSS Levels
    - CSS, Earliest Draft in May, 1995
    - 