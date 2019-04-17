#  Django_13 InstagramUP 

##  1. Like

- 좋아요 기능은 M:N model 

posts - model.py - like_users 추가 (기존 코드는 이전 TIL 내용 확인)

- user를 기점으로 like_posts 를 많이 부를 예정이므로(유저중심 앱 특성상) 아래와 같이 . 

- 물론 post 로부터 user를 부를 수 있다. 

``` python
like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, realted_name='like_posts', blank=True)
```

- migrate 
- pip lnstall django_extensions - settings.py 에 APP 추가 

``` bash
(insta-venv) soowon:~/workspace/INSTAGRAM (master) $ python manage.py shell_plus
>>> Post.objects.all()
<QuerySet [<Post: 좋아요!>, <Post: 넹!>, <Post: sdfsddddddddd>]
>>> Post.like_users
<django.db.models.fields.related_descriptors.ManyToManyDescriptor object at 0x7f945af60dd8>
>>> user = User.objects.first()
>>> user.like_posts
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x7f945ad575c0>
>>> user.like_posts.all()
<QuerySet []>
```

admin에서 사용자를 추가하였다 

- 유저에 좋아요 시킨다 - 아래와 같이 유저가 좋아요 한 포스트를 확인 할 수 있다. 

``` bash
>>> User.objects.all()
<QuerySet [<User: admin>, <User: swon>]>
>>> post = Post.objects.all()
>>> swon = User.objects.last()
>>> swon.like_posts.all()
<QuerySet []>
>>> swon.like_posts.add(Post.objects.first())
>>> swon.like_posts.all()
<QuerySet [<Post: 좋아요!>]>
```

- admin이 쓴 게시물 확인 

``` bash
>>> admin = User.objects.first()
>>> admin
<User: admin>
>>> admin.post_set.all()
<QuerySet [<Post: 좋아요!>, <Post: 넹!>, <Post: sdfsddddddddd>]>
```

- admin이 쓴 첫번째 게시판을 좋아요 한 사람 보기 

``` bash
>>> admin.post_set.first().like_users.all()
<QuerySet [<User: swon>]>
```



**이제 앱에 적용시키자** 

posts - urls.py

- url엔 posts 아이디만 넘겨주면 된다. 

``` python
path('<int:post_id>/like/', views.like, name ='like'),
```

views.py 에 like 추가  (기존 코드는 이전 TIL 내용 확인)

- @login_required  : 만약 유저가 로그인이 안되어있으면, 로그인을 하게 하도록 보낸다. 
- 장고가 해주는 일이다. 그래서 앞으로 로그인에 관련된 account 로 명명하겠다. 장고 기본값에 맞춰서. 

```python
from django.contrib.auth.decorators import login_required

@login_required 
def like(request,post_id):
    # 1. like를 추가할 포스트를 가져옴
    # post = Post.objects.get(id=post_id)
    post = get_object_or_404(Post, id=post_id)
    # 2. 만약 유저가 해당 포스트를 이미 like했다면 , 
        # like를 제거하고 
    #    아니라면
        # like를 추가한다. 
    if request.user in post.like_users.all():
    # request.user  => 현재 접속한 유저가 누구냐 
        post.like_users.remove(request.user)
    else: 
        post.like_users.add(request.user)
    return redirect('posts:list')
```

list.html

- fontawesome에서 빈하트와 꽉찬하트를 가져왔다. 

``` html
{% extends 'base.html' %}
{% block body %}
...
        
        <!--좋아요버튼-->
        <div class="card-body">
          <a href='{% url 'posts:like' post.id %}'>
            <!--해당 유저가 like를 했으면 꽉찬하트-->
            {% if user in post.like_users.all %}
              <i class="fas fa-heart"></i>
              <!--아니면 빈하트-->
            {% else %}
              <i class="far fa-heart"></i>
            {% endif %}
          </a>
          <p class ='card-text'>
            {{ post.like_users.count }}명이 좋아합니다.
          </p>
        </div>
      </div>
    {% endfor %}
  </div>
{% endblock %}
```



##  2. Login & Logout

accounts 앱생성 - settings.py

` (insta-venv) soowon:~/workspace/INSTAGRAM (master) $ python manage.py startapp accounts` 

urls.py 

``` python
from django.urls import path
from . import views 

app_name ='accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    ]
```

nav.html  - 로그인, 로그아웃 버튼 생성 

``` html
...
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" href={% url 'accounts:login' %}>로그인</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href={% url 'accounts:logout' %}>로그아웃</a>
      </li>
      <li class="nav-item">
        <a class="nav-link disabled" href="#">Disabled</a>
      </li>
    </ul>
  </div>
</nav>
```

accounts - templates - accounts - login.html

