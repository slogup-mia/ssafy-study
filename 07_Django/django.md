#  django_개념과 환경설정

**프레임워크를 사용하면** 

웹서비스 제작을 A to Z 모두 하지 않고  커스터마이징만 할 수 있다. 

cf) 카페창업을 할때 , 내가 다 하지 않고 프랜차이즈 카페를 오픈하는 것과 같다. 

ex) 그 프레임워크가 바로 python django, Ruby on rails, Java Spring, PHP Laravel, Express Js  



**장고를 사용하는 이유?**



###  MTV

Model : 데이터를 관리

Template: 사용자가 보는 화면 

View: 중간 관리자 (다른 프레임워크에서는 Controller라고 명명)





## 장고 환경설정 (in C9)

* 구글 공유 폴더- ssafy_seoul - 슬라이드 - 'startup_django.pdf' 참고! 

###  1. 설치

http://zzu.li/install-pyenv : 위의 링크의 코드를 한땀한땀 터미널 창에 복붙하여 설치 

####  in terminal

``` shell
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
exec "$SHELL"

git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
exec "$SHELL"
```

이로써 pyenv와 pyenv-virtualenv가 설치되었다. 

- `pyenv --version` 로 설치상태 확인 out[]: `pyenv 1.2.9-2-g6309aaf2`

**이후 아래와 같이 반드시 pyenv install** 

> 현업환경에 들어가면 파이썬 버전이 다를 수 있다.  원래 프로젝트를 관리, 새프로젝트 시작 할 때에 파이썬을 편하게 관리 하기 위해 pyenv를 설치하는 것이다. 
>
> *장고 책 함부로 사지 마라. 대부분 장고 1버전.  장고 2버전대에서 이전 버전  

``` shell
soowon:~/workspace $ pyenv install 3.6.7
```

설치에 5분 정도 소요된다. 

설치 완료 후 파이선 전역 버전을 3.6.7로 설정 한다.

``` shell
soowon:~/workspace $ python --version
Python 2.7.6
soowon:~/workspace $ pyenv global 3.6.7
soowon:~/workspace $ python --version
Python 3.6.7
```

 

###  프로젝트 생성 및 환경설정

1. 프로젝트 진행할 폴더 생성 (디렉토리명 : PRACTICE)

2. **해당 폴더로 이동 (cd PRACTICE/)**

3. 가상 환경 설정 

   나 가상환경 하나 만들건데 3.6.7.로 만들거야 그 이름을 'practice-venv'

   ```shell
   soowon:~/workspace/PRACTICE $ pyenv virtualenv 3.6.7 practice-venv 
   ```

   지금 폴더에 가상환경을 적용할거야 : 이 폴더로 진입함과 동시에 가상환경 진입  (폴더진입 = 가상환경진입)

   ``` shell
   soowon:~/workspace/PRACTICE $ pyenv local practice-venv
   (practice-venv) soowon:~/workspace/PRACTICE $
   ```

4. `django` 설치

   ``` shell
   (practice-venv) soowon:~/workspace/PRACTICE $ pip install django
   ```

5. Django 프로젝트 test 생성 

   - 'practice' 프로젝트를 현재(' . ') 폴더에서 시작

   ``` shell
   (practice-venv) soowon:~/workspace/PRACTICE $ django-admin startproject practice .
   ```

   디렉토리 확인 

   ```shell
   (practice-venv) soowon:~/workspace/PRACTICE $ tree .
   .
   ├── manage.py
   └── practice
       ├── __init__.py
       ├── settings.py
       ├── urls.py
       └── wsgi.py
   ```

6. 혹시 가상환경을 잘못된 디렉토리에 설정했다면?

   가상환경 목록 확인 / 가상환경 삭제 

   ``` shell
   $pyenv virtualenvs
   $pyenv uninstall 가상환경이름
   ```


### 실행코드

1.  서버구동 (C9 밖에서는 $IP:$PORT부분 삭제)

```shell
(practice-venv) soowon:~/workspace/PRACTICE $ python manage.py runserver $IP:$PORT
```

2. 서버페이지를 열어서 - 페이지 주소 복사

3. settings.py 파일을 열어서 빈 allowed host를 내 페이지 주소를 아래처럼 편집하여 넣는다. 

    `ALLOWED_HOSTS = ['django-practice-soowon.c9users.io']` 

    -  `ALLOWED_HOSTS = ['*']` : 모든 url을 허용한다.

4. 열려있는 페이지 새로고침 하면  - 장고 시작 





###  시간, 언어 설정

- 장고는 internationalization  (a.k.a i18n) 을 제공한다. 

settings.py 설정파일을 건드릴때만 서버를 재구동하면 된다.  

```python
LANGUAGE_CODE = 'ko-kr'      #참고로 'ko-kp'는 북조선 국가코드
TIME_ZONE = 'Asia/Seoul'
```