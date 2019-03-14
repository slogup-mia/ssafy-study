# Django in Local + hack

- 이제 C9에서 벗어나 로컬에서 장고를 돌려보자 

###  Local 개발환경

-  [StudentPack](https://education.github.com/pack) - JETBRAIN 인증 절차 등 + PyCharm Professional 설치

- Python3.6 - [Python 3.7.2 - Dec. 24, 2018](https://www.python.org/downloads/release/python-372/) - [Windows x86-64 executable installer](https://www.python.org/ftp/python/3.7.2/python-3.7.2-amd64.exe)  설치 

###  PyCharm Professional 기본 설정 및 팁

- 잔소리 밑줄 없애기 : 설정 - pep8 coding style violation 끄기
- 터미널 cmd→git : 설정 - terminal - shell path : C:\Program Files\Git\bin\bash.exe
- python / Terminal 글씨 설정 : Editor - Font /  Console Font 
- plugins 설치 : .ignore, MetarialTheme

###  

##  Django Project

- Django Project를 생성해보자.

- C9에서 했던 길고 긴 장고 초기 설정을 하지 않아도 된다. 

- pip install Ipython , django_extensions 

- 프로젝트를 생성하고 프로젝트 setting및 app등록 등 기본 코딩을 한다. 

- 정확한 코드 활용은 [실습파일](https://github.com/JungSWon/CODING/tree/master/Django/first_local)에서 확인하자.

  ###   


###  1. gitignore 

- 장고 프로젝트의 venv 는 git에 올리면서 관리하면 안된다. 너무 크다. 

- in shell : 프로젝트 root로 위치 잡아주고 아래와 같이 파일 생성 

  ``` bash
  student@M7012 MINGW64 ~/PycharmProjects/first_local (master)
  $ touch .gitignore
  ```

- 하면 프로젝트 파일트리에 .gitignore 파일이 생긴다. 

  아래와 같이 git에 올리지 않을 폴더 및 파일들을 추가해준다.

  ``` python
  #Virtual ENV
  venv/
  
  # Pycharm Auto Generated DIR
  .idea/
  pycache  /
  
  #DB
  *.salite3
  ```

- 특정 폴더를 깃 관리에서만 지우고싶다면 

  .gitignore에 폴더를 추가하고 

  bash에서 `git rm -r --cached  폴더명/ `

###  


###  2. DB 조회 

- models.py 에서 db를 생성하고 migrate 과정을 완료한다.
- 어드민 페이지에서 DB 보기 

#### - 1.  Admin Page에서 DB 조회하기

```python
# admin.py 
from django.contrib import admin
from .models import Article

admin.site.register(Article)
```

``` bash
$python manage.py makesuperuser 
$python manage.py runserver 
```

####  - 2. Pycharm에서 DB확인하기 

- 윈도우 우측 Database 라벨클릭 - '+' 아이콘 - DDL Data Source - SQLite - 다운로드 

- 프로젝트 파일 트리에 db.sqlite3 파일이 생성된다

  : 이게바로 우리 프로젝트의 db - 우측 Database에 sqlite3파일을 끌어온다 

  - 하위 확장하면 models.py 에서 migrate한 db들이 모두 포함되어있다. 

### 3. DB 추가 

- models.py 에서 새로 db를 추가하고 migrate를 한 후
- Database 새로고침 하면 새로만든 db가 들어와있다. 

- admin.py에 db를 아래와 같이 추가해주고 admin 페이지를 새로고침하면 마찬가지로 확인 가능

  ``` python
  from django.contrib import admin
  from .models import Article, Comment
  
  admin.site.register(Article)
  admin.site.register(Comment)
  ```

-  ※중요 ※ Database - sqlite에서 직접 db를 crud하면 안된다.  

  > 우리는 db중개자인 orm이 있는 상태로 장고 프로젝트를 만들고 관리하고 있는데, 중개자 없이 db자체를 바로 건드리면 기능적 충돌이 나는 경우가 많다.  orm이 자동으로 해주는 자잘한 기능들이 모두 무시되기 때문이다 (ex.DB를 삭제했을 때 sqlite상에 남아있는 contents 까지 삭제하는 작업 등)

  그러므로 sqlite파일은 admin페이지에 가지 않고도 db를 확인하는 용도로만 사용하자. 



###  4. Page 관리

####  -1. base.html extends  

db에 article이 아직 없는상황인데  ul은 생성되어서 페이지상에서 마진을 먹는다. 

그러므로 db가 있는 경우에만 리스트업 공간을 마련하려면 if article 코드를 짜면된다.

```html
<h1>Article list</h1>
{% if articles %}
    <ul>
        {% for article in articles %}
            <li>{{ article.title }}</li>
        {% endfor %}
    </ul>
```



#### -2. html include 

_comment.html 생성하여 코멘트 부분을 따로 작성하고 detail.html에 불러온다. 

_comment.html

```html
<hr>
<div id="commentUI">
    <div id="commentForm">
        <form action="{% url 'board:create_comment' article.id %} " method="POST">
            <label for="comment">comment: </label>
            <input type="text" id="comment" name="content" autofocus>
            {% csrf_token %}
        </form>
    </div>
    <div id="commentList">
            {% if comments %}
                <ul>
                    {% for comment in comments %}
                    <li>{{ comment.content }}</li>
                        <form action="{% url 'board:delete_comment' article.id comment.id %}" method="POST">
                            <button type="submit" onclick="return confirm('정말 삭제?')">[x]</button>
                            {% csrf_token %}
                        </form>
                {% endfor %}
                </ul>
            {% endif %}
    </div>
</div>
```

detail.html

```html
{% include 'board/_comment.html' %}
```







####  -3. 오류페이지 관리

settings.py에서 

```python
DEBUG = False
#ALLOWED_HOSTS = ['127.0.0.1:8000/'] 아래와 같다.
ALLOWED_HOSTS = ['*']
```

로 설정하면 디버그 상세 페이지가 뜨지 않는다. 단순히 상태코드가 뜰 뿐. 배포된 페이지에는 기업 내부 개발 정보가 노출되면 안되기 때문에.

false로 설정하면 allowed_host 주소도 넣어줘야함  

http 상태코드를 구글링해서 200, 404, 500 등 어떤 의미인지 알아보자.

views.py에서 아래와 같이 페이지 상태를 

```python
def article_detail(request,article_id):
    article = get_object_or_404(Article, id= article_id)
    # article = Article.objects.get(id=article_id)
    return render(request,'board/detail.html',{'article':article,})
```



#### -4. 요청 관리

##### (1) onclick = confirm

삭제 버틀을 눌렀을때 확인 창 띄우기 

```html
    <div>
        <form action="{% url 'board:delete' article.id %}" method='POST'>
            <button type="submit" onclick="return confirm('정말삭제?')">Delete</button>
            {% csrf_token %}
        </form>
    </div>
```



##### (2) GET, POST

**[표1]** GET과 POST 호출이 일어나는 경우를 나누도록 하자.

| GET                                | POST                                       |
| ---------------------------------- | ------------------------------------------ |
| 직접 url을 작성하여 접근한 경우    | 페이지상에서 제출버튼 또는 엔터를 누른경우 |
| 리다이렉트 또는 페이지가 렌더된다. | 제출양식이 전달되어 액션을 취한다.         |

- 

아래는 POST 요청이 들어온다면 : 요청 내용이 db 리스트에 존재하는 것이라면 : 액션 후 리다이렉트

POST요청도 아니고  url에 요청한 내용이 db 리스트에 없는 것이라면 : 리다이렉트시 오류 페이지가 뜬다. 

``` python
def delete_article(request, article_id):
    if request.method =='POST':
        article = get_object_or_404(Article, id = article_id)
        # db안에 해당 아티클이 있는지 우선 검사 하고 있으면 진행
        article.delete()
    return redirect('board:list')
```

- 

그래서 아래와 같이 우선 요청 내용이 db에 존재하는 검사먼저 해주고 조건을 나누면 

POST 요청이든 GET 요청이든 없는 내용이라면 404오류 페이지가 뜬다.

 ``` python
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method =='POST':
        article.delete()
    return redirect('board:list')
 ```

- 

그렇다면, url에 직접 쳤을때(GET)와 양식을 제출했을때(POST) 리턴값을 달리 하려면 어떻게 해야 할까? 

``` python
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method =='POST':
        article.delete()
        return redirect('board:list')
    elif request.method == 'GET':
        return redirect('board:detail',article.id)
```

- 

그런데 지금, 너무 많은 url이 열려있다. 코드를 줄일 수 있을까? 

**[표2]** 아래 표를 바탕으로 생각해보면 해답을 유추할 수 있다. 

| GET                                                        | POST                          |
| ---------------------------------------------------------- | ----------------------------- |
| 클라이언트가 페이지요청 및 리소스(이미지,영상)을 요청할 때 | DB에 영향을 주는 액션을 할 때 |

- 

예로 CRUD중 Create에 관련된 두 메소드를 비교해 보자. 

**[표 3]** [표 1] 과 [표 2] 를 합쳐보면 이렇다.

| GET                                       | POST                                               |
| ----------------------------------------- | -------------------------------------------------- |
| **주소창에 /create 작성하여 접근**한 경우 | create 페이지에서 제출버튼을 눌러 양식 제출한 경우 |
| 새 게시물 작성 페이지를 렌더해준다        | 새 게시물 저장 : **DB에 영향을 주는 액션**을 한다. |

코드로 구현해보자. (in views.py)

기존의 `new_article()` 함수를 지우고 아래와 같이 합칠 수 있게 된다.

``` python
# def new_article(request):
#     return render(request, 'board/new.html')

def create_article(request):
    if request.method == 'GET':
        return render(request, 'board/new.html')
    else:
        article = Article()
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('board:detail',article.id)
```

- 

이해를 높이기 위해 html5의 철학에 대한, 근원적인 이야기를 해보자

아래는 crud액션을 할 때 취해야 할 올바른 메소드이다. 

| C    | R    | U     | D      |
| ---- | ---- | ----- | ------ |
| post | get  | patch | delete |

- 

한편, url은 'Uniform Resource Locator'로, '유일한 리소스 지시기'를 의미한다. 

쉽게 말해 리소스가 '어디' 있는지 명명해 주는 것. 그러므로 url은 명사형으로 제시되어야 하는게 맞다.

그러나 이제까지 우리는 쉬운 이해(또는 명료함)를 위해 '/article/**create**' , '/article/**update**/1' 등과 같이 동사형으로 url을 요청해왔다. 

아래와 같이 메소드와 명사를 맵핑해놓으면 html철학에 맞는 명사형 url요청이 가능해진다. 

| method | Noun       | 요청의 의미              |
| ------ | ---------- | ------------------------ |
| get    | /articles  | 아티클들을 줘라          |
| get    | /article/1 | 아티클1을 줘라           |
| Post   | /article   | 아티클을 새로쓰자        |
| Patch  | /article/1 | 아티클1을 수정(패치)하자 |
| Delete | /article/1 | 아티클1을 삭제하자       |

 [이 페이지](https://zzu.li/6E07j)에서 조금 더 얘기하고 있다. 2번과  4번이 그 내용.

- 

다시 코딩으로 돌아와서, in html

``` html
<form method="POST">
```

 summit => POST 제출: 제자리 뛰기 => 메서드가 POST일 때 하기로(views.py에서) 약속한 액션을 취하게 된다. 



###  5. Comment 

- autofocus : 페이지에 접근하자마자 커서가 댓글란에서 깜빡이도록 한다 

``` html
<hr>
<div id="commentUI">
    <div id="commentForm">
        <form action="{% url 'board:create_comment' article.id %} " method="POST">
            <label for="comment">comment: </label>
            <input type="text" id="comment" name="content" autofocus>
            {% csrf_token %}
        </form>
    </div>
    <div id="commentList">
            {% if comments %}
                <ul>
                    {% for comment in comments %}
                    <li>{{ comment.content }}</li>
                        <form action="{% url 'board:delete_comment' article.id comment.id %}" method="POST">
                            <button type="submit" onclick="return confirm('정말 삭제?')">[x]</button>
                            {% csrf_token %}
                        </form>
                {% endfor %}
                </ul>
            {% endif %}
    </div>
</div>
```



###  

##  Django in Pycharm - Hack

- Pycharm에서 Django project를 진행하면서 사용할 수 있는 꿀팁들을 알아보자

- 다음은 Pycharm professional 기준으로, Community 에선 되는지 안되는지 잘 모르겠다. 

- 본문 초반에 언급한 파이참 초기 설정을 완료했다고 가정한다. 


###  1. 범용 단축키 

- `Shift` 연타 : 파일을 파일명으로 바로 열 수 있다. 
- `cirl` + `d`  : 윗 줄이 그대로 duplicate된다.
- `shift` + `Enter` : 줄 중간에서 바로 다음 새 줄로 이동 
- `Ctrl` + `g` + 줄번호 : 해당 번호 줄로 바로이동
- 윈도우 하단 Version Control - Log - project - 각 파일을 클릭하면 마지막 커밋 후 차이를 보여준다. 

####  - 디버깅 

- `Alt` + `Enter` : 오류를 바로잡아주는 코드를 제시해준다

  활용 예 ) 코드를 짜다 import 해야 할 부분이 있다면 `from sth import sth` 을 자동완성해준다

- `ctrl` + `Alt` + `l` : 인덴팅 바로잡기

- 디버깅 툴 `emded()` 코드 사용하기 :일종의 댐 역할을 한다. 

  해당 페이지에서 해당 액션을 취하면 그 전 부분까지만 runserver가 되고 멈춘다. 

  ``` python
  from IPython import embed
  def article_list(request):
      articles = Article.objects.all().order_by('-id')
      embed()
      return render(request,'board/list.html',{'articles':articles,})
  ```

  shell에서 결과값을 리턴받아 확인 할 수 있다.

  ``` bash
  In [1]:  a = Article.objects.all()
  In [2]: a
  Out[2]: <QuerySet [<Article: 1: >, <Article: 2: 네네>]>
  In [4]: exit()
  ```

- `#TODO: update action` 윈도우 하단 TODO탭 클릭하여 해야 할 액션이 리스트 업 되어있음. 

- `#FIXME : sth` 또한 TODO에 수정해야할 부분으로 리스트업된다.



### 2. in Django project

- `ctrl` + `Alt` + `r` : python manage.py 가 포함된 bash창에 접근

  다만 `python manage.py runserver` 만은 터미널창에서 직접 하는 게 좋다. 

- html파일에서 for + Tab 하면 views.py 에서 지어준 변수명에 따라 for문을 자동완성해준다. 

  `{% for article in articles %}`

- 마찬가지로 html파일에서 if + Tab 하면 자동완성

- views.py줄번호와 코드 사이에 html아이콘이, html에도 py아이콘이 있다. 클릭: 연결 파일로 바로이동

  이러한 기능이 많으므로 16G 이상인 컴퓨터에서 작업하기를 권장한다.


### 3. in Git Bash

- `Alt` + ` F12` : Terminal(bash) On, 다시누르면 작업파일로 커서 
- git bash창에서 다중 디렉토리와 파일 한꺼번에 생성하기 `$ mkdir -p d/e/f/a.html`  
- git bash창에서 `git add . && git commit ` : 첫 명령이 오류가 나면 멈춘다.
- git bash창에서 `git add . ; git commit ` : 첫 명령이 오류가 나도 뒤의 명령을 한다.
- `python manage.py migrate appname zero` : migrate와 데이터베이스를 모두 삭제한다. 초기화. 