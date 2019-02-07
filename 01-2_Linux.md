# Linux

리눅스와 친숙해지자. operation, command를 다루면서.



* command line 관련 추천 강의 : udacity -  linux command line basics / configuring web linux
* command line을 통해서는 그래픽 환경에서 파일을 여닫고, 추가삭제할 수 없다. 리눅스 환경에서 작업하기 위해서는 이에 익숙해져야 한다. 

#### in C9

* `pwd` : print working directory

* `echo`: 출력 외에 특정파일에 쓸 수 있다. 

  ex) 출력 예 : `NAME="Soowon"` `echo $NAME` Soowon `echo NAME` NAME` 

  ex) echo 'Hello' > a.txt ` 'Hello'라고 a.txt라는 새 파일에 써넣겠다 

   `echo 'Sooowon' > a.txt ` 'Soowon'라고 a.txt라는 기존 파일에 덮어쓰겠다(기존내용 삭제).` 

  `echo 'World' >> a.txt ` 'world'이라고 a.txt라는 기존 파일에 써넣겠다 

* `ls -al` 숨겨진 파일까지 보겠다.

* `ls forder/` 'forder'라는 폴더 안에 있는 파일들을 보겠다. (폴더밖에서 열람할때)

* `c9 .gitconfig`  숨겨진 파일을 열겠다.

* `c9 .gitbashrc`

* `vi .bash` 

* `vi .bashrc`

* `alias` 특정 커맨드에 대한 별명 붙이기

  ```
  soowon:~ $ alias gs="git status"
  soowon:~ $ alias gcm="git commit-m"
  soowon:~ $ alias gp="git push"
  soowon:~ $ alias gl="git log"
  soowon:~ $ alias p3="python3"
  
  ##별명을 붙인 후엔 반드시 소스로 환경변수를 리로드해야해 
  soowon:~ $ source ~/.bashrc
  ##처음엔 '지금부터 관리할거야' 
  soowon:~ (master) $ git init 
  ```

* CtrlC : 벗어나기  

* `cat a.txt ` 'a.txt' 파일의 컨텐츠를 읽어온다. 

* `man cat` cat이라고 하는 커맨드에 대한 설명을 열람한다 `q`로 빠져나온다

* `touch a.txt` 'a.txt'라는 파일을 생성한다. 

* `rm a.txt` 'a.txt' 라는 파일을 remove한다.  (삭제 전 그파일이 맞는지 cat으로 확인 필)

* `mkdir empty` 'empty'라는 폴더를 생성한다.
* `rm -r empty` 'empty'라는 폴더를 reculsive하게 지우겠다. 재귀적으로 아래쪽까지 돌려가면서 지우겠다 = 폴더를 지우겠다.
* `tree` 폴더, 파일 관계도 열람
* `mv templates/app.py .` mv templates폴더에 있던 app.py 파일을 현재폴더로 가져오겠다. 
* ` mv *.html templates/` 모든 .html 파일을 templates 폴더로 옮기겠다.  
* `mv templates/* .` templates의 모든 파일을 현재폴더로 옮기겠다. 
* `mv app.py main.py` app.py를 main.py로 바꾸겠다. 
* `cp mail.py templates/` copy 파일 복사본을 templates에 넣는다. 
* `cp -r templates/ views` templates 폴더를 views이름을 가진 복사본으로 생성 
* `rm -rf views/ ` views 폴더를 어쨌든(force) 지워줘 

작업기준은 home directory (window 기준 USER , Mac기준 workspace)





