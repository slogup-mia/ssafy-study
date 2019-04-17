#  Homework 21

###  1.

> Question 모델과 Comment 모델이 1:N관계라고 할때 하나의 Question을 보여 주는 페이지에서 Comment를 모두 보여주려고 한다. 다음과 같은 detail.html이 있을때 모든 Comment의 content를 h3태그를 이용해서 출력하는 for문을 작성 하세요. (related_name은 설정해주지 않았다고 가정한다.)

``` html
{% extends 'base.html' %}
{% block body %}
<h1>{{question.title}}</h1>
<h1>{{question.author}}</h1>

{% for question in questions %}
	{{question.content}}
{% endfor %}
{% endblock %}
```



###  2. 

> 다음과 같은 urls.py 파일이 있다고 가정할 때 comment를 작성하는 버튼을 만들기 위해 form태그 안에 action 속성 값으로 넣어줘야 하는 경로를 작성하세요 

``` python
app_name = 'question'

urlpatterns =[
    path('',views.index, name='list'),
    path('<int:id>/',views.detail, name='detail'),
    path('create/',views.create, name='create'),
    path('<int:id/update>',views.update, name='update'),
    path('<int:id>/comments/create',views.comments_create, name='comments_create'),
]
```

``` html
<form action ='comments/create/' method='POST'>
    댓글달기 : <input type='text' name ='comment'/>
    <input type='submit' value='submit'/>
    {% csrf_token %}
</form>
```

