#  Database SQL 기초

구글 공유 드라이브에 자료 있으니 참고하자

##  DB

데이터베이스: 체계화된 데이터의 모임

여러 사람이 공유하고 사용할 목적으로 통합 관리되는 정보의 집합.

- 만들고create
- 읽고read
- 수정하고update
- 삭제하고delete

-> crud operation



### RDBMS 관계형데이터베이스 관리 시스템

관계형 모델을 기반으로 하는 데이터베이스 관리 프로그램이다

ex) MySQL, SQLite, PostgreSQL 등의 오픈소스

ex) ORACLE, MS SQL (유료)

RDB(관계형 데이터베이스)의 쉬운 예? 엑셀파일, 엑셀의 table 형태. 

**SQLite**

서버가 아닌 응용 프로그램에 넣어 가벼운 프로그램 

우리가 배울 프로그램. 



* c9 terminal에서 `sqlite3`하면 실행된다 `.exit`으로 나온다. 




###  스키마

청사진

데이터베이스 자료의 구조, 표현방법, 관계 등을 정의한 구조 

| column    | datatype |
| --------- | -------- |
| id        | str      |
| telephone | int      |
| age       | int      |
| ...       | ...      |



* 베이터베이스 :엑셀 파일  = 테이블1,2,3.. : 시트1,2,3...
* 열 : column 고유한 데이터 형식이 지정된다. 모든 name, 모든age.. 세로줄. 
* 행 : row,레코드.  4명의 고객정보라면, 4개 행 존재. 가로 한줄 한줄이 각 행.
*  PK : 기본 키. 각 행의 고유핪으로 Primary Key라고 불린다. 반드시 설정해햐 하며, DB관리및 관계 설정 시 주요하게 활용된다. 





##  SQL 개념 

Structured Query Lite

RDBMS의 데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어. 

자료의 검색과 관리, 스키마 생성과 수정, 데이터베이스 객제 접근 조정 관리.

###  SQL문법

- DDL 데이터 정의 언어
- DML 데이터 조작 언어
- DCL 데이터 제어 언어

 -> 자세히 배우진 않는다. 활용도가 높은 것들 위주로 배울 예정. 



####  데이터 가져오기(c9기준)

1. db.csv 파일을 가져다 디렉토리에 넣기 (구글 공유폴더에 파일 있음)

2. 터미널실행 - `sqlite3` - `.mode csv`

3. `.import hellodb.csv hellodb`  디비.csv 파일을 가져와서 hellodb라는 시트를 만들겠다. 

4.  `.tables` 테이블을 다 보여줘  

5.  `SELECT*FROM hellodb;` 테이블로부터 다("*")선택해서 가져와줘 

   `SELECT last_name,first_name FROM hellodb;` 테이블에서 last_name이랑 first_name 가져와줘

   **SELECT는 데이터베이스에서 특정값을 반환한다.**

6. `.mode column` 칼럼별로 공간을 줘

7. `.headers on` 헤더를 다 보여줘 

   ```ter
   sqlite> .mode column
   sqlite> .headers on
   sqlite> SELECT*FROM hellodb;
   
   id          first_name  last_name   age         country     phone        
   ----------  ----------  ----------  ----------  ----------  -------------
   1           길동      홍         600         충청도   010-2424-1232
   ```



#### 데이터베이스 생성

1. `sqlite3 tutorial.sqlite3`

2. `.databases`테이블 생성 

3. 

   ```ter
   soowon:~/workspace $ sqlite3 tutorial.sqlite3
   SQLite version 3.8.2 2013-12-06 14:53:30
   Enter ".help" for instructions
   Enter SQL statements terminated with a ";"
   sqlite> .databases
   seq  name             file                                                      
   ---  ---------------  ----------------------------------------------------------
   0    main             /home/ubuntu/workspace/tutorial.sqlite3                   
   sqlite> CREATE TABLE classmates (
      ...> id INTEGER PRIMARY KEY,
      ...> name TEXT
      ...> );
   sqlite> .tables
   classmates
   ```

4. `.schema classmates` classmates의 구조를 보겠다 



####  테이블 및 스키마 조회

1. `.tabels`  현재 sqlite3파일에 들어있는 테이블들을 조회하겠다


####  테이블 삭제

1. `DROP TABLE classmates;` classmates라는 테이블을 삭제하겠다

   함부로 쓰면 데이터가 다 날아갈 수 있으니 조심! 함부로 쓰지 말자 


####  쉽게 명령 편집하기 

1. 터미널에서 실수했다면? ctrl +D 하던거 취소하고 나오기 

   한번 실수하면 계속 취소 해야 하니, 전체 명령어를 써서 불러오자. 

