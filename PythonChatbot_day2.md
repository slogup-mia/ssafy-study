#  Python Chatbot 2일차



##  Git

* 분산 관리 시스템 

* 코드의 History를 관리하는 도구, 개발 과정과 타임라인을 볼 수 있음 

* 프로젝트의 이전 버전을 복원, 변경사항을 비교 

* Git 포스팅 서비스 / Git을 사용한 공유 환경 서비스 : Github, Gitlab, GitKraken, Gitbucket 

* [git linus torvalds google : git 개발배경 영상](https://www.youtube.com/watch?v=4XpnKHJAok8)

* git 결과창에 한글 설정하기 : 우클릭 - Text - Locate - ko_KR / eucKR


 `$ git init` 버전관리를 시작하겠다

 `$ git status ` 버전상태가 어떤지 체크 

`$ git add README.md` 'README.md' 라는 파일을 추가한다 (그 전엔 파일 트랙킹이 안됨)



####  Git의 작업흐름 

1. add 커밋할 목록에 추가

1. commit 커밋(create a snapshop) 만들기

1. push 연재까지 역사가 기록되어 있는 곳에 새로 생성한 커밋들 반영하기 



### Visual studio 에서 마크다운하고 Github에 올리기

``` git

student@M7012 MINGW64 /
$ cd ~

student@M7012 MINGW64 ~
$ cd TIL

student@M7012 MINGW64 ~/TIL (master)
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        README.md

nothing added to commit but untracked files present (use "git add" to track)

student@M7012 MINGW64 ~/TIL (master)
$ git add README.md

student@M7012 MINGW64 ~/TIL (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

        new file:   README.md


student@M7012 MINGW64 ~/TIL (master)
$ git commit -m "first commit"

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'student@M7012.(none)')

student@M7012 MINGW64 ~/TIL (master)
$  git config --global user.email "flowerneco@gmail.com"

student@M7012 MINGW64 ~/TIL (master)
$ git commit -m "first commit"
[master (root-commit) 1f2136a] first commit
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 README.md

student@M7012 MINGW64 ~/TIL (master)
$ git log
commit 1f2136a198d557284652dea2541ce507521b26bb (HEAD -> master)
Author: unknown <flowerneco@gmail.com>
Date:   Tue Dec 18 10:15:51 2018 +0900

    first commit

student@M7012 MINGW64 ~/TIL (master)
$ git status
On branch master
nothing to commit, working tree clean

student@M7012 MINGW64 ~/TIL (master)
$ git diff

student@M7012 MINGW64 ~/TIL (master)
$ git commit -m "2nd commit"
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean


student@M7012 MINGW64 ~/TIL (master)
$ git remote add origin https://github.com/JungSWon/TIL.git
student@M7012 MINGW64 ~/TIL (master)
$ git remote -v
origin  https://github.com/JungSWon/TIL.git (fetch)
origin  https://github.com/JungSWon/TIL.git (push)

student@M7012 MINGW64 ~/TIL (master)
$ git push -u origin master


## visual에서 md내용 수정/추가 후 저장하기
$ git status
$ git commit -m "3rd commit"    #몇번째 커밋인지 잘 보고 하기 
$ git push -u origin master    #github 새로고침하여 업로드 확인   


```

``` git
$ git remote -v 
 # 이때 origin 주소가 잘못되었다면 
$ git remote remove origin 
$ git remote add origin #clone or download 주소복붙
```





#### NAVER 소스 가져오기

```visual
#1. requests에게 naver.com요청을 보내서
#2. 응답 받은 문서를 저장하고 
#3. BeautifulSoup 패지지를 활용, 정보를 찾기 좋게 만들고 
#4. 우리가 원하는 정보를 뽑아온다. 

import requests
import bs4

url = "https://www.naver.com/" 

response = requests.get(url)

print(response.text)

############# 3. 부터 아래 

import requests
import bs4

url = "https://www.naver.com/" 

response = requests.get(url)
doc = bs4.BeautifulSoup(response.text,'html.parser')
result = doc.select_one('.ah_k')
# 위소스는 불러올 웹 내용의 요소검사- 복사- CSS선택자이다. 

print(result)



```

```

student@M7012 MINGW64 /
$ cd ~

student@M7012 MINGW64 ~
$ cd chatbot

student@M7012 MINGW64 ~/chatbot (master)
$ cd day2

student@M7012 MINGW64 ~/chatbot/day2 (master)
$ ls
naver_trend.py

student@M7012 MINGW64 ~/chatbot/day2 (master)
$ python naver_trend.py
<Response [200]>

```



####  1위 검색어 웹브라우저 창 열기 

``` visual
import requests
import bs4
import webbrowser

url = "https://www.naver.com/" 

response = requests.get(url)
print(response)
doc = bs4.BeautifulSoup(response.text,'html.parser')
result = doc.select_one(".ah_k")
print(result.text)


#5. webbrowser를 통해 1위 검색어 페이지를 열어주는 코드  

search_url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=" + result.text
webbrowser.open(search_url)
```

`$ python naver_trend.py `







* visual studio : 여러줄 박스 ctrl + /  : 멀티라인 주석화
* ctrl +shift + i  우클릭안될때 요소검사 