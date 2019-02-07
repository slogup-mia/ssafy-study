# python Chatbot 1일차

1일차 파이썬 기반 챗봇 만들기

[챗봇플랫폼](https://s1.py.hphk.io/bots)

![pyhton](https://www.python.org/static/opengraph-icon-200x200.png)

## I. 기초 문법

### (1) 저장

#### 1. 개념

파이썬은 **dynamic typing language** -> 자료형 정의가 필요없다.

1. 숫자 

   ```python
   greeting = "hello world"
   ```

2. 글자

3. Boolean

#### 2. 실습

``` python
# 변수 활용하기
greeting = "안녕하십니까"
print(greeting)
print(greeting)
print(greeting)
print(greeting)
print(greeting)
```

1. 리스트

   ```python
   menu = ["김치찌개", "해장국", "햄버거", "구내식당", "중화요리"]
   ```

   1-1 리스트 중 랜덤선택하기 

   ```python
   import random
   menu = ["김치찌개", "해장국", "햄버거", "구내식당", "중화요리"]
   choice = random.choice(menu)
   print(choice)
   ```

2. 조건 (if/else)

   ```python
   if(True):
   	print("조건문입니다.")
   ```

   ```python
   url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?ServiceKey={}&sidoName=서울&pageNo=3'.format(key)
   response = requests.get(url).text
   soup = BeautifulSoup(response, 'xml')
   gn = soup('item')[7]
   location = gn.stationName.text
   time = gn.dataTime.text
   dust = int(gn.pm10Value.text)
   
   print('{0} 기준: 서울시 {1}의 미세먼지 농도는 {2} 입니다.'.format(time, location, dust))
   
   if dust > 150 :
     print ("매우나쁨") 
   elif dust > 80 : 
     print ("나쁨") 
   elif dust > 30 : 
     print ("보통") 
   else : 
     print ("좋음") 
   ```

   ```
   2018-12-17 13:00 기준: 서울시 강남구의 미세먼지 농도는 93 입니다.
   나쁨
   ```

3. 반복

   3-1 반복 while 

   ```python
   n=0
   while n<3:
       print("출력")
       n=n+1
   ```

   ```resul
   출력
   출력
   출력 
   ```

   3-2 반복 for 

   ```python
   dust = [59,24,102]
   for i in dust: 
       print(i)
   ```

   ```result
   59,24,102
   ```

   ```python
   #list를 돌면서 프린트하기01
   for name in ["강동주","유태영","전민호"]:
     print(name)
   
   #list를 돌면서 프린트하기02  
   names = ["강동주","유태영","전민호"]
   for name in names:
     print(name)
   ```

   ```resul
   강동주
   유태영
   전민호
   ```



## II. 개발 계명 (development Commandments)

### 1. 브라우저는 Chrome 이다.

### 2. 문서는 마크다운(.md)이다.

### 3. 교과서는 공식문서 & 내가 정리한 마크다운이다. 



## III. API 

### 1. 미세먼지 데이터는 어디서 왔을까

#### 1-1. API : 다른 시스템 간의 커뮤니케이션

- Application Programming Interface,  응용프로그램 프로그래밍 인터페이스 

- 웹(WEB)에서의 커뮤니케이션 방식 

  : 요청(request with URL)과 응답(response with XML, Jason, HTML)

- 활용 예 : 간편하게 가입하기 - 페이스북으로 시작하기 

  ​		카카오톡 API / 네이버지도 / Riot / 공공데이터 API 

  => 서비스와 서비스간의 대화방식 

  => 요청을 받는 측에서 일정한 방식을 명세 - 정보제공


#### 1-2. 데이터 요청하기

- [공공데이터포털](www.data.go.kr) 

  ```python
  url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?ServiceKey={}&sidoName=서울&pageNo=3'.format(key)
  response = requests.get(url).text
  soup = BeautifulSoup(response, 'xml')
  gn = soup('item')[7]
  location = gn.stationName.text
  time = gn.dataTime.text
  dust = int(gn.pm10Value.text)
  ```

- 만들어진 코드를 활용하기 == 오픈소스 활용하기  :  함수를(function) 써보자



## IIII. 함수

#### 1. 외장함수

1-1. random.choice (배열) : 복원추출

1-2.random.sample(리스트,개수) : 비복원 추출

#### 2. 외장함수 활용

``` python
# 1. random 외장 함수 가져오기
import random 
# 2. 1~45까지 숫자 numbers에 저장하기
numbers = list(range(1,46))
  	 # range(1,46)로 해도 가능. 위는 list안에 깔끔명료하게 저장하기 위함. 
# 3. numbers에서 6개 뽑기
lotto = sorted(random.sample(numbers,6))
 	 # 내장함수 sorted : 작은 숫자부터 출력되도록 한다. / 원본유지,복사본을 쏘팅
 	 # cf) 내장함수 sort : 원본파괴. 원본자체를 쏘팅한다. distructive method 
# 4. 출력하기
print(lotto)
```

```resu
[2, 3, 4, 16, 40, 45]
```



 ## V. GIT 

ls : 모든 파일 나열 

pwd : 내 작업 위치 

mkdir : make directory (새폴더만들기)

cd : change directory (폴더로 이동)

폴더명 쓰다가 Tab : 자동완성 

exit : 끄기 

현재 디렉토리 표시 

code . + Enter 

clear : 내용 모두 지우기 

Ctrl + Insert : 복사 

Shift + Insert : 붙여넣기 

* [Git tips](https://cyberpass.blog.me/221037298316)
* [git bash기본 사용법](http://gbsb.tistory.com/10)





##  VI. Shell

#### 1 . 컴퓨터 조작하기 - 웹브라우저 조작하기

1-1. 웹브라우저 열기

```shell
>>> import webbrowser
>>> url= "http://daum.net"
>>> webbrowser.open(url)
True
>>> webbrowser.open_new(url)
True
>>> webbrowser.open_new_tab(url)
True
```

1-2. 검색하기  "SSAFY"

```shell
>>> search_url = "https://search.daum.net/search?q="
>>> webbrowser.open(search_url + "SSAFY")
True
```

```shell
#mission 1
#webbrowser, "ssafy", "samsung", "sw", "coding"
#반복문 활용 

keywords =["ssafy", "samsung", "sw", "coding"]
for i in keywords: 
webbrowser.open(search_url + i)

```



##  VII. Python

* 다운로드 시 : [python path](https://medium.com/@psychet_learn/python-%EA%B8%B0%EC%B4%88-2%EC%9E%A5-python-%EC%84%A4%EC%B9%98-%EB%B0%8F-%ED%99%98%EA%B2%BD%EC%84%A4%EC%A0%95-windows-ver-b030d96bcbd0) 설정 

1-1. 정보 스크랩하기 (크롤링하기)

​	자주 확인하는 정보를 자동 스크랩하기 

- request 패키지를 인스톨  :​	`$ pip install requests                                                          `

  bs4 인스톨 : 	`$ pip install bs4                                                          `

  ​			pip : pyton install package

```shell
request.get(주소)
request.get(주소).text
request.get(주소).status_code 
```

```visual s
bs4.BeautifulSoup(문서)
bs4.BeautifulSoup.Select(경로)
bs4.BeautifulSoup.Select.one(경로) 
```

가져오려는 내용 마우스 커서 올리고 우클릭 - 검사하기 - 해당 내용 우클릭 - copy - copy selector 

```visual s
#kospi 정보를 스크랩한다. 
import requests 
import bs4 

url = "https://finance.naver.com/sise/"

response = requests.get(url).text

doc = bs4.BeautifulSoup(response,'html.parser')

result = doc.select_one('#KOSPI_now')

print(result.text)
```

```git bash
student@M7012 MINGW64 /
$ cd ~

student@M7012 MINGW64 ~
$ ls
'3D Objects'/
 AppData/
'Application Data'@
 chatbot/
 Contacts/
 Cookies@
 Desktop/
 Documents/
 Downloads/
 Favorites/
 Intel/
 Links/
'Local Settings'@
 Music/
'My Documents'@
 NetHood@
 NTUSER.DAT
 ntuser.dat.LOG1
 ntuser.dat.LOG2
 NTUSER.DAT{bbd90b96-e875-11e8-b39d-988389879652}.TM.blf
 NTUSER.DAT{bbd90b96-e875-11e8-b39d-988389879652}.TMContainer00000000000000000001.regtrans-ms
 NTUSER.DAT{bbd90b96-e875-11e8-b39d-988389879652}.TMContainer00000000000000000002.regtrans-ms
 ntuser.ini
 OneDrive/
 Pictures/
 PrintHood@
 Recent@
'Saved Games'/
 Searches/
 SendTo@
 Templates@
 Videos/
'시작 메뉴'@

student@M7012 MINGW64 ~
$ cd chatbot/

student@M7012 MINGW64 ~/chatbot
$ ls
day1/

student@M7012 MINGW64 ~/chatbot
$ cd day1/

student@M7012 MINGW64 ~/chatbot/day1
$ ls
hello.py  scrap.py

student@M7012 MINGW64 ~/chatbot/day1
$ python scrap.py
```



1-2. 파일명 바꾸기

```visual 
os.chdir(r'폴더주소') 
os.getcwd() 현재 경로 불러오기
os.listdir('') 경로 바꾸기 
os.rename('처음이름', '바뀐이름')
```

``` visual studio code
import os

print(os.listdir('.'))

os.chdir(r'c:\Users\student\chatbot\day1\list')

print(os.getcwd())

# print(os.listdir('.'))

os.rename('hello.txt', 'changed.txt')
```

* mission : https://zzu.li/file  에서 더미파일을 다운받아 파일명을 바꿔라  

  압축풀어 day1 폴더(작업폴더)안에 넣는다.

```visual studio code
#mission 500명의 명단 파일 이름앞에 'SSAFY_'를 추가수정하라.  

import os 

os.chdir(r'c:\Users\student\chatbot\day1\list')

fileList = os.listdir('.')
#filelist는 리스트 형태이다. 500명의 명단이 들어있는. 

for i in fileList :
    os.rename(i, 'SSAFY_'+ i)
   #os.rename(i, i[5:]) => 이름 앞부분을 지울 수 있다. 
```



import os 

os.chdir(r'c:\Users\student\chatbot\day1\list')

filelist = print(os.listdir('.'))

#filelist는 리스트 형태이다. 500명의 명단이 들어있는. 



# 참고

- http://pythontutor.com/  
  ​    : VISUALIZE CODE AND GET LIVE HELP
- https://s1.py.hphk.io/bots : python chatbot 
- https://github.com/tensorflow/tensorflow
- https://chocolatey.org
- markdown -typora  : NOTE FOR SW developer 

* https://docs.python.org/ko/3/library/functions.html : 파이썬 내장함수 

* https://git-scm.com/download/win 윈도우용 . 디폴트값으로 설치 

* https://code.visualstudio.com/ 
  기타 옵션:  'code를 ... 추가' 체크박스 네개 모두 체크 하여 설치