2. create_table.sql 파일 생성 - 명령어 전체 입력, 저장 

   ```sql
   CREATE TABLE classmate (
       id INTEGER PRIMARY KEY,
       name TEXT,
       age INTEGER
   );
   ```

   `sqlite3 tutoral.sqlite3` 'tutoral.sqlite3'라는 sqlite3파일을 (만들어)실행하겠다 

   -`.read create_table.sql` 명령어가 든 sql 파일을 읽어오겠다

   -`.tables` 현재 sqlite3파일에 들어있는 테이블들을 조회하겠다

3. 좀더 가보자!!!

   ```sql
   CREATE TABLE classmates (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name TEXT,
       age INTEGER NOT NULL,
       adress TEXT IS NULL
   );
   ```

   `id INTEGER PRIMARY KEY AUTOINCREMENT`: primary key인 id는 자동으로 상승하며 생성

   `age INTEGER NOT NULL`:  age에는 반드시 인티져값이 들어가야한다. 비면 안됨.

   `adress TEXT IS NULL`:  adress에는 값이 비어있어도 괜찮다. 


#### data 추가 (insert)

1. 특정 table에 새로운 행을 추가하여 데이터를 추가할 수 있습니다. 

   ``` terminal
    ALTER TABLE classmate
    ADD COLUMN twitter_handle TEXT;
   ```

   - `ALTER TABLE` is a clause that lets you make the specified changes. 
   - `ADD COLUMN` is a clause that lets you add a new column to a table: 
   - `twitter_handle` is the name of the new column being added



2. 기존 행에 데이터를 추가할 수 있습니다.

   ```terminal
    INSERT INTO celebs (id, name, age)
    VALUES (1,'Justin Bieber', 22);
   ```

   ```
   INSERT INTO celebs VALUES (1,'Justin Bieber', 22,'@justbieb');
   ```


####  data 수정 (update)

1. 특정 행 특정 열의 데이터를 수정할 수 있습니다.

   ``` terminal
    UPDATE celebs
    SET twitter_handle = '@taylorswift13'
    WHERE id = 4;
   ```

   - `UPDATE` is a clause that edits a row in the table. 
   - `celebs` is the name of the table. 
   - `SET` is a clause that indicates the column to edit.



#### data 삭제 (delete)

1. 특정 열을 조건에 맞춰 삭제할 수 있습니다.

   ```terminal
    DELETE FROM celebs
    WHERE twitter_handle IS NULL;
    SELECT *FROM celebs;
   ```

   - `DELETE FROM` is a clause that lets you delete rows from a table.
   - `celebs` is the name of the table we want to delete rows from.
   - `WHERE` is a clause that lets you select which rows you want to delete. Here we want to delete all of the rows where the twitter_handle column `IS NULL`.
   - `IS NULL` is a condition in SQL that returns true when the value is `NULL` and false otherwise.

2. 보통 유니크 식별자인 id로 삭제한다 : 이름으로 지울결우 동명이인의 가능성 있으므로 

   ``` DELETE FROM classmates
   DELETE FROM classmates
      ...> WHERE id = 2;
   ```

3.  삭제된 id 포함하여 누적된다  ; 123 중 2를 삭제하고 새로 작성했다면 134.. 로 누적

   ```
   sqlite> INSERT INTO classmates (name, age, adress) VALUES ('손지명',30,'서울');
   sqlite> SELECT * FROM classmates;
   ```

   ```
   SELECT * FROM classmates;
   id          name        age         adress    
   ----------  ----------  ----------  ----------
   1           강동주   34          서울    
   3           권혁주   29          강릉    
   4           손지명   30          서울 
   ```






#### new table ; Constraints

1. 새로운 테이블을 한번에 생성해 봅시다.

   Create a new table with constraints on the values.

   ``` terminal
   CREATE TABLE awards (
    	id INTEGER PRIMARY KEY,
    	recipient TEXT not NULL,
   	award_name TEXT DEFAULT 'Grammy'
   );
   ```

   ``` terminal
   CREATE TABLE celebs (
      id INTEGER PRIMARY KEY, 
      name TEXT UNIQUE,
      date_of_birth TEXT NOT NULL,
      date_of_death TEXT DEFAULT 'Not Applicable'
   );
   ```

   - `PRIMARY KEY` columns can be used to uniquely identify the row. Attempts to insert a row with an identical value to a row already in the table will result in a *constraint violation* which will not allow you to insert the new row.
   -  `UNIQUE` columns have a different value for every row. This is similar to `PRIMARY KEY` except a table can have many different `UNIQUE` columns.
   -  `NOT NULL` columns must have a value. Attempts to insert a row without a value for a `NOT NULL` column will result in a constraint violation and the new row will not be inserted.
   -  `DEFAULT` columns take an additional argument that will be the assumed value for an inserted row if the new row does not specify a value for that column.



####  데이터 선택적으로 조회하기

  **1.  LIMIT 과 OFFSET**

1. 우선 테이블 전체를 보자 

   ``` 
   SELECT *FROM classmates;     
   id          name        age         adress    
   ----------  ----------  ----------  ----------
   1           강동주   34          서울    
   2           정수원   28          부천    
   3           권혁주   29          강릉       
   ```

