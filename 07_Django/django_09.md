# Django_09

##  TODO list tool 만들기

- 상용화된 TODO list tool 예 
  - 분더리스트 https://www.wunderlist.com/ko/ 
  - 트렐로 https://trello.com/ 
  - 마이크로소프트todo https://todo.microsoft.com/ko-kr 
- 참고 : 리로드 없이 UI가 변화하는 기능을 구현하는 것들은 
  - JAVA Script 가 헤비하게 사용된다. 
  - 이런 작업을 할 수 있는 프론트엔드 개발자가 수급불균형의 끝을 달리고 있기 때문에 반드시 배워놓자 반드시! 

###  환경 

- c9 - rails 프로젝트 생성 

- how to install pyenv on ubuntu https://cjh5414.github.io/ubuntu-pyenv-virtualenv/

  - ``` shell
       sudo apt-get update  
       ```

         : apt-get 은 우분투의 초코라고 생각하면 된다.

         = 우분투가 쓰고있는 패키지매니저 툴

        소프트웨어, 패키지를 홈페이지 가서 버튼클릭 등등 하는게 아니라 커맨드라인에서 바로 인스톨 할 수 있도록 관리해주는 아이 

       `update` 는 앱-겟을 최신버전으로 업데이트 하는것. 프로젝트를 처음 시작할 때는 패키지 인스톨 전에 반드시 업데이트를 해 주어야 한다. 

  - ``` shell
    sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev
    ```

    위와 같이 필요한 패키지들을 한꺼번에 인스톨한다. (`sudo apt-get install 패키지이름들`)

  - https://gist.github.com/djohnkang/7d7ba4854b505fe42236fccd8ee9788c

    pyenv 인스톨 코드 순서대로 복붙 

  - ``` shell
    soowon:~/workspace $ mkdir TODOAPP
    soowon:~/workspace $ cd TODOAPP/
    soowon:~/workspace/TODOAPP $ pyenv install 3.6.7
    ```

  - 참고 ) pyenv 인스톨 상태 확인하기 `c9 ~/.bashrc`

  - 파이썬 3.6.7을 글로벌환경으로 만들고 확인

       장고 깔고 앱생성 

       ``` shell
       soowon:~/workspace/TODOAPP $ pyenv global 3.6.7
         soowon:~/workspace/TODOAPP $ python --version
         Python 3.6.7
       ```

       ``` shell
       soowon:~/workspace/TODOAPP $ pyenv virtualenv 3.6.7 todo-venv
       soowon:~/workspace/TODOAPP $ pyenv local todo-venv
       ```

       ``` shell
       (todo-venv) soowon:~/workspace/TODOAPP $ pip install django django_extensions
       (todo-venv) soowon:~/workspace/TODOAPP $ django-admin startproject todoapp .
       (todo-venv) soowon:~/workspace/TODOAPP $ python manage.py startapp todos
       ```

- todoapp/settings.py - 앱추가 

- url include 설정 , app내 url 설정, home.html 등등등등 



### 목업하기 

- 카카오오븐 https://ovenapp.io/ 

- 어도비XD https://www.adobe.com/kr/products/xd.html#x

- 발사믹(유료) https://balsamiq.com/ 



###  로그인 

- 장고에는 로그인기능이 이미 짜여져 있기 때문에 우리는 바닥부터 짤 필요가 없다. 

- migrate를 하면 아래와 같이 auth 가 깔린다. 이게 로그인기능을 해주는 아이. 슈퍼유저를 생성한다. 

  ``` shell
  (todo-venv) soowon:~/workspace/TODOAPP $ python manage.py migrate
    ...
    Applying auth.0002_alter_permission_name_max_length... OK
    Applying auth.0003_alter_user_email_max_length... OK
    Applying auth.0004_alter_user_username_opts... OK
    ...
  (todo-venv) soowon:~/workspace/TODOAPP $ python manage.py createsuperuser
  ```

- users 앱 생성

  ``` shell
  (todo-venv) soowon:~/workspace/TODOAPP $ python manage.py startapp users
  ```

- 메인문지기에게 users 관련 url path 설정  

- 앱 기본환경(url, views, html) 조성 
- users/login.html  - 로그인 폼 구성 

#### - SHA256

