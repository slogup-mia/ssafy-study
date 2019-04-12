# Django N : M Model

- 프로젝트, 앱 생성 후 

 ``` python
from django.db import models

# pip install faker(더미생성 라이브러리) 후 
from faker import Faker
# 국가코드로 결과값이 한국이름이 되도록
fake = Faker('ko-kr')
import random


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    student_id = models.IntegerField()

    # 더미 데이터를 자동으로 넣어주는 친구 
    @classmethod
    def dummy(cls,n):
        for i in range(n):
            cls.objects.create(name=fake.name(),student_id=random.randint(2000,2010))

    def __str__(self):
        return self.name
    
class Lecture(models.Model):
    title = models.CharField(max_length=100)
    
class Enrollment(models.Model):
    lecture = models.ForeignKey(Lecture,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.student.name}님이 {self.lecture.title}과목을 수강하였습니다.'
 ```

- `python manage.py shell_plus`
- `Student.dummy(10)` - `Student` 

``` bash
soowon:~/workspace $ cd SCHOOL
(edu-env) soowon:~/workspace/SCHOOL $ pip install faker
(edu-env) soowon:~/workspace/SCHOOL $ python manage.py makemigrations
(edu-env) soowon:~/workspace/SCHOOL $ python manage.py shell_plus
>>> Student.dummy(10)
>>> Student.objects.all()
<QuerySet [<Student: Student object (1)>, <Student: Student object (2)>, <Student: Student object (3)>, <Student: Student object (4)>, <Student: Student object (5)>, <Student: Student object (6)>, <Student: Student object (7)>, <Student: Student object (8)>, <Student: Student object (9)>, <Student: Student object (10)>, <Student: Student object (11)>]>
>>> Lecture.objects.create(title='알고리즘')
<Lecture: Lecture object (1)>
>>> Lecture.objects.create(title='자료구조')
<Lecture: Lecture object (2)>
>>> Lecture.objects.create(title='데이터베이스')
<Lecture: Lecture object (3)>
>>> Lecture.objects.create(title='운영체제')
<Lecture: Lecture object (4)>
>>> Lecture.objects.create(title='인공지능')
<Lecture: Lecture object (5)>
>>> Enrollment.objects.create(student_id=1,lecture_id=1)
<Enrollment: Enrollment object (1)>
>>> enrol= Enrollment.objects.first()
>>> enrol.student
<Student: 강창모>
>>> exit()
(edu-env) soowon:~/workspace/SCHOOL $ python manage.py shell_plus
>>> enrol = Enrollment.objects.first()
>>> enrol
<Enrollment: 강창모님이 알고리즘과목을 수강하였습니다.>
>>> kcm = Student.object.get(pk=1)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: type object 'Student' has no attribute 'object'
>>> kcm = Student.objects.get(pk=1)
>>> kcm = Student.objects.get(id=1)                                                                  
>>> kcm = Student.objects.first()
>>> kcm = Student.objects.get(name='강창모')                                                         
>>> Lecture.objects.all()
<QuerySet [<Lecture: Lecture object (1)>, <Lecture: Lecture object (2)>, <Lecture: Lecture object (3)>, <Lecture: Lecture object (4)>, <Lecture: Lecture object (5)>]>
>>> lectures = Lecture.objects.all()
>>> for num in range(2,6):
...     Enrollment.objects.create(student=kcm, lecture_id=num)
... 
<Enrollment: 강창모님이 자료구조과목을 수강하였습니다.>
<Enrollment: 강창모님이 데이터베이스과목을 수강하였습니다.>
<Enrollment: 강창모님이 운영체제과목을 수강하였습니다.>
<Enrollment: 강창모님이 인공지능과목을 수강하였습니다.>
>>> Enrollment.objects.all()
<QuerySet [<Enrollment: 강창모님이 알고리즘과목을 수강하였습니다.>, <Enrollment: 강창모님이 자료구조 과목을 수강하였습니다.>, <Enrollment: 강창모님이 데이터베이스과목을 수강하였습니다.>, <Enrollment: 강창모님이 운영체제과목을 수강하였습니다.>, <Enrollment: 강창모님이 인공지능과목을 수강하였습니다.>]>
>>> 
```



``` python
from django.db import models

# pip install faker(더미생성 라이브러리) 후 
from faker import Faker
# 국가코드로 결과값이 한국이름이 되도록
fake = Faker('ko-kr')
import random


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    student_id = models.IntegerField()

    # 더미 데이터를 자동으로 넣어주는 친구 
    @classmethod
    def dummy(cls,n):
        for i in range(n):
            cls.objects.create(name=fake.name(),student_id=random.randint(2000,2010))

    def __str__(self):
        return self.name
    
class Lecture(models.Model):
    title = models.CharField(max_length=100)
    
class Enrollment(models.Model):
    lecture = models.ForeignKey(Lecture,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.student.name}님이 {self.lecture.title}과목을 수강하였습니다.'
        
# 메타데이터는 데이터에 대한 정보를 관리한다.
class Client(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
    
    # class Meta:
        # ordering =('name')
    @classmethod
    def dummy(cls,n):
        for i in range(n):
            cls.objects.create(name=fake.name())
        
class Resort(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
    
    # clients = models.ManyToManyField(모델 틀래스 이름,on_delete = 필수가아니다)
    # 누구랑 관계를 가지겠다 라고 장고에게 얘기해 주는 것
    # 둘의 관계에서 한 쪽에만 설정해주면 된다.
    # 다만 윗줄에서 인자로 넣을 클래스가 미리 정의되어있어야 한다.  
    # 이로인해 migrate를 하면 : app이름_resort_clients 라는 테이블을 자동으로 만들어 줄 것이다. 
    # realted_name='resorts'를 사용하여 반대로 client에서 resort를 가리킬 수 있도록 한다. 
    clients = models.ManyToManyField(Client,realted_name='resorts')
    
    @classmethod
    def dummy(cls,n):
        for i in range(n):
            cls.objects.create(name=fake.company())
        

       
```



``` bash
(edu-env) soowon:~/workspace/SCHOOL $ python manage.py makemigrations
Migrations for 'sugangs':
  sugangs/migrations/0002_client_resort.py
    - Create model Client
    - Create model Resort
(edu-env) soowon:~/workspace/SCHOOL $ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, sugangs
Running migrations:
  Applying sugangs.0002_client_resort... OK
(edu-env) soowon:~/workspace/SCHOOL $ python manage.py shell_plus
>>> Client.dummy(20)
>>> Resort.dummy(5)
>>> resort = Resort.objects.get(pk=2)
>>> resort
<Resort: 최문>
>>> resort.clients.add(Client.objects.first())
>>> resort.clients.all()
<QuerySet [<Client: 권민재>]>
>>> resort.clients.remove(Client.objects.get(name='권민재'))
>>> resort.clients.all()
<QuerySet []>
>>> 
```



중복되는 데이터가 들어가지 않도록 하기 

