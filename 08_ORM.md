#  ORM

- **Object-Relational Mapping** 

- Flask-SQLAlchemy 



### 준비 

```terminal
sudo pip3 install sqlalchemy 
sudo pip3 install flask-sqlalchemy 
```

- zzu.li/sqlalchemy 로 가면 flask_sqlalchemy 공식 문서에서 참고하자. 

``` python
from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] ='sqlite:///blog2.db'
#아래코드 중요하다. 오류 방지를 위해 직접쳐야함 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] =False

db = SQLAlchemy(app)
db.init_app(app)
#어플리케이션이 이니셜라이즈될때 app도 함께 이니셜라이즈. 

```



###  테이블 생성

>  **Flask-SQLAlchemy** 

``` python
class Flight(db.Model):
__tablename__ = "flights"
id = db.Column(db.Integer, primary_key=True)
origin = db.Column(db.String, nullable=False)
destination = db.Column(db.String, nullable=False)
duration = db.Column(db.Integer, nullable=False)

db.create_all()
```

> **sqlitee3** 

``` sql
CREATE TABLE flights (
id SERIAL PRIMARY KEY,
origin VARCHAR NOT NULL,
destination VARCHAR NOT NULL,
duration INTEGER NOT NULL
);
    
```



### 열 추가

> **Flask-SQLAlchemy** 

```python
flight = Flight(origin="New York",destination="Paris",duration=540)
db.session.add(flight)
```

> **sqlite3**

``` sqlite
INSERT INTO flights
(origin, destination, duration)
VALUES ('New York', 'Paris', 540)
```



###  조회 (불러오기) 1 

> **Flask-SQLAlchemy**  

```python
Flight.query.all()
```

```python
Flight.query.filter_by(origin="Paris").all()
```

```python
Flight.query.filter_by(origin="Paris").first()
```

```python
Flight.query.filter_by(origin="Paris").count()
```

```python
Flight.query.filter_by(id=28).first()
Flight.query.get(28)
```

> **sqlite3**

```sqlite
SELECT * FROM flights;
```

```sqlite
SELECT * FROM flights WHERE origin = 'Paris';
```

```sqlite
SELECT * FROM flights WHERE origin = 'Paris' LIMIT 1;
```

```sqlite
SELECT COUNT(*) FROM flights WHERE origin = 'Paris';
```

```sqlite
SELECT * FROM flights WHERE id = 28;
```



### 조회 (불러오기) 2

> **Flask-SQLAlchemy**  

1. ``` python
   Flight.query.order_by(Flight.origin).all()
   ```

2. ``` python
   Flight.query.order_by(Flight.origin.desc()).all()
   ```

3. ``` python
   Flight.query.filter(Flight.origin != "Paris").all()
   ```

4. ``` python
   Flight.query.filter(Flight.origin.like("%a%")).all()
   ```

5. ``` python
   Flight.query.filter(Flight.origin.in_(["Tokyo", "Paris"])).all()
   ```

6. ```python
   Flight.query.filter(and_(Flight.origin == "Paris",Flight.duration > 500)).all()
   ```

7. ```python
   Flight.query.filter(or_(Flight.origin == "Paris",Flight.duration > 500)).all()
   ```

8. ```python
   db.session.query(Flight, Passenger).filter(Flight.id == Passenger.flight_id).all()
   ```

> **sqlite3**

1. ```sqlite
   SELECT * FROM flights ORDER BY origin;
   ```

2. ``` sqlite
   SELECT * FROM flights ORDER BY origin DESC;
   ```

3. ``` sqlite
   SELECT * FROM flights WHERE origin != "Paris"
   ```

4. ``` sqlite
   SELECT * FROM flights WHERE origin LIKE "%a%"
   ```

5. ``` sqlite
   SELECT * FROM flights WHERE origin IN ('Tokyo', 'Paris');
   ```

6. ``` sqlite
   SELECT * FROM flights WHERE origin = "Paris" AND duration > 500;
   ```

7. ``` sqlite
   SELECT * FROM flights WHERE origin = "Paris" OR duration > 500;
   ```

