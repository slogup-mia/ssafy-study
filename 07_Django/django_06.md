#  django_06 Model + Comment

**학습목표**

- DB관계 
- 댓글달기

참고 

- [Modeling 테이블 이미지 생성 사이트](http://Aquerytool.com) 



##   1. DB관계 

- 댓글은 어느 글에 속하게 되어있다. 

  = 데이터베이스 안에 들어갈 테이블 간의 상호 관계를 생각하는 과정을 배워보자. 

- 데이터베이스 관계 = 테이블간의 관계 

### - 1 : 1 관계  

- 가장 간단함
- 생활 예) 부부관계, 1처1부제   예2) 사람과 주민번호 관계

### - 1 : N 관계

- 가장 많은 경우
- Has_many, Belongs_to
- 생활 예) 학급- 학생 관계 
- 코딩 예) 게시글-댓글 ,  유저-게시글 
- 학생을 지칭하면 어느 학급에 있는지 알 수 있다, 학급을 지칭하면 N명의 학생.

### - M : N 관계

- Many to many 
- 생활 예) 수강신청,학적관리: 수업-학생  
- 1 : N을 중첩하는 개념이다

###  - 관계 없음 

- 연관이 없는 관계 



##  2. 댓글달기

- 댓글달기는 1 : N의 관계이다.



댓글 클래스 선언 ()

댓글이 속한 본문을 명시할 때, 본문의 id를 사용한다. 

그러므로 댓글 테이블은 : 댓글 id , 댓글 내용, 본문id

여기서 본문 id는 댓글의 foreign key이다.  

 foreign key 표현방법 

- 인자1: 어디에 속하는지
- 인자2: 본문이 지워졌을 때 댓글을 어떻게 할지 
  - CASCADE : 본문이 지워지면 속한 댓글이 모두 지워진다. 일반적인 옵션
  - PROTECT / SET_NULL / DO_NOTTHING 등 의 다른 옵션들이 있다. 
- 인자2: 관계될때 댓글이 본문에 대해 어떤 존재인지 

models.py

``` python
#댓글 테이블 
class Comment(models.Model):
    content = models.TextField()
    #댓글이 속한 본문
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
```

테이블을 마이그레이션 하고 생성된 (articles.0002_comment)를 통해 sql상에서 확인 할 수 있다.  

``` shell
(board-venv) soowon:~/workspace/BOARD $ python manage.py makemigration
(board-venv) soowon:~/workspace/BOARD $ python manage.py migrate
...
Running migrations:
  Applying articles.0002_comment... OK
(board-venv) soowon:~/workspace/BOARD $ python manage.py sqlmigrate articles 0002
...
CREATE TABLE "articles_comment" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content" text NOT NULL, "article_id" integer NOT NULL REFERENCES "articles_article" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "articles_comment_article_id_59ff1409" ON "articles_comment" ("article_id");
```



``` shell
(board-venv) soowon:~/workspace/BOARD $ python manage.py shell_plus
In [1]: Article.objects.all()
Out[1]: <QuerySet [<1,제목 테스트:zz>, <2,네네:넹!>, <5,url테스트:네>, <7,redirect:url테스트>, <9,왜:왜왜왜그럴까>, <10,수정!:띠용??>, <11,새글:쓰기>]>

In [2]: article = Article.objects.first()  
In [3]: article.id   
Out[3]: 1

In [4]: comment = Comment(content='첫번쨰 글의 첫번째 댓글입니다.', article=article)             
In [5]: comment.content
Out[5]: '첫번쨰 글의 첫번째 댓글입니다.'

In [6]: comment.article
Out[6]: <1,제목 테스트:zz>

In [7]: comment.save()
In [8]: Comment.objects.first().article
Out[8]: <1,제목 테스트:zz>

In [9]: Comment.objects.first().article.title
Out[9]: '제목 테스트'

In [10]: Comment.objects.first().article.content
Out[10]: 'zz'
```

In [8] : 코멘트의 입장에서 본문을 불러오기 

- Article.objects.get(Comment.objects.first().article_id) 과 같다.

- .article : 장고orm이 간단하게 클래스안의 property로써 사용할 수 있도록 해준다. 

본문(id가 1인)의 입장에서 코멘트를 불러오기 

- article_id 가 1인 코멘트만 불러오기 
- 코멘트의 셋을 모두 불러올래 
- article.object.first().comment_set.all() 





detail.html

``` html
<h1>제목: {{article.title}}</h1>
<h2>내용: {{article.content}}</h2>
<a href="{% url 'edit' article.id %}">수정</a>
<a href="{% url 'delete' article.id %}">삭제</a>

<a href="{% url 'index' %}">글 목록</a>

<h3>댓글</h3>

<form action ="{% url 'comment' article.id %}" method='POST'>
    <input type="text" name=""/>
    <input type="submit" value="Submit"/>
    {% csrf_token %}
</form>

<h4>댓글 불러오기 방법1</h4>
<ul>
    {% for comment in comments %}
        <ui>{{comments.content}}<a href="{% url 'index' %}">[댓글수정]</a></ui>
    {% endfor %}
</ul>



<h4>댓글 불러오기 방법2</h4>
<ul>
    <!--아티클로부터 댓글 모두 불러오기-->
    <!--아래 코드를 사용하면 views.detail에서 댓글DB를 불러서 
        탐색하지 않아도 된다.-->
    <!--템플릿 html에서는 ...all()에서 ()를 뺴야한다.-->
    <!--{% for comment in article.comment_set.all %}-->
    
    <!--models.Comment 에서 관계명을 정의하고 related_name='comment'
        위의 comment_ser을 관계명인 comments로 수정한다. -->
    <!--조회순서 뒤집기: {% for comment in article.comments.all reversed %}-->
    {% for comment in article.comments.all %}
        <li>{{comment.content}}<a href="{% url 'index' %}">[댓글수정]</a></li>
    {% endfor %}
</ul>
```

views.py

``` python
from django.shortcuts import render, redirect
from .models import Article , Comment
# from .models import Comment

def detail(request, Aid):
    # 아이디에 맞게 DB불러오기 
    article = Article.objects.get(id=Aid)
    # 본문id를 article_id(foreignKey)로 갖고 있는 댓글DB 모두 불러오기
    # 위의 html에서 댓글 불러오기 방법2를 쓴다면 이 과정이 필요 없음    
    comments = Comment.objects.filter(article_id=Aid).all()
    context = {'article':article, 'comments':comments}
    return render(request, 'articles/detail.html', context)

    
def comment(request, Aid):
    #댓글을 작성한다.
    content = request.POST.get('content')
    comment = Comment(content=content, article_id=Aid)
    comment.save()
    return redirect('detail', Aid)

```