2. `SELECT id, name, age FROM classmates LIMIT 2;` : 2개까지만 보겠다

   ```
   id          name        age       
   ----------  ----------  ----------
   1           강동주   34        
   2           정수원   28 
   ```

3. `SELECT id, name, age FROM classmates LIMIT 1 OFFSET 1;` : 1개 건너띄고 1개만 보겠다

   ```
   id          name        age       
   ----------  ----------  ----------
   2           정수원   28   
   ```

   ex) 게시판에서 게시물을 한페이지에 50개씩만 보도록 LIMIT을 걸고, 특정 페이지를 보고자 하면 앞 페이지를 건너띄고 조회하는 OFFSET*페이지 를 걸 수 있다. : 페이지네이션 

**2. WHERE**

1. `SELECT * FROM classmates WHERE name = '강동주';`

   `SELECT * FROM classmates WHERE id is 3;`

   `SELECT id,name FROM classmates WHERE adress = '서울';  `

2. is 보다 = 를 쓰는 것이 더 공식적이다. ==도 가능하다. 참고









### 더 해보기 

1. users.csv 데이터베이스를 가져와라 

   ```
   sqlite> .mode csv
   sqlite> .import users.csv users
   sqlite> .tables
   classmates  users 
   ```

2. 카운트해줘라, 모든 개수를, users의?

   ```
   sqlite> SELECT COUNT(*) FROM users;
   COUNT(*)
   1000
   ```

3. 카운드해줘라, 모든 개수를,  user의, 나이가 30세 이상인? 

   ```
   sqlite> SELECT COUNT(*) FROM users WHERE age >30;          
   COUNT(*)
   386
   ```

4. 가져와라, 모든 user의 나이가 30세 이상인 데이터들을

   ```
   sqlite> SELECT * FROM users WHERE age >30;
   id,first_name,last_name,age,country,phone,balance
   1,"정호","유",40,"전라북도",016-7280-2855,370
   2,"경희","이",36,"경상남도",011-9854-5133,5900
   3,"정자","구",37,"전라남도",011-4177-8170,3100
   4,"미경","장",40,"충청남도",011-9079-4419,250000
   ...
   ...
   ... 
   ```

5. 성과 이름을 가져와라, user에서 나이가 30세 이상인 데이터들을  

   ```
   sqlite> SELECT last_name,first_name FROM users WHERE age >30;
   last_name,first_name
   "유","정호"
   "이","경희"
   "구","정자"
   "장","미경"
   ...
   ```

6. 데이터베이스에서 나이가 30이상이고 성이 '정'인 데이터의 성과 나이를 가져와라 

   ```
   sqlite> SELECT last_name, age FROM users WHERE age > 30 AND last_name = '정';
   last_name,age
   "정",38
   ```

7. 데이터베이스에서 발란스가 가장 큰 사람의 성과 이름을 가져와라 (성과 이름과 가장 큰 발란스값을 가져와라) 

   ```
   sqlite> SELECT first_name, last_name, MAX(balance) FROM users;
   first_name,last_name,MAX(balance)
   "선영","김",990000
   ```

8. 30세 이상인 데이터들의 발란스 평균을 가져와라 

   ```
   sqlite> SELECT AVG(balance) FROM users WHERE age>30;
   AVG(balance)
   154958.704663212
   ```

9. 선X  

   ```
   sqlite> SELECT * FROM users WHERE first_name LIKE "선%";
   id,first_name,last_name,age,country,phone,balance
   42,"선영","이",37,"충청북도",011-8272-1305,570000
   101,"선영","손",35,"경상북도",010-6837-7763,230
   ```

   | 2%   | 2로 시작하는 값 |
   | ---- | --------------- |
   |      |                 |

10. ```
    sqlite> SELECT *FROM users ORDER BY age ASC LIMIT 30;
    id,first_name,last_name,age,country,phone,balance
    11,"서영","김",15,"제주특별자치도",016-3046-9822,640000
    59,"지후","엄",15,"경상북도",02-6714-5416,16000
    ```

11. ```
    sqlite> SELECT *FROM users ORDER BY age DESC LIMIT 20;                                             
    id,first_name,last_name,age,country,phone,balance
    1,"정호","유",40,"전라북도",016-7280-2855,370
    4,"미경","장",40,"충청남도",011-9079-4419,250000
    28,"성현","박",40,"경상남도",011-2884-6546,580000
    53,"상훈","홍",40,"전라북도",016-7698-6684,550
    ```

12. ```
    sqlite> SELECT *FROM users ORDER BY age, last_name ASC LIMIT 10;                                  
    id,first_name,last_name,age,country,phone,balance
    295,"정수","강",15,"충청북도",02-7245-5623,500
    61,"우진","고",15,"경상북도",011-3124-1126,300
    998,"시우","고",15,"제주특별자치도",016-3732-8726,270
    ```