``` html
{% extends 'base.thml' %}
{% load bootstrap4 %}


{% block body%}
<h1 class='text-center'>로그인</h1>
<form method ='POST'>
    {% csrf_token%}
    {% bootstrap_form form%}
    <button class='btn btn-primary' type="submit" value="Submit"/>로그인</button>
</form>
{% endblock %}
```

accounts - views.py 

``` python
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login , logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm


def login(request):
    # POST : 실제 로그인( 세션에 유저 정보 추가)
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        # 유효성 검증에 성공할 경우
        if form.is_valid():
            # form으로 부터 user의 정보를 가져옴 
            auth_login(request, form.get_user())
            # next가 정의되어 있으면 해당 url(/posts/13/like/)로 리다이렉트, 
            # 아니라면 post:list로 리다이렉트
            return redirect(request.GET.get('next') or 'posts:list')
        
        # 아래의 과정은 장고가 다 알아서 해주므로 필요가 없다. 
        '''
        # 인증에 성공했을 경우
        if user:
            # Django의 auth앱에서 제공하는 login함수를 실행해 앞으로의 요청/응답에 세션을 유지한다
            auth_login(request, user)
            # Post목록 화면으로 이동
            return redirect('posts:list')
        # 인증에 실패하면 login_form에 non_field_error를 추가한다
        login_form.add_error(None, '아이디 또는 비밀번호가 올바르지 않습니다.')
        '''
        
    # GET : 로그인 정보 입력
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html',form)



def logout(request):
    auth_logout(request)
    return redirect('posts:list')
```



nav.html 

``` html
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">
    <i class="fab fa-instagram"></i>
    Instagram
  </a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav ml-auto" >
      <!--만약 로그인이 되어 있으면 -->
      {% if user.is_authenticated %}
      <li class="nav-item">
        <a class="nav-link disabled" href='#' tabindex='-1' aria-disabled='true'>{{ user.username }}</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href={% url 'accounts:logout' %}>로그아웃</a>
      </li>
      {% else %}
      <!-- 로그인이 되어있지 않으면 -->
      <li class="nav-item">
        <a class="nav-link" href={% url 'accounts:login' %}>로그인</a>
      </li>
      
      <li class="nav-item">
        <a class="nav-link disabled" href="#">회원가입</a>
      </li>
      {% eldif %}
    </ul>
  </div>
</nav>
```



##   3. Signup 

accounts / urls.py -  `path('signup/', views.signup, name='signup'),  `

nav.html 

``` html
      ...
      <li class="nav-item">
        <a class="nav-link" href={% url "accounts:signup" %}>회원가입</a>
      </li>
      {% endif %}
```

views.py 

``` python
def signup(request):
    # POST: 유저등록
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # 회원정보에 등록하고 로그인 시켜준다. 
            user = form.save()
            auth_login(request, user)
            return redirect('posts:list')

    # GET : 유저정보입력
    else:
        form = UserCreationForm()
    
    return render(request,'accounts/signup.html', {'form':form})
```

signup.html 생성 

```html
{% extends 'base.html' %}
{% load bootstrap4 %}


{% block body%}
<h1 class='text-center'>회원가입</h1>
<form method ='POST'>
    {% csrf_token %}
    {% bootstrap_form form %}
    <button class='btn btn-primary' type="submit"/>회원가입</button>
</form>
{% endblock %}
```





##  4. People



instagram - urls.py 

``` python
from accounts import views as accounts_views  

..
    path('<str:username>/', accounts_views.people, name='people'),
```

accounts - views.py

``` python
def people(request, username):
    # 사용자에 대한 정보 
        # 방법1. 아래는 string을 리턴한다. 
    # person = get_object_or_404(settings.AUTH_USER_MODEL, username=username)
        #방법2. 아래는 model에서 가져오기. import get_user_model 필요, 안쓴다.
    # person = get_object_or_404(settings.AUTH_AUTH_USER_MODEL(django.conf)
        #방법3. 아래는 실제 모델 클래스를 리턴해준다, 최신버전, 강력. 
    people = get_object_or_404(get_user_model(), username=username)
    return render(request, 'accounts/people.html', {'people':people})
```

accounts - people.html  생성

``` html
{% extends 'base.html' %}
{% load bootstrap4 %}


{% block body%}
<div class="container">
    <h1> {{people.username}}</h1>
    <div class="row">
        <!--해당 유저가 가진 모든 포스트를 for문으로 들고오기 -->
        {% for post in people.post_set.all %}
        <div class="col-4">
            <img src="{{post.image.url}}" class='img-fluid'></img>
        </div>
        {% endfor %}
    </div>
</div>

{% endblock %}
```

nav.html 

``` html
...
      <li class="nav-item">
        <a class="nav-link disabled" href="{% url 'people' user.username %}" tabindex='-1' aria-disabled='true'>{{ user.username }}</a>
      </li>
...
```

