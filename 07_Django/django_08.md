#  django_08 

실습환경설정

- sns app 생성 : `python manage.py startapp sns`
- app 추가 : settings.py - `INSTALLED_APPS `
- 

settings.py 

``` python
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

대문자는 상수명 : 작업동안 변하지 않는 값을 지정할 때 대문자를 사용한다. 변수가 아니라 상수.

- 

urls.py

``` python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

위는 개발모드에서는 꼭 써야 하는 코드이다.

DEBUG =True 일때 효과있는 코드로, False이면 빈 리스트가 제공되어 기능이 없다. 

개발서버는 배포용서버보다 기능이 적다 = 경량화 되어있다.  개발모드에서 서버를 제공하기 위한 코드이다. 

###  

##  img 업로드

###  1. DB생성 

models.py

``` python
from django.db import models

class Posting(models.Model):
    content = models.TextField(default='')
    icon = models.CharField(max_length=20, default='')
    image = models.ImageField(blank=True, upload_to='postings/%y%m%d')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}: {self.content[:20]}'
```
1. **시간**

   - 시간은 당장 필요없다고 판단되더라도 레코드에 항상 넣는 습관을 들이자 

     작업시간에 크게 영향을 주지 않고 나중에 추가하려면 못하므로. 

2. **이미지**

   - 이미지는 업로드 날짜에 맞는 디렉토리`postings/%y%m%d`가 생성되어 저장되도록 한다.  

   - 컴퓨터 성능은 1디렉토리에 100개 파일 보다 100디렉토리 각 1파일씩 100 파일이 훨씬 좋다. 

     참고로 인스타는 `/%y/%m/%d/%h/%m%s`초단위로 저장한다. 워낙 리소스가 실시간 대량으로 들어오므로.

   - 이미지는 DB테이블에 주소string이 제공된다. 

     왜 이미지 자체를 저장하지 않는가?

     비트값 → 연산 이미지로 인코딩하는 작업은 서버 리소스를 상당히 잡아먹게되므로

   - blank=True 에 관련된 것은 [이 게시물](https://wayhome25.github.io/django/2017/09/23/django-blank-null/)을 참고해보자 

- in bash : pip install pillow , makemigrations, migrate
- Database에 sqlite3 끌어다 놓는다. 

###  

###  2. ADMIN 관리

admin.py

``` python
from django.contrib import admin
from .models import Posting

class PostingModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    # 관리자가 직접 수정하면 안되므로 readonly, 개별화면에서 확인만 가능
    list_display = ('id','content','created_at','updated_at')
    # 리스트에서 보여질 컬럼들
    list_display_links = ('id','content')
    # 요소들을 클릭하여 게시물로 들어갈 수 있다. 위 코드가 없다면 디폴트는 id만.
admin.site.register(Posting,PostingModelAdmin)
```

- runserver - admin page 
- 포스팅하면 이미지를 받기로한 `/media/postings/날짜`에 이미지가 추가되는 것을 확인 할 수 있다.  



###  3.  리소스 관리 

- 유저가 너무 큰 용량의 이미지를 

- $ pip install django-imagekit

- settings.py ` INSTALLED_APPS = ['imagekit',.. ]` 



model에서 DB 테이블을 수정하고 makemigrations 하면 no change detected 

migration은 파일 추가가 되었을때만 change가 생김 

