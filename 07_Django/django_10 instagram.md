## instagram

- `zzu.li/install-pyenv`

- 코드 복붙  +  `pyenv install 3.6.7` +  `pyenv global 3.6.7`

- `mkdir INSTAGRAM` - `cd INSTAGRAM` - ` pyenv virtualenv 3.6.7 insta-venv` - `pyenv local insta-venv`

- `pip install django==2.1.7`  - `pip install --upgrade pip`

- ` django-admin startproject instagram .`

- 루트폴더에 `.gitigmore` 파일 생성 후 알맞게 ignore 리스트 작성

  - 참고 : `gitignore.io` - `django` 생성  

    장고 프로젝트 생성시 필요한 gitignore 리스트 생성해준다. 복붙만 하면 됨.

- `git init ` - `git status` - `git add .gitignore` 등  

- 개발 순서(flow)를 추적하기 위해 깃 관리를 잘 해야한다. 좋은 개발자의 기본 자세. 

  폴더별 또는 작업 별 등 commit을 쪼개는 기준은 프로젝트팀(기업) 마다 다르므로 눈치껏 하면 된다.  

  commit message는 상세하게 가는 것이 좋다. 

- `git log ` : 커밋 히스토리를 볼 수 있다.

- github 접속 - 레퍼지토리 생성 - Initialize this repository with a README 는 체크안하는게 좋다. 체크 = README 자동커밋하고 시작 

- `git remote add .... ` : 깃 리모트 (연동) - `git push -u origin master`

###  서비스 기획 순서 (BDD -> TDD)

- BDD : 사용자 행동을 중심으로 기획 
- TDD : 테스트 주도 개발 . 테스트 후 개발 

1. 무엇을 하는 서비스인지?  :  사용자 interact 
2. mock up : 사용자가 어떤 화면을 볼지 
3. 데이터 모델링 : 어떤 데이터를 사용할 지  
4. 코딩



###  앱 생성

- `python manage.py startapp posts`

- model 테이블 생성 - `python manage.py makemigrations` - ` python manage.py migrate` - `git commit -m '구체적인 작업내용'`

- admin.py 클래스 설정, createsuperuser 생성 - commit 

- 루트폴더/Templates 폴더 - base.html 생성 - bootstrap starter templates 복붙

  - 참고 : Tab space가 2step 인지 4step인지 개발환경을 체크하고 통일하기 

- settings.py 

  ``` python
  TEMPLATES = [
      {
          ...
          'DIRS': [os.path.join(BASE_DIR,'templates')],
  ```

  루트폴더에 대한 BASE_DIR 절대경로에 대해 : 운영체제마다 폴더경로를 구분하는 법이 다르기 때문에 ( \ or / )  파이썬이 os 모듄 내 path 내 경로생성을 해주도록 한다. 

- urls , views , html 



- `pip install django-bootstrap4 `pip 장고에 부트스트랩을 올리기

- settings.py 

  ``` python
  INSTALLED_APPS = [
      'bootstrap4',
  ```




####  fontawesome

- 아이콘 사용하기 

1. startusing free - base.html head에 fontawesome link rel 복붙
2. 아이콘 html 복붙하여 적절한 위치에 복붙 



### image

- `pip install pillow`

- ImageField 모델 추가 - makemigrations - migrate

- create.html -  `<form method ="POST" enctype='multypart/form-data'>`  

- settings.py 

  ```  python
  STATIC_URL = '/static/'
  
  # 미디어가 어느 url로 어디에 쌓일지 지정
  ## 미디어 파일들이 불릴 URL
  MEDIA_URL = '/media/'
  ## 실제 저장장소 
  MEDIA_ROOT = os.path.join(BASE_DIR,'media')
  ```

- urls.py

  ``` python
  # 파일에 직접들어가지 않고 접근하는 함수, 객체, 방법을 만들어서 파일을 직접 조작하지 못하게 한다.
  # 왜? 앱이 방대해졌을때 직접 접근하게 되면 파일경로 등이 바뀌었을때 하나하나 바꾸어야 하기 때문에.
  # settings.py에 넣어놓은 설정과 관련 정보는 모두 .conf 에 다른 설정과 함께 들어간다. 
  from django.contrib import admin
  from django.urls import path, include
  from django.conf import settings 
  from django.conf.urls.static import static
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('posts/', include('posts.urls')),
  ]
  
  
  # urlpatterns += static('/media/', os.path.join(BASE_DIR,'media'))
  # 아래는 위와 같이 settings에 설정해놓은 인자 값으로 불러온다. 
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  ```



###  Post - User 연결

- models.py  

  ``` python
  # from django.contrib.auth.models import User
  from django.conf import settings
  
  #user = models.ForeignKey(User, on_delete=models.CASCADE )
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE )
  ```

- migtations, migrate

  - 이 때 ForeignKey를 받는다는 것은 칼럼이 추가가 된다는 의미로 
  - migrate를 시도하면 : (기존의 주인없는 post를 연결시켜줄 user)디폴트값을 주거나 취소하라는 메세지가 뜬다. 
  - 1을 누르면 어느 유저에게 연결할지 물어본다. 
  - 이 경우엔 admin이 유일한 유저이므로 admin의 pk인 1을 누르면 그에게 자동으로 연결시켜준다.  

- 작성자만 수정/ 삭제 가능하도록 하기 

  list.html

  ``` html
  {% extends 'base.html' %}
  
  {% block body %}
    <div class="row justify-content-center">
      {% for post in posts %}
        <div class="card" style="width: 40rem;">
          <div class="card-header">
            <span>{{ post.user }}</span>
          </div>
          <img class="card-img-top" src="{{ post.image.url }}" alt="Card image cap">
          <div class="card-body">
            <p class="card-text"> {{post.content}} </p>
            <a href="{% url 'posts:delete' post.id %}" class="btn btn-danger">삭제</a>
            <a href="{% url 'posts:update' post.id %}" class="btn btn-info">수정</a>
          </div>
        </div>
      {% endfor %}
    </div>
  {% endblock %}
  {% if post.user == request.user %}
  ```

  views.py

  ``` python
  # @require_POST
  def delete(request,post_id):
      post = Post.objects.get(id='post_id')
      if post.user != request.user:
          return redirect('post:list')
      post.delete()
      return redirect('posts:list')
      
  def update(request,post_id):
      post = get_object_or_404(Post,pk=post_id)
      # post = Post.objects.get(pk=post_id)
      if post.user != request.user:
          return redirect('post:list')
      if request.method == 'POST':
          form = PostModelForm(request.POST, instance=post)
          if form.is_valid():
              form.save()
              return redirect('posts:list')
  ```


