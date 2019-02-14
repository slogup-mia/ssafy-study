# django_04

프로젝트와 어플리케이션은 django_03 이어서 이므로 변수명을 참고하자. 



##  ADMIN

C9 프로젝트에서 서버를 돌리면 아래와 같은 주소로 admin 페이지에 접근할 수 있다. 

https://django-practice-soowon.c9users.io/admin/

####  shell

- 접속을 위해서는 계정과 암호가 필요하므로 아래와 같이 admin계정을 생성하고 서버를 돌린다.  

  ``` shell
  (db-env) soowon:~/workspace/DB $ python manage.py createsuperuser
  사용자 이름 (leave blank to use 'ubuntu'): admin
  이메일 주소: 
  Password: 
  Password (again): 
  비밀번호가 너무 일상적인 단어입니다.
  비밀번호가 전부 숫자로 되어 있습니다.
  Bypass password validation and create user anyway? [y/N]: y
  Superuser created successfully.
  (db-env) soowon:~/workspace/DB $ python manage.py runserver $IP:$PORT
  Performing system checks...
  ```

####  admin.py

- admin에 해당 어플리케이션의 모델을 등록한다.

  ``` python
  from django.contrib import admin
  from .models import Job 
  
  admin.site.register(Job)
  ```

- 아래와 같이 추가하면 Job DB를 조회하는데 게시판 형식으로 볼 수 있다. 

  ``` python
  from django.contrib import admin
  from .models import Job 
  
  class JobAdmin(admin.ModelAdmin):
      list_display = ('name','job')
  
  admin.site.register(Job, JobAdmin)
  ```


