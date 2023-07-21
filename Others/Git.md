# git
[github 링크](https://github.com/)

## git 이란?

* 분산 버전 관리 시스템

* git 의 기능
  * 각 버전과 변경사항을 기록, 관리 가능함<br>
  * 최종 파일은 git bash에 저장된다.
<br><br>

* git 을 사용하는 이유
  * git에 있는 프로젝트를 pull/push 하기 위해

## git 구조와 작동 원리

1. git 의 작동 방식
    - 중앙 집중식 vs 분산식
    - git은 분산식으로,
      1. 동시에 다양한 작업 수행이 가능, 충돌을 줄여줌
      2. 중앙 서버의 장애에 대비항 백업, 복구가 용이
      3. 인터넷이 없어도 작업을 계속 할 수 있음

2. git 의 구조
    * (git) local repository : working dir, staging area, repository
    * (github) remote repository
    
    <br>

    - local repository :
      1. working dir 에서 변경사항을 작업
      2. staging area 로 변경 사항을 add
      3. 마지막으로 local repository 로 commit 
    - remote repository :
      1. local repository 에서 변경사항을 remote repository 로 push 하여 저장
      2. 다른 PC 에서 다시 local repository 로 pull 하여 작업

    <br>

    *working dir : 실제 파일이 있는 영역<br>
    *staging area : 선택적인 추가, 제거가 가능한 중간 준비 영역<br>
    *repository : 버전 이력과 파일들이 영구적으로 저장되는 영역<br>
    *commit (= 버전) : 변경된 파일들을 저장하는 행위

## git bash 기본 명령어

* touch file : 파일 생성<br>
* echo > file > file : 한번에 여러개의 파일 생성<br>
* mkdir folder : 폴더 생성

<br>

* start file/folder : 파일/폴더 실행

<br>

* rm file : 파일 삭제<br>
* rm -r folder : 폴더 삭제<br>
* rm -rf folder : 폴더 삭제<br>
* rm * : 전체 삭제<br>
* rm *.txt : 해당 확장자 전체 삭제<br>

<br>

* cd folder : 현재 디렉토리의 해당 폴더로 이동 <br>
* . : 현재 디렉토리<br>
* .. : 상위 디렉토리<br>
* ... : 상위의 상위 디렉토리<br>
* ~dir : 절대 디렉토리<br>

<br>

* ls folder : 해당 디렉토리의 모든 파일과 폴더 검색<br>
* clear : 터미널 창 기록 삭제<br>

<br>

* \ : 띄어쓰기 등 인식 못하는 문자 앞에 붙여주면 인식하게 할 수 있음<br>

## git 기본 명령어
git 유저 설정 방법

* git config --global user.name name : 유저 이름 설정<br>
* git config --global user.email email : 유저 이메일 설정<br>
* git config --global -l : 유저 확인<br>

<br>git 실행 및 local repository 조작 명령어

* git init : git 실행 (.git 파일 생성)<br>
* rm -rf .git : git 종료 (.git 파일 제거)<br>
* echo file >> .gitignore : 특정 파일 무시<br>
* rm .gitignore : 파일 무시 해제<br>
* git add . : 모든 파일 add<br>
* git status : 파일 상태 확인 (add 확인)<br>
* git rm --cached file : add 된 파일 제거<br>
* git commit -m 'commit_message' : add 된 파일 commit<br>
* git log : commit 된 파일 확인<br>
 

## github 이용 방법

1. github 에 가입 후 remote repository 를 만들어 URL을 따낸다.
   * https://github.com/KTaeGyu/remote_repository_name.git

<br>

2. 다음 순서로 git bash에 입력하여 데이터를 push 한다.<br>

   * echo "# remote_repository_name" >> README.md<br>
   * git init<br>
   * git add README.md<br>
   * git commit -m "commit_message"<br>
   * git branch -M master<br>
   * git remote add origin remote_repo_url<br>
   * git push -u origin master

 * 만약 실행되지 않는다면 다음 명령어를 이용해 강제로 push 가능
   * git push origin +master
 
<br>

1. 다음 코드를 입력하여 github 에서 데이터를 pull or clone 한다.<br>

   * git pull origin master
   * git clone remote_repo_url