8. ``` sqlite
   SELECT * FROM flights JOIN passengers ON flights.id = passengers.fought_id;
   ```





###  수정 

> **Flask-SQLAlchemy** 

```python
flight = Flight.query.get(6)
flight.duration = 280
db.session.commit()
```

> **sqlite3**

```sqlite
UPDATE flights SET duration = 280 WHERE id = 6;
COMMIT;
```



### 삭제 

> **Flask-SQLAlchemy** 

```python
flight = Flight.query.get(28)
db.session.delete(flight)
db.session.commit()
```

> **sqlite3**

```sqlite
DELETE FROM flights WHERE id = 28;
COMMIT;
```







##  실습

- C9 -  minipjt-cloned  참고 

``` python
# sudo pip3 install sqlalchemy 로 인스톨 먼저
# sudo pip3 install flask-sqlalchemy 
from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
import datetime



app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] ='sqlite:///blog2.db'
#아래코드 중요하다. 오류 방지를 위해 직접쳐야함 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] =False
#zzu.li/sqlalchemy 로 가면 flask_sqlalchemy 공식 문서에서 참고하자. 

db = SQLAlchemy(app)
db.init_app(app)
#어플리케이션이 이니셜라이즈될때 app도 함께 이니셜라이즈. 

# 테이블 생성 
class Article(db.Model):
    __tablename__= "articles"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String, nullable = False)
    content = db.Column(db.String, nullable =False)
    author = db.Column(db.String, nullable =False)
    created_at = db.Column(db.String, nullable =False)

db.create_all()


@app.route('/')
def index():
    return redirect('/articles')
    

#첫화면 
#글목록 표시
@app.route('/articles')
def articles():
    print(app.config)
    articles = Article.query.all()
    return render_template('articles.html', articles=articles)
    
    
#새글 생성 form 페이지 
@app.route('/articles/new')
def new():
    return render_template('new.html')
    
    
    
#글 생성 페이지  
@app.route('/articles/create',  methods=['POST','GET'])
def create():
        #orm을 사용하여 데이터를 저장한다.
        ## form.get vs. args.get => form.get은 POST로 받은 데이터를 가져오는 것. 
    title = request.form.get('title')
    content = request.form.get('content')
    author = request.form.get('author')
    now = datetime.datetime.now()
    created_at = now.strftime('%Y-%m-%d %H:%M:%S')
    
    a = Article(title=title,content=content,author=author,created_at=created_at)
    db.session.add(a)
    db.session.commit()
    
    return render_template('/create.html')
    

#글 조회 창
@app.route('/articles/<int:no>')
def view(no):
    '''
    c = sqlite3.connect('project.sqlite3')
    db = c.cursor()     
    sql = "SELECT * FROM articles WHERE id = {}".format(no)
    db.execute(sql)
    data = db.fetchall()
    c.close()
    '''
    data = Article.query.get(no)
    
    return render_template('/view.html',data= data)
    
    

#글 수정 form 페이지 
@app.route('/articles/<int:no>/edit')
def edit(no):
    
    data = Article.query.get(no)
    return render_template('edit.html',data=data)
     
    
    
#글 수정 페이지  
@app.route('/articles/<int:no>/update', methods=['POST','GET'])
def fin_edit(no):
    title = request.form.get('title')
    content = request.form.get('content')
    author = request.form.get('author')
    
    '''
    c = sqlite3.connect('project.sqlite3')
    db = c.cursor()     
    sql = "UPDATE articles SET title='{}', content='{}', author='{}' WHERE id = {}".format(title,content,author,no)
    db.execute(sql)
    c.commit()
    c.close()
    '''
    up = Article.query.get(no)
    up.title = title
    up.content = content
    up.author = author
    
    db.session.commit()
    
    return redirect('/articles/{}'.format(no))  



    
@app.route('/articles/<int:no>/delete')
def delete(no):
    #해당하는 글을 db에서 삭제한다
    
    article =Article.query.get(no)
    #db.session.delete(지우고자 하는 데이터레코드 객체)
    db.session.delete(article)
    db.session.commit()
    
    return redirect('/')
    
    
```



