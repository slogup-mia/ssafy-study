# django_03

### base.html 

``` html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <!-- CSS 부트스트랩 코드 -->
    <!-- 아래와 같이 타이틀에 {% block 변수명%}을 먹인다
		이를 다른 html로 가져가서 base.html의 스타일로 통일해 줄 수 있다. -->
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
    <!-- 바디도 마찬가지로 {% block 변수명 %} {% endblock %}-->
    {% block body %}
    {% endblock %}
	<!-- 바디 끝단에 JS 부트스트랩 코드(세줄)를 먹이면 헤드에 넣는것 보다 성능이 좋다 -->    
</body>
</html>
```

base.html의 스타일을 가져갈 다른.html 에 아래와 같이 작성한다.

```html
{% extens 'base.html' %}

{% block title %}
장고 홈페이지
{% endblock %}

{% block body %}
<h1>First Django</h1>

<h2>{{ name }}</h2>
<h3>{{ msg }}</h3>

{% end block %}
```





## MODEL

###  models.py

스키마를 생성하는 과정. sqlalchemy의 create table 명령과 같다.

DB폴더 생성 -  pracdb 프로젝트 생성-  db-env가상환경 생성,설정 - articles 앱 생성

learn by doing 으로 가보자 



###  1. DB 생성

####  1-1. DB생성 (models.py)

```python
from django.db import models
                    # models(DB와 같다)
class Article(models.Model):
    title = models.TextField()
    content = models.TextField()
    #'title'칼럼, content'칼럼은 텍스트가 될거다 
    # CREATE TABLE ( .. )과 같은과정이지만 더 간단하지!
    # 텍스트 필드 외에 date, auto, char field emdemddl 
```

####  1-2. migration 생성 (terminal) 

model.py 를 기반으로 마이그레이션을 만든다. 

아래 위치에  initial.py 파일이 생성된다.  

​	`(db-env) soowon:~/workspace/DB/articles/migrations/0001_initial.py `

만들어진 migragtion을 실행한다. (migrate한다.)

존재하는 테이블들을 확인할 수 있다. 

``` shell
(db-env) soowon:~/workspace/DB $ python manage.py makemigrations
(db-env) soowon:~/workspace/DB $ python manage.py migrate
(db-env) soowon:~/workspace/DB $ sqlite3 db.sqlite3
sqlite>.tables
sqlite>.exit
```



### 2. 칼럼 추가 

리눅스 대화형 셀로 접속 

```shell
(db-env) soowon:~/workspace/DB $ python manage.py shell
Python 3.6.7 (default, Feb 13 2019, 02:17:32) 
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
```

만들어 놨던 articles앱의 models에서  선언한 class Article을 불러오겠다. 

그 Article에 칼럼을 추가하고(title ='', content=''), 저장하겠다.  

```shell
>>> from articles.models import Article
>>> a = Article(title="happy", content="hacking")
>>> a.save()
```

한줄로 추가하기 

``` shell
>>> Article.objects.create(title='hey', content='create')
제목:hey, 내용:create
```



### 3. DB 및 칼럼 조회

#### 3-1. 기본 조회

Article에 존재하는 objects를 조회하고 나가자. 

​	쿼리셋이란?:  리스트처럼 생긴 객체

```shell
>>> Article.objects.all()
<QuerySet [<Article: Article object (1)>]>
>>> Article.objects.first()
<Article: Article object (1)>
>>> Article.objects.first().title
'happy'
>>> exit()
```

아래와 같이 sqlite에서도  DB에 저장된 레코드를 열람할 수 있다. 

```shell
(db-env) soowon:~/workspace/DB $ sqlite3 db.sqlite3
SQLite version 3.8.2 2013-12-06 14:53:30
Enter ".help" for instructions
Enter SQL statements terminated with a ";"

sqlite> .tables
articles_article            auth_user_user_permissions
auth_group                  django_admin_log          
auth_group_permissions      django_content_type       
auth_permission             django_migrations         
auth_user                   django_session            
auth_user_groups  

sqlite> SELECT * FROM articles_article;
1|happy|hacking
```



#### 3-2. repr, str 조회 

models.py 클래스 안에 repr 함수 선언 

```python
    def __repr__(self):
        return f'제목:{self.title}, 내용:{self.content} by repr'
    def __str__(self): 
        return f'제목:{self.title}, 내용:{self.content} by str'
```

shell을 재접속 - DB인 class Article 불러오기 - 조회

조회 : Article.objects.all()  ,  Article.objects.first()  ,  len(Article.objects.all()) 

```shell
>>> exit()
(db-env) soowon:~/workspace/DB $ python manage.py shell
...
>>> from articles.models import Article
>>> Article.objects.all()
<QuerySet [제목:happy, 내용:hacking, 제목:와 여기서도 글이 써진다!!, 내용:장고 짱짱맨!]>
>>> Article.objects.first()
제목:happy, 내용:hacking
>>> len(Article.objects.all())
2
```

str 함수 선언 전, 후로 - print(a)와 a 출력차이를 보자 

