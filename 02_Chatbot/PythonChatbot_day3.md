#  PythonChatbot_day3

##  Cloud9

* https://c9.io

  AWS : Amazon Web Service 웹개발을 가볍게 할 수 있음.

####  url의 의미

* https://www.naver.com : 누구에게 보낼지 (요청받는 사람의 주소)

*  / : 가장 기본이 되는(root) 페이지를 주세요 

  ​	ex) https://www.naver.com/ 네이버야 네이버 기본페이지 주세요

*  /xxx :  무엇을 받을지 

*  /search.naver : 네이버야 검색해줘 

*  ?xx : xx이러한 정보를 담아 보낼게 (파라미터 정보)

  ​	ex) ?chat_id=123403958&text=hello

* ?query=xx : 이런 단어를 담아 보낼게 == xx를 검색해줘



####  cloud9으로 편리하게 개발하기 

```py
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    
@app.route("/name")
def name():
    return "Soowon Jung"
    
	# /hello/john => "hello john"
	# /hello/Michael => "hello Michael"
@app.route("/hello/<name>")
def hi(name):
    return "hello " + name 
    
    
    # /cube/2 ==> 8 : 2의3승
    # /cube/3 ==> 27: 3의3승
@app.route("/cube/<num>")
def cube(num):
    result = int(num) ** 3
    return str(result)
    #int : 문자로 인식된 num값을 숫자로 바꾸기 
    #str : 숫자로 받기 
    
    # return str(num**3) 한줄로 줄일 수 있음 
    #return pow(3,num) 가능할까? 세제곱함수 
    
    
    # /reverse/hello ==> olleh 
@app.route("/rev/<word>")
def rev(word):
    return str(word)[::-1]

    # /palindrome/racecar ==> true 
    # /palindrome/hello ==> false 
@app.route("/pal/<word>")
def pal(word):
    return str(word == word[::1])
    
    #아래 코딩으로 가능할까? 
    #result = str(word)[::-1]
    #if result == str(word)  -> 여기서 오류가 왜 날까 
    #return true
    #else return false
```

``` c9
soowon:~/workspace $ sudo pip3 install flask

$ flask run --host=0.0.0.0 --port=8080
# 서버돌리기 - 새로저장 후 서버돌릴땐 ctrlC로 서버취소하고 다시
```

-> 우측상단 share - application 주소클릭 - 열기 : 웹 페이지 결과 확인 가능

-> https://flask-soowon.c9users.io/name  url에 name추가하여 요청하면 

   @app.route .... 이하 명령에 대한 결과창으로 이동 

-> url.../hello/name 추가하여 요청하면 "hello name" 





#  HTML

* visual studio에서 새파일.html 을 만들면 html로 코딩할 수 있다. 

*  ctrl + /  : 주석 

* ! + tab  : html의 기본코드 자동완성. 개꿀!! 

* h1 + tab : <h1></h1> 태그 자동완성, 다른 태그도 마찬가지

* 파일.html 을 열면 디벨롭된 웹을 열어서 결과 확인 가능. 

  ``` visual html
  <!DOCTYPE html>
  <html>
      <head>
          <!-- 머리 : 상대적으로 덜 중요한 부분(문서에 대한 정보) -->
          <title>HTML 테스트</title>
          <!-- meta charset="utf-8"
              위는 firefox에서 돌릴때 한글을 지원하도록 하는 코드 -->
      </head>
      <body>
          <!-- 몸통 : 중요한부분 -->
          <h1>HTML 테스트</h1>
          <!-- 가장 중요한 내용  -->
          <h2>부제목</h2>
          <P>안녕하세요</P>
          <p>HyperText Markup Language
              가장큰 특징은 링크를 만들 수 있다는 점 
              문서들간의 연결묶음!
              지식의 생태계를 구성하는 요소~ 
          </p>
          <a href="https://www.naver.com">네이버로 가는 링크</a>
          <!-- herf : hyper reference의 약자 -->
          <img src="https://img.insight.co.kr/static/2018/09/08/700/z05iby35955xer75h8x4.jpg"> 
          <!-- img태그는 열고 닫지 않는다. 단태그 -->
          <iframe width="560" height="315" src="https://www.youtube.com/embed/f_EbM1uhUNo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
          
  
      </body>
  </html>
  ```

```visual html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>SoowonJung</title>
</head>
<body>
    <h1>SW's</h1>
    <p>p tag: I'll be a Frontend develper</p>
    <p>p tag: no pain no gain</p>
    <p>-------------------------------------------</p>
    <div>div tag: I'll be a Frontend develper</div>
    <div>div tag: no pain no gain</div>
    <table>
        <tr>
            <td>나이</td><td>20's</td>
        </tr>
        <tr>
            <td>주소</td><td>경기</td>
        </tr>
        <tr>
            <td>전공</td><td>경영</td>
        </tr>
    </table>

    <ul>
        <li>soup</li>
        <li>pasta</li>
        <li>burger</li>
    </ul>

<img src="https://img.insight.co.kr/static/2018/09/08/700/z05iby35955xer75h8x4.jpg" alt="웰시코기옹동이">
    <!-- alt : 사진 설명 -->

</body>
</html>
```









#  CSS basic

CSS : 옷입히기 



*  색 설정하기 

``` visual html
    <!-- alt : 각 태그 안에 직접 색 설정할 수 있다  -->
	<h1 style="color: royalblue">SW's</h1>
    <p style="color: purple">p tag: I'll be a Frontend develper</p>
```

```visual html
    <!-- alt : head 안에서 색을 지정하면 div, p, body등 각 태그의 색을 지정할 수 있다. -->
head
<head>
div{
        color :seagreen
    }
    p{
        color :skyblue
    }
    body{
        background-color: beige
    }
    </style>
</head>
```

​	*   class 선택자 :  .

​	*    id 선택자 : # 

```html
<head>
	...

	<style> 
    .text{
        color :seagreen
    }
    #header{
        color :skyblue
    }
    body{
        background-color: beige
    }
    </style>
</head>
<body>
    <h1 id="header">SW's</h1>
    <p >p tag: I'll be a Frontend develper</p>
    <p>p tag: no pain no gain</p>
    <p>-------------------------------------------</p>
    <div class="text">div tag: I'll be a Frontend develper</div>
    <div>div tag: no pain no gain</div>
    ...
</body>
```



###  CSS 튜토리얼

* [css-tricks.com](css-tricks.com )

* [w3schools.com](w3schools.com)

#### 탬플릿 소스 

* [https://startbootstrap.com](https://startbootstrap.com)
* [https://getbootstrap.com](https://getbootstrap.com)











##  참고

*  zzu.li/flask : flask로 app만들기 튜토리얼 

* `$ code .` in gitbat : 현재 폴더상에서 코드를 짜겠다 

  ​					-> visual studio 켜짐

* shift + \ :  '|'      '|이름|나이|혈액형|'   : 테이블 생성

  | 이름 | 나이 | 혈액형 |
  | ---- | ---- | ------ |
  |      |      |        |

* class 선택자 :  .

*  id 선택자 : # 



