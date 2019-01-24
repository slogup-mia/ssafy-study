# CSS



### 4. Display

#### 1) block

새로운 라인에서 시작한다. 

프로 길막러다.  다음 코드가 와도 화면 왼쪽끝-오른쪽끝까지 차지한다. 

화면 크기 전체의 가로폭을 차지한다. (width:100%) 한줄을 다 차지

블럭 레벨 요소 내에 inline 레벨 요소를 포함할 수 있다. 

ex) p,ol, ul, li, ht,table, form,div,h1~h6 

```<h1 width:50%> 이렇게 자기 크기가 작아져도 남는 부분은 마진으로 차지 </h1>```

#### 2) inline

얘는 크기정보(패딩 보더 등)가 없다.

항상 컨텐츠 길이만큼만 공간차지를 한다.   

새로운 라인에서 시작하지 않고, 문장 중간에 들어갈 수 있다.

width, margin-top,margin-bottom,height 프로퍼티를 지정할 수 없다.

margin-left,margin-right는 지정 가능하다. 

상,하 여백은 line-height로 지정한다.

ex) a href, img, br, input, select, span, a, strong, 



**아래는 :** 

태생적으로 block의 성격을 가진 ul을 inline의 모양을 띄게 style을 먹여 주는 것이다. 

(= 한줄이 한줄씩 다 차지하는 block의 모양이아니라 inline처럼 쪼르르 위치하게끔 만들어준다.)

 그래서 아래처럼 ul에 마진값을 넣어줘도 값이 들어가긴 하지만 실제로 마진폭이 들어가진않는다. 

```html
    <style>
    ul{
        margin-top: 16px;
        margin-bottom: 16px;
        margin-left: 16px;
        margin-right: 16px;
    }
    ul{
        display:inline;
    }
    li {
        display:inline;
    }
    </style>
</head>
<body>
    <ul>
        <li>파이썬</li>
        <li>CSS</li>
        <li>HTML</li>
    </ul>
</body>
```

#### 3) None

해당 요소를 화면에 표시하지 않는다. 사라진다. 

얘가 차지하던 공간 자체가 사라진다. 

```html
<head>
    <h2>
        
    </h2>
    None 먹이는 방법 !!!!!!!!!!!!!! 다시 알기 
</head>
```

#### 4)visibility 

- visible

  해당요소를 보이게 한다.

- hidden

  해당요소를 안보이게 한다. (컨텐스만 숨기고 자리는 그대로. )

  ```html
  <style>
           h2{
              visibility: hidden; 
          }
  </style>
  ```

#### 5) background image

화면 전체의 백그라운드 컬러를 먹이고 싶을땐 : 

```html
헤드 style   body{백그라운드-이미지: 컬러코드}
```

화면 전체에 백그라운드 사진을 먹일때:

```html
	헤드 스타일 바디{백그라운드-이미지:'이미지url';

				백그라운드-repear:no-repeat;

				background-position: center;

				background-size:cover;}
```

#### 6) font 

https://fonts.google.com/

https://spoqa.github.io/spoqa-han-sans/ko-KR/

웹에서 제공하는 폰트를 가져다가 쓸 수 있다! 

```html
<head>
    <link href='// 각 페이지에서 제공하는 코드주소'>
    <style>
        *{
            font-familu: '각 페이지에서 제공하는 폰트패밀리 코드(를 모든 글씨에 먹이겠다)'
        }
        a{
            font-family: '각 페이지에서 제공하는 폰트패밀리 코드(를 a태그에 먹이겠다)'
        }
    </style>
</head>
<body>
    
</body>

```



### CSS의 구체화 순서, 상세정도 순서 (순위)

1. !important 형님
2. inline tag     
3. #id   
4. .class
5. tag 이름
6. global



### CSS의 선언 순서 (우선순위)

1. 무조건 뒤에 정의된 친구가 적용된다.



### 5. Positioning 위치 

#### 1) static (기본위치)

기본적인 요소 배치 순서에 따라 위-아래로, 왼-오른쪽으로 순서에 따라 배치된다

부모요소 내 자식 요소로서 존재할 때는 부모 요소의 위치를 기준으로 배치된다. 

=> 부모div 가 div자식을 가질때: div는 한줄을 다 차지하는 block요소니까 부모가 끝나는 위치를 기준으로 자식의 위치가 놓이게 된다. 

#### 2) relative(상대위치)

기본 위치(static으로 지정되었을 때의 위치)를 기준으로 좌표 프로퍼티(top,bottom,left,right)를 사용하여 위치를 이동 

#### 3) (절대위치)

무보 요소 또는 가장 가까이 있는 조상 요소(static 제외)를 기준으로 좌표 프로퍼티만큼 이동한다. 

즉, relative, absolute, fixed 프로퍼티가 선언되어 있는 부모 또는 조상 요소를 기준으로 위치가 결정된다. 



#### 4) fixed (고정 위치)

부모 요소와 관계없이 브라우저의 viewport를 기준으로 좌표 프로퍼티를 사용하여 위치를 이동시킨다.

스크롤이 되더라도 화면에서 사라지지않고 항상 같은 곳에 위치한다. 

ex) 네비게이션바, sticky footer 