```shell
>>> for a in Article.objects.all():
...     print(a)
... 
Article object (1)
Article object (2)

>>> for a in Article.objects.all():
...     a
... 
제목:happy, 내용:hacking
제목:와 여기서도 글이 써진다!!, 내용:장고 짱짱맨
```



#### 3-3.  조건

Article.objects.filter(title="happy").all    (*str함수 선언 전,후 출력해보자)

Article.objects.filter(content='hacking').first()

```shell
>>> Article.objects.filter(title="happy").all 
<bound method QuerySet.all of <QuerySet [제목:happy, 내용:hacking]>>

>>> Article.objects.filter(content='hacking').first()
제목:happy, 내용:hacking
```

Article.objects.get(pk=1) 과 Article.objects.get(id=1) 는 같다.

``` shell
>>> Article.objects.get(pk=1)
제목:happy, 내용:hacking
>>> Article.objects.get(id=1)
제목:happy, 내용:hacking
```

Article.objects.get(title='happy') 과 Article.objects.filter(content='hacking').first() 는 같다.

``` shell
>>> Article.objects.get(title='happy')
제목:happy, 내용:hacking
>>> Article.objects.filter(content='hacking').first()
제목:happy, 내용:hacking
```



####  3-4. 정렬, 역정렬 조회 (order)

``` shell
>>> Article.objects.order_by('id').all()
<QuerySet [제목:와 여기서도 글이 써진다!!, 내용:장고 짱짱맨!, 제목:happy, 내용:Thursday, 제목:hey, 내용:create, 제목:check, 내용:str?repr?]>
>>> Article.objects.order_by('-id').all()
<QuerySet [제목:check, 내용:str?repr?, 제목:hey, 내용:create, 제목:happy, 내용:Thursday, 제목:와 여기서도 글이 써진다!!, 내용:장고 짱짱맨!]>
```



####  3-5. 구간, 역정렬 조회 (index, slicing)

``` shell
>>> Article.objects.all()[0]
제목:와 여기서도 글이 써진다!!, 내용:장고 짱짱맨!
>>> Article.objects.all()[::-1]
[제목:check, 내용:str?repr?, 제목:hey, 내용:create, 제목:happy, 내용:Thursday, 제목:와 여기서도 글이 써진다!!, 내용:장고 짱짱맨!]
>>> Article.objects.all()[1:3]
<QuerySet [제목:happy, 내용:Thursday, 제목:hey, 내용:create]
```



#### 3-6. 기타 조회

- **migration 조회**

  0001 migration 파일의 정체와 족적을 조회한다. 

  ``` shell
  (db-env) soowon:~/workspace/DB $ python manage.py sqlmigrate articles 0001
  BEGIN;
  --
  -- Create model Article
  --
  CREATE TABLE "articles_article" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" text NOT NULL, "content" text NOT NULL);
  COMMIT;
  ```

- **메소드 조회** 

  일반 리스트보다 엄청 메소드가 많다. =  사용자의 편의가 좋다.  

  ``` shell
  >>> dir(Article.objects.all()) 
  ['__and__', '__bool__', '__class__', '__deepcopy__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_add_hints', '_batched_insert', '_chain', '_clone', '_combinator_query', '_create_object_from_params', '_db', '_earliest_or_latest', '_extract_model_params', '_fetch_all', '_fields', '_filter_or_exclude', '_for_write', '_has_filters', '_hints', '_insert', '_iterable_class', '_iterator', '_known_related_objects', '_merge_known_related_objects', '_merge_sanity_check', '_next_is_sticky', '_populate_pk_values', '_prefetch_done', '_prefetch_related_lookups', '_prefetch_related_objects', '_raw_delete', '_result_cache', '_sticky_filter', '_update', '_validate_values_are_expressions', '_values', 'aggregate', 'all', 'annotate', 'as_manager', 'bulk_create', 'complex_filter', 'count', 'create', 'dates', 'datetimes', 'db', 'defer', 'delete', 'difference', 'distinct', 'earliest', 'exclude', 'exists', 'explain', 'extra', 'filter', 'first', 'get', 'get_or_create', 'in_bulk', 'intersection', 'iterator', 'last', 'latest', 'model', 'none', 'only', 'order_by', 'ordered', 'prefetch_related', 'query', 'raw', 'resolve_expression', 'reverse', 'select_for_update', 'select_related', 'union', 'update', 'update_or_create', 'using', 'values', 'values_list']
  ```


### 4. DB 및 칼럼 수정 및 삭제 

수정할 부분 정의 - 수정 - 저장 - 변경내용 확인  

``` shell
>>> a = Article.objects.get(id=1)
>>> a.content = "Thursday"
>>> a.save()
>>> Article.objects.get(id=1)
제목:happy, 내용:Thursday
```

삭제할 부분 정의 - 삭제 - 저장 - 확인 

``` shell
>>> a = Article.objects.get(id=1)
>>> a.delete() 
(1, {'articles.Article': 1})
>>> a.save()
```





####  mission

- 전생앱 

  /pastlife   :  form으로 사용자의 이름을 입력받아

  /result  :  전생직업을 알려준다. 

  팁 ; pip install faker

  답; c9 - django-practice - DB - pastlifes



