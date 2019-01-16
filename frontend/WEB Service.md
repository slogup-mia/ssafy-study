# Intro to WEB Service

- web site 는 협소한 의미 - 특정주소의 특정 리소스만을 의미 

- 우리는 SaaS (Software as a Service)를 만든다.  

- 관련 강의 : https://www.edx.org/course/agile-development-using-ruby-on-rails-the-basics -> 매우 재미있게 꾸려놨다.

- service는 요청과 응답으로 이루어진다. 



#### 요청의 종류

- 줘라(Get)
- 받아라(Post)



#### web developer chrome extension

https://chrome.google.com/webstore/detail/web-developer/bfbameneiokkgbdmiekhjnmfkcnldhhm?hl=ko

- 웹사이트의 자바스크립, 레이아웃을 간편하게 알려주는 (까발릴수있는)
- 태그분석에도 용이 
- css의 역할파악에 도움이 된다. 



#### Octotree 

https://chrome.google.com/webstore/detail/octotree/bkhaagjahfmjljalopjnoealnfndnagc?hl=ko

- 깃헙의 특정 리퍼지토리에 가면 파일 소스코드의 파일트리를 알수 있다. 



DNS : Domain Name System 

- 아이피주소를 우리가 흔히 아는 http주소로 전환해주는 시스템 
- 185.274.164.72.  -> www.naver.com 





#### 도메인 구매

https://aws.amazon.com/ko/route53/

https://kr.godaddy.com/

- 도메인(주소)을 살 수 있는 곳
- aws.amazon에서 1만원/2년 정도면 살 수 있다. 
  - 인증서 관리도 해줘서 좋다. 
- .com 이 제일 비싸다 



#### IP

- Internet Protocol
- 172.271.27.78
- 8비트 (0~255) 까지의 숫자로 구성된 숫자의 집합으로, 각자가 가지고 있는 주소와 동일하다.
- 키벨류페어

#### Domain 

- 네트워크상의 컴퓨터를 식별하는 호스트명 
- google.com

#### URL

- 도메인 + 경로, 실제로 해당 서버에 저장된 자료의 위치
- https://www.google.com/doodles/
- 명시적이고 표준적이고 구조화된 url 구성이 중요해졌다.

#### Dynamic Web / Web App 



#### w3c 

- https://www.w3.org/

www은 법제정도 없고 만들어놓은 기술에서 모두 사용하던 방법이 표준이 됐다.

그러나 의견 충돌이 있어왔다.  ex) 마소에서 표준 외 익스플로러 개발 , 표준외 규칙을 제정해 개발자들이 따르도록 하여 사용자가 아닌 마소의 입맛대로 지배력을 가졌다. - 크롬이 표준을 지키는 브라우저를 제공하여 압도적인 점유율을 갖게 되었다.

w3c는 표준에 대한 제안을 하고 받아들이는 장이라고 보면 됨. 

=> 이 전보다 브라우저 대응이 수월해졌다. ex) 파폭, 익스, 크롬에 맞게 따로 코딩했어야 했다. 이제는 크롬에서만 돌아가게 해놓으면 웬만한 브라우저에서는 돌아간다. 표준이 잘 세워져 있으므로.  



#### HTML

- hyper Text Markup Language 

- 가독성이 떨어지는 문서를 마킹하는 언어. 

- 문단, 글자, 단어, 문장의 역할을 정해준다. 

- </큰제목> </작은제목> </본문> ...   
- Hyper Text : 기존 선형적 텍스트가 아닌 비선형적 텍스트를 일컫름 



#### CSS

- Cascading Style Sheet 

- Cascading 방식 : https://poiemaweb.com/css3-inheritance-cascading

  - 상속화된 속성 전달방식, 폭포처럼 
  - 참고) poiemaweb.com 웹관련 설명이 매우 잘 되어있는 페이지

- 어렵다. 

  - 이미 관리하기 쉽게 만들어진 프레임워크를 쓴다. 

  - 그래서 쓰는게 Bootstrap (by Instagram)
  - 부트스트랩을 쓴다해도 CSS에 대한 이해가 기본 



#### Java Scrip 

- CSS가 옷을 입히는 것이라면, 자바스크립트가 움직이게 한다.
- 파이썬과 매우 닮아 있어서 조금 괴랄한 언어지만 파이썬 학습 이후에는 난이도가 높지 않다. 
- 이름이 자바인 이유는 개발당시 자바가 유명해서..
  - 웹 생태계에서는 유명한 표준의 영향력이 매우 크다는 예
  - 자바스크립트와 자바의 다른점은 바다코끼리와 코끼리의 차이와 같다.
- ES6 :  자바스크립트를 구현하는 모듈



```
<!DOCTYPE html>      -> 문서 타입 선언
<    >
<head>
	<meta charset ="">
 ...
</head>
<body>
 ... 
</body>
```



## Tag와 DOM TREE 

### Document object model



#### 1.요소 

HTML의 element는 태그와 내용으로 구성되어 있다. 

```<h1>웹문서 </h1>```

태그는 대소문자를 구분하지 않으나 소문자로 작성하는게 표준



#### 2. self-closing element

닫는 태그가 없는 태그도 존재

``` <imp src ='url'/>```

id,class, style은 태그와 상관없이 모두 사용 가능하다 



#### 3. 속성(Attribute)

태그에는 속성이 지정될 수 있다. 

``` <a href ='google.com'/>```

  a 속성명 = '속성값'



#### 4. DOM Tree 

태그는 중첩되어 사용가능하며, 이때 다음과 같은 관계를 갖는다. 

[DOM Tree image](https://www.google.com/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwiHxN_qmPHfAhVIM94KHSMhBU0QjRx6BAgBEAU&url=https%3A%2F%2Ftuftsdev.github.io%2FWebProgramming%2Fnotes%2Fdom.html&psig=AOvVaw3QZBOmjT0XUBJv7044QadW&ust=1547690030284045)

- DOM : document object module
- 태그를 구조화, 객체화해서 thml모듈을 효율적으로 빠르게 돌아가게 한다. 



#### 5. 시맨틱태그 

컨텐츠의 의미를 설명하는 태그

HTML에 새롭게 추가된 시맨틱 태그가 있다. 시맨틱 태그 활용한 페이지가 대세

개발자 및 사용자 뿐만 아니라 검색엔진 등에 의미있는 정보의 그훕을 태그로 표현하여 단순히 보여주기 위한 것을 넘어서 의미를 가지는 태그들을 활용하기 위한 노력

|  태그   |                    설명                    |
| :-----: | :----------------------------------------: |
| header  |                    헤더                    |
|   nav   |    내비게이션 (페이지 상단 탐색링크 바)    |
|  aside  |              사이드 폴더구조               |
| section |       페이지 중앙 섹션별 컨텐츠 그룹       |
| article |                                            |
| footer  | 페이지 하단 또는 구석에 위치한 페이지 정보 |

- https://news.google.com/?hl=ko&gl=KR&ceid=KR:ko

  http://webtoon.daum.net

  - 최근 표준을 매우 잘 지키고 있는 예 

- 그리드 시스템을 바탕으로 컨텐츠들을 비율에 맞게 배치하고 있다. 

- 사용성, search engine optimization의 활용성을 높이기 위해서는 태그표준을 지키는게 중요하다. ex) 검색엔진에 자동 노출되는 방식, 시각장애인의 웹사용환경 구성 등 