- SHA256 (Secure Hash Algorithm - made by NSA)

- Crypotographic + Hash Function 

- 데이터를 원본그대로보다는 **Hash Function** 을 통해 관리한다. 

- 어떤 값을 input 받아 hash function을 통해 일정길이의 숫자가 만들어진다.  이과정을 hash digest라고 부름

- 아웃풋을 가지고 인풋값을 알 수 있으면 안된다. 랜덤한 값이 아웃된다고 생각하면 된다. 

- 다만 같은 인풋값에는 항상 같은 256비트의 아웃풋값이 나온다.

- 사이트, 서비스마다 랜덤하게 주어진 salt값을 가지고 있어서 add a salt 과정을 통해 한번 더 암호화 한다.  

- 활용 예) 긴 문서 또한 단 256비트의 hash값으로 저장할 수 있다. 이 때 데이터 이동 또는 전달시 데이터의 무결성을 입증하는데에 쓰인다. ' . '하나만 추가/삭제 되어도 hash 값이 완전 달라진다. 데이터 전달 도중 데이터가 손상, 쉽게말해 납치, 악의적 가공이 되었는지 여부를 검증할 수 있다. 그래서 블록체인에서는 이가 매우 중요한 알고리즘으로 활용된다. 

- 활용 예) `git hash-object.txt ` 로 문서의 해쉬값을 확인할 수 있다. 

  깃이 이를 통해 커밋 히스토리와 변경사항을 빠르게 알아낼 수 있는것이다. 

- 활용 예) 전자서명을 위한 인증서에도 sha인증필드를 가지고 있다. 

- 암호학의 추상적인 개념이나마 맛보고싶다면 - [칸아카데미 - crytography](https://ko.khanacademy.org/computing/computer-science/cryptography) - 한시간도 안걸리는 재미있는 강의가 있다. 꼭 한번 보도록 하자. [영상으로도 볼수 있음](https://www.youtube.com/watch?v=wXB-V_Keiu8) 

- 참고 : SHA256과 같은 기능을하는 MD5 (Message-Digest algorithm 5) 는 더이상 쓰면 안되는 알고리즘이다. 이제 복호화가 쉬워졌기 때문. 해쉬in-out값이 저장된 레인보우 테이블이 공유,오픈 되었다. 



####  - 로그인이란?

- 유저를 검증하고

- 해당 유저가 검증된 사용을 서버가 알게 하는 것 

  ``` mermaid
  graph TD
  철수 --> 서버Django; 영희 --> 서버Django; 창모 --changmo,12341234--> 서버Django; 동찬 --> 서버Django;
  ```

  - 서버 : 유저를 검증 =  서버 내 DB에 존재하고 , id & pw 가 일치하는지

- HTTP = statless (상태없음)

  검증을 한번 하더라도 HTTP는 유저가 검증된(로그인된) 상태인지 여부를 트래킹할 수 없게 한다. 

  ``` mermaid
  graph LR
  철수 --> 서버Django; 영희 --> 서버Django; 창모+과자 --changmo,12341234--> 서버Django; 동찬 --> 서버Django; 서버Django--cookie--> 창모+과자;
  ```

  - 기존엔 쿠키를 갖는 유저를 인증유저로 간주했다. 쿠키는 모든 유저에게 동일한 쿠키가 제공 되었다 

  - 부작용 : 해커가 쿠키값을 알아내 쿠키를 가지고 접속을 한다면 로그인 하지 않고도 접근을 할 수 있었다.

  - 현재 : 유저마다 과자값을 다르게 제공한다.

    유저가 로그인 하면 DB에 '로그인된 유저info + 과자값 + a' 를 저장하여 보안을 강화했다. 

    저장된 값이 바로 세션, '세션이 만료되었습니다', '유효한 세션이 아닙니다' 라고 나오는 이유가 바로 서버가 이 값의 상태를 계속 확인하고 있기 때문. 




settings.py 

기본값인 쿠키에서 세션으로 설정해준다 .

메세지가 저장될 공간은 코드와 같이 세션을 통해서 저장할거야. 

``` python
MEESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
```



로그아웃시킨다 = 세션에서 유저를 지운다. 

로그아웃 또한 장고가 제공하는 로그아웃함수를 사용하면 된다. 



