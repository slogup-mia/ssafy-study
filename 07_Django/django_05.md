#  django_05



프로젝트를 진행할 폴더생성과 가상환경설정 

``` shell
soowon:~/workspace $ mkdir BOARD
soowon:~/workspace $ mkdir BOARD
soowon:~/workspace $ cd BOARD
soowon:~/workspace/BOARD $ pyenv virtualenv 3.6.7 board-venv
soowon:~/workspace/BOARD $ pyenv local board-venv
```

install 띄어쓰기로 여러 패키지를 한꺼번에 깔 수 있다.

``` shell
(board-venv) soowon:~/workspace/BOARD $ pip install django ipython django_extensions
```

프로젝트 시작 

```shell
(board-venv) soowon:~/workspace/BOARD $ django-admin startproject board .
(board-venv) soowon:~/workspace/BOARD $ python manage.py startapp articles
```

setting.py 

- ALLOWED_HOSTS, 언어, 시간 설정
- INSTALLED_APPS 을 아래와 같이 추가 

```python
INSTALLED_APPS = [
		... 
    'django_extensions',
    'articles',
]
```

templates 안에 어플 폴더 만들어서 구분하자 

```
BOARD/
│	manage.py
└────articles/
│		└─__pyache__
│		└─migrations/
│       └─templates/ 
│			└─articles/
│			 	 index.html
│				   ... 
│		__init__.py
│		admin.py
│		models.py
│		views.py
│			..
└────board/
		__init__.py
		settings.py
		urls.py
		wsgi.py
```





models.py - class Article 생성

``` shell
(board-venv) soowon:~/workspace/BOARD $ python manage.py makemigrations
(board-venv) soowon:~/workspace/BOARD $ python manage.py sqlmigrate articles 
(board-venv) soowon:~/workspace/BOARD $ python manage.py migrate
dbshell 열어줘 
(board-venv) soowon:~/workspace/BOARD $ python manage.py dbshell
```

인스톨했던 extensions 이 대화형 ipython 콘솔을 만들어준다.  열어줘

```shell
(board-venv) soowon:~/workspace/BOARD $ python manage.py shell
```

아래와 같이 사용할 수 있다. 

```shell
In [1]: from articles.models import Article         
In [2]: article = Article(title="제목 테스트" , content="zz")
In [3]: article.save()                                                        
In [4]: Article.objects.first()
Out[4]: <1,제목 테스트:zz>
```

알아서 import를 해줘서 편하게 쓸 수 있다. 

``` shell
(board-venv) soowon:~/workspace/BOARD $ python manage.py shell_plus
```



#### R

/articles/   :list

/articles/ 1	:detail

#### C

 /articles/new	:new(작성)

 /articles/create	:create(DB저장)

#### U

 /articles/1/edit	:edit

 /articles/1/update	:update

#### D

 /articles/1/delete		:delete





서브문지기 .py 생성

articles 앱 폴더 안에 urls.py 생성 

``` python
from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.index),
]
```

메인문지기로 가서

전역 urls.py 

```python
from django.contrib import admin
from django.urls import path, include
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    # articles/ 패턴이 들어오면 서브문지기에게 보내겠다.
]
```

그럼 다시 서브문지기 

```python
urlpatterns = [
    path('', views.index),
]
```

와 같이 수정하고 서버를 돌렸을때 아래와 같은 주소로 들어가면 돌아간다.

 https://django-practice-soowon.c9users.io/articles/

즉슨 앱 안의 서브문지기는 반복되는 /articles/ 를 체크하지 않아도 된다. 



장고가 보안을 위해 하는 일. 

글작성  페이지를 요청하면 new.html을 제공하면서 토큰을 함께 (몰래) 발급해준다.  

글 작성후 submit해서 (리다이렉트,또는 html) 리퀘스트 시 발급해준 토큰이 맞는지 확인후 작성을 받아들인다. 

new.html : 메소드를 POST로 설정하고 토큰을 발행한다. 

