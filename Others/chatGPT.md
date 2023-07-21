# chatGPT

[SSAFY 공용 문서 및 chatGPT 구현 설명 Notion 링크](https://abit.ly/pb-document)

## chatGPT 란?
* Generative AI : 오디오, 비디오, 이미지, 텍스트, 코드, 시뮬레이션 등의 새로운 콘텐츠를 생성하는 인공지능 모델
  * 최근 언어 및 이미지 분석에서 큰 파급력을 보임

<br>

* chatGPT : GPT 모델을 기반으로 한 대화형 AI
  * GPT = Generative/ Pre-tranined/ Transformer


## chatGPT Program Problem

1. 위 Notion 링크의 설명에 따라 *chatGPT API key* 를 발급받는다.
2. *gpt-program-problem.zip* 의 앞축을 풀고 *VScode* 를 실행시켜 파일을 읽는다.
3. *app.js* 파일을 완성하여 chatGPT 를 구현한다.
   1. **index.html** 파일을 열어 **devtool (F12)** 을 실행시킨다.
   2. 채팅창에 아무 채팅이나 친 후 *devtool* 의 *console* 창을 확인한다.
   3. *console* 창 내의 응답 메세지의 경로를 확인하고, 메세지의 콘텐츠를 **response** 로 저장한다.
   4. **addChat** 함수를 이용하여 채팅창에 메세지를 등록한다.
   5. 앞서 받은 **response** 를 **oldMsg** 변수에 저장한다.
   6. *chatReceive* 함수에 **oldMsg** 를 추가하여 이전 대화에 대한 정보를 추가한다.
4. index.html 을 실행시켜 구현이 되었는지 확인한다.

    참고) 3-4 번까지 진행했다면, chatGPT 와 단발성 채팅은 가능하다. 그러나, 이전 대화에 대한 정보가 없어 연속적인 질문이 불가능하다.
