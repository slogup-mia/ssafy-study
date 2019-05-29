# django_02 

### 장고 디렉토리 구조

> PROJECT/project(Django project) : 다양한 어플리케이션의 집합 
>
> PROJECT/project/ pages , 
>
> PROJECT/project/ movies ,  ...   : 'pages', 'movies'등 의 어플리케이션 

 어플리케이션 생성 

``` shell
(practice-venv) soowon:~/workspace/PRACTICE $ python manage.py startapp pages 
```

pages 라는 폴더가 생성되었다

> pages/__init__.py 
>
> pages/models.py, 
>
> pages/views.py, 
>
> pages/admin.py  각자 장고의 M T V 를 위한 파일들이 있다.



글로벌 설정에 어플리케이션 'pages' 추가

- PRACTICE/practice/settings.py  

* 이 때 ' , ' 잊지않기. 장고에서 맞는 신텍스다.

``` python
INSTALLED_APPS = [
    'django.contrib.admin',
    ... 
    'pages',
]
```



- PRACTICE/pages/views.py 

```python
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
```

인덱스 템플릿 생성

- PRACTICE/pages/templates/index.html 

url 추가 

- PRACTICE/practice/urls.py

```python
from django.contrib import admin
from django.urls import path
# url 추가 전에 pages라는 앱 안에 views라는 파일을 불러온다. 
from pages import views

urlpatterns = [
  # 장고에서는 url/ 뒤에 슬래시'/'를 붙여야 한다.
    path('admin/', admin.site.urls),
  # path(url, 해당요청을 다룰 view 함수)
  # 페이지를 켜자마자 열리는 root url은 빈 url로 설정 ('')
    path('',views.index )
]
```



###  MISSION

1.

`def isval(request):` 선언하여 url이 `isval/`인 페이지를 추가해보자. 

이 페이지는 오늘이 발렌타인데이 인지 여부에 따라 '네', '아니오' 를 보여준다. 

2.

사용자가 url에 입력한  단어가 팰린드롬단어인지 판별하는 페이지를 만들어보자

3.

로렌픽섬을 사용하여 랜덤이미지를 보여주는 페이지를 생성해보자

```
https://picsum.photos/200/300/?random
```

정답: C9 -  django-practice   -   PRACTICE/pages/views.py  

4.

ascii 로 그림을 그려주는 api가 있다. http://artii.herokuapp.com/

다음과 같이 url에 원하는 텍스트를 입력하면: http://artii.herokuapp.com/make?text=ssafy

폰트를 바꾸고 싶다면: http://artii.herokuapp.com/make?text=ssafy&font=trek

그렇다면 사용자로부터 단어를 입력받는 페이지와 /new 

결과를 보여주는 페이지를 만들어보자 /artii 



5.

/papago 

사용자로부터 단어를 입력받아 /result로 넘겨줌

papagp API 검색 결과 보여줌 







####  C9 bash에서 암호키 저장하기

1. bashrc를 켠다 `c9 ~/.bashrc`  (루트'~'에서 c9 배쉬를 열겠다)

2. 암호키를 입력한다 `export NAVER_ID='' \ export NAVER_PASS=''`

3. 변경사항 저장 `source ~/.bashrc`

4. c9에서는 반드시 배쉬 가상환경을 끈다  `source deactivate`

5. view.py로 돌아가 `import os ` , 