``` html
<h1>게시글 작성</h1>
<!--post방식으로 보낼때는 넘기는 url을 '/'로 닫아준다-->
<form action ='/articles/create/' method='POST'>
    제목 : <input type="text" name="title"/>
    내용 : <input type="text" name="content"/>
    <input type="submit" value="Submit"/>
    {% csrf_token %}
</form>
```

view.py: 받는 방식을 POST로 바꾼다. 

```python
def create(request):
    #DB에 저장
    title = request.POST.get('title')
    content = request.POST.get('content')
            # import Article
    article = Article(title=title,content=content)
    article.save()
    
    return redirect('/articles')
```



하드코드 url (날것의 url그대로)을 

앱 내 urls.py 에서 인자에 이름을 먹이면(=url들한테 함수명과 동일한 별명을 주면 ) 간단하게 사용할 수 있다. 

상세 url을 바꾸는 경우가 많은데, url경로를 수정해도 html, views.py마다 수정하지 않아도 된다. 

index.html

```html
<h1>게시판이오</h1>

<!--<a href="/articles/new/">새글쓰기</a>
    위의 하드코드 url을 아래와 같이 간단히 할 수 있다.-->
<a href="{% url 'new' %}">새글쓰기</a>


<table>
    <tr>
        <th>번호</th>
        <th>제목</th>
    </tr>    
    {% for article in articles %}
    <tr>
        <td>{{article.id}}</td>
        <!--<td><a href='/articles/{{article.id}}/'>{{article.title}}</a></td>-->
        <td><a href="{% url 'detail' article.id %}">{{article.title}}</a></td>
    </tr>
    {% endfor %}
</table>
```

views.py

```python
def update(request, Aid):
    ....
    article.save()
    # return redirect(f'/articles/{Aid}/') 
    return redirect('detail', article.id)
    
def delete(request,Aid):
    article = Article.objects.get(id=Aid)
    article.delete()
    return redirect('index')
```





##   



앱생성 

``` shell
(board-venv) soowon:~/workspace/BOARD $ python manage.py startapp pages
```

메인문지기 urls.py에 앱 추가 

``` python
from pages import views
```

settings.py -  INSTALLED_APPS  에 앱 추가 

앱 내에 templates, home.html 생성

views.py

```python
def home(request):
    print("Pages 앱의 views.home이라는 함수로 불린 페이지입니다.")
    print("이 앱이 돌아간다면 첫페이지를 리로드했을때 shell에 출력될 것입니다.")
    # 모든 앱의 html파일을 동등하게 찾는다. (어디든 있는지 없는지만 찾는다.)
    # return render(request, 'articles/home.html')
    # 위와같이 위치를 명시하여 렌더하면 아티클에 있는 home.html을 불러오게된다. 
    # return render(request, 'home.html')
    # 위처럼 동명이개의 html을 부르면 settings.py -INSTALLED_APPS에서 적시한 순서가 먼저인 것을 찾는다. 
    # 그러므로 렌더 오류를 막기 위해 아래와 같이 명시해준다. 
    return render(request, 'pages/home.html')
```



앱별로 템플릿폴더가 있고, 전역템플릿을 생성한다. 

BOARD/templates/ 도 되지만 

BOARD/board/templates/ 로 프로젝트 폴더 안에 넣어준다. 

앱 안에 들어가있는 템플릿 폴더를 먼저 찾는다. 전역템플릿을 찾는게 디폴트가 아니다. 

그러므로 찾아주라고 설정해야해 아래와 같이

settings.py

DIRS 안에 절대경로(literally처음부터 끝까지)가 모두 들어가야 하지만 

import 되어있는 os를 사용하여 짧은 경로를 알아내서 넣는다. 

`os.path.join(BASE_DIR)` 는 경로를 알맞게 만들어준다.

ex) `os.path.join('/','ddd','sss','ggg')` => `'/ddd/sss/ggg'`

그러므로 결론 : 보드/템플릿을 디폴트 템플릿으로 추가해주려면 아래와 같이 명시해주면 된다. 

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR),'board','templates'],
```

지금까지 템플릿 구조

``` 
-보드(프로젝트) 
	- 템플릿
-아티클(앱1)
	- 템플릿
	- 아티클즈 
-페이지(앱2)
	- 템플릿
	- 페이지스 
```

