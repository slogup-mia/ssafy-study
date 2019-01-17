# Frontend

## HTML

- `ctrl /` 주석처리  

- 구분줄넣기

  `<hr>`

- 리스트 

  - `<ol></or>`
  - `<ul></ur>`

- 항상 한국어로 링귀지 바꿔주는것 잊지말기 

  `<html lang="ko">`

- 글씨크기 조절

  `<h2 style="color: green; font-size: xx-large">파이썬</h2>`

  font-size : 150% , large, 35px, 1em(=100%) 세가지 단위로 지정 가능   

  - 브라우저마다 기본 글씨크기, 글꼴 등이 다르다. 

- 컬러코드 가져오기 : https://htmlcolorcodes.com/



  ### 중복되는 코드 간편하게 설정하기 

  ex) 모든 h3에 동일한 컬러 먹이고 싶어  

  - head에서 설정한다.

    ```
    <style>
            h1{color:#34495E}
            h2{color:teal; font-size: 6em}
            h3{background-color:#FAD7A0 ;color:#b22223}
            p{background-color: darkgrey}
            .grey-font {color: gray}
        </style>
    </head>
    ```

  - grey-font 클래스 설정하고 `.grey-font {color: gray}`

    ```
    <body>
    ...
        <strong class = 'grey-font'>클래스설정</strong>
        <li class ='grey-font'>str</li>
    ...
    </body>
    ```

    위와같이 클래스를 먹이면 해당 글씨색으로 설정된다. 

  - 스타일 요소가 많아지면 html이 너무나 길어진다 

    - style.css 파일 생성

      ```
      h1 {
          color:#34495E
      }
      
      h2 {
          color:teal; font-size: 6em
      }
      
      h3 {
          background-color:#FAD7A0 ;color:#b22223
      }
      
      p {
          background-color: darkgrey
      }
      
      .grey-font {
          color: gray
      }
      ```

      html 헤드 부분 에는 아래와 같이 불러온다. 

      ```
      <link href ='style.css' rel='stylesheet'>
      </head>
      ```

- id를 설정하고 id를 먹이기 

  html

  ```
  <p id='salmon'>파이썬에서 숫자형은 아래와 같이 있다.</p>
  ```

  css 

  ```
  #salmon {
      background: darksalmon;
  }
  ```

  id는 동적으로 한꺼번에 설정변경이 가능하다.

  css보다 자바스트립트에서 많이 활용된다. 







- `<meta name="viewport" content="width=device-width, initial-scale=1.0">`

  앞으로 컨텐트 폭과  이니셜스케일을 뷰포트 단위의 디바이스폭, 1.0으로 하겠다. 





프로퍼티 값의 단위 

h1{color:blue;font-size:15px;}     



## Box model

thml을 렌더하는 데에서 가장 중요한 부분

검사 - style - 

- -padding,border,margin 의 두께를 설정

- -`element.style{ border style: solid}`

bootstrap을 쓰면 박스모델 설정하면서 꼬이지 않도록 편하게 한다.  





##  Bootstrap

- https://getbootstrap.com/docs/4.2/getting-started/introduction/
- install보다는 CDN(content delivery network)을 통해 부트스트랩이 작성된 CSS, JS를 활용하자
- HTML파일 head 안에 CSS부분을 카피하여 붙여넣는다. 

```
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">    #이부분 
    <title>프로그래밍 교육</title>
</head>
```

- https://getbootstrap.com/docs/4.2/content/typography/

  타이포그래피 부분을 css설정하는 부트스트랩 소스가 있는 페이지이다.

  설명을 보고 html에 코드를 바르게 복붙하기만 하면 구현된다!

- https://learn.freecodecamp.org/

  html, css 강의가 매우 좋다. 





###  1. Spacing 

`.m-0`: 마진을 0으로 주겠다. 

`.mr-0` `.ml-0`: 오른쪽, 왼쪽 마진을 0으로 주겠다. 

`.mt-0` `.mb-0` : top, bottom 

`.mx-0` `.my-0`: x,y축

`.py-0` 세로y축 패딩을 0으로 주겠다. 

`.mt-1`: margin top을 0.25rem(약 4px) 으로 주겠다 

`.mt-2` 0.5rem 8px

`.mt-3` 1rem 16px

`.mt-4` 1.5rem 24px 

`.mt-5` 3rem 48px

`.my-n0` 마이너스마진 

`.mx-auto` 디스플레이 옵션,나중에.. 



###  2. Color

부트스트랩은 색을 원색에서 약간 파스텔화 시킨다. 이뻐

그런데 이름이 일반적이진 않다. 

`primary` 파랑 

`secondary` 회색

`success` 연두

`warning` 빨강

`light` 흰

`dark` 어두운회색



### 3. Border 

```
 <p class = 'mx-1 border rounded'>라운드 </p>
    <p class = 'mx-2 border rounded-top'>위에만 라운드</p>
    <p class = 'mx-3 my-3 border rounded-circle'>마진x3 마진y3 rounded-circle</p>
    <p class = 'mx-5 my-5 border rounded-pill'>마진x5 마진y5 rounded-pill</p>
```



### 4. Display

[css grid](https://www.google.com/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjM5I3w3vHfAhVBeXAKHR0ABF0QjRx6BAgBEAU&url=https%3A%2F%2Fwebkit.org%2Fblog%2F7434%2Fcss-grid-layout-a-new-layout-module-for-the-web%2F&psig=AOvVaw16DYlIDJwtc4qf-DFfUDWB&ust=1547708830873833)를 보기좋게 나누어 배치하는 것은 매우 중요하다. 

16,24개 등 여러개 그리드를 혼용하여 사용했었다.  

모던 웹에서는 12개로 표준화되었다. 약수가 많아서 12.  

그리드에 관한 부트스트랩 소스  : https://getbootstrap.com/docs/4.2/layout/grid/  

그리드에 관한 CSS 정리 :https://developer.mozilla.org/ko/docs/Web/CSS/CSS_Flexible_Box_Layout/Flexbox%EC%9D%98_%EA%B8%B0%EB%B3%B8_%EA%B0%9C%EB%85%90

그리드를 재미있고 쉽게 학습하기  :https://flexboxfroggy.com/

1. gird.html에 부트스트랩 - start - css, js코드를 헤드나 바디에 복붙 

2. 바디에 2중 div 

   ```
       <div class = 'container'>
           <div class ='row'>
   
           </div> 
       </div>
   ```

   - 여기서 container 클래스 :  반응형 ; 창을 줄이면 콘텐츠도 같이 줄어듦

     ​						container-fluid로 쓰면 패딩이 조금 덜 먹힌다. 

   - row 클래스 :  행구분  ㅡ>   (cf. col 클래스 : 열||||) 

3. -1 부트스트랩 -컴포넌트 -카드 코드 복붙 

   ```
       <div class = 'container'>
           <div class ='row'>
               <div class="card" style="width: 18rem;">
                   <img src="..." class="card-img-top" alt="...">
                   <div class="card-body">
                       <h5 class="card-title">Card title</h5>
                       <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                       <a href="#" class="btn btn-primary">Go somewhere</a>
                   </div>
               </div>
           </div> 
       </div>
   ```

4. -2 -1

   ```
   
   ```

   -2 -2

   ```
       <style>
           .vivid_bd{
               background-color: burlywood;
               border: 10px;
               border-style:double;
               border-color: aquamarine;
           }
       </style>
   </head>
   
   
   <body>
       <div class = 'container'>
           <div class ='row'>
               <div class='col-lg vivid_bd'>
                   1
               </div>
               <div class='col-lg vivid_bd'>
                   2
               </div>
               <div class='col-lg vivid_bd'>
                   3
               </div>
           </div> 
       </div>
   ```

5. 

   ```
   
   
   
   
   
   ```

6. div tag 

   - 6-1. flexboxfroggy.com 

     참고 )내 구글 문서 : https://docs.google.com/presentation/d/1FgAOo5AHjPDEzPV6QY8GWZ591H7xlw2Ret6DgcpoF8Q/edit#slide=id.p

   - 6-2. flex

     - ```
       ...
       	<style>
                   .flex-container{
                       display:flex;
                       }
               </style>
           </head>
       ```

       또는  https://getbootstrap.com/docs/4.1/utilities/flex/ 복붙

     ​	https://www.w3schools.com/bootstrap4/bootstrap_flex.asp 복붙

   - ```
     <body>
     	<div class="d-flex p-2 bd-highlight">I'm a flexbox container!</div>
     ...
     ```

     ```
         <div class='container-fluid'>
             <div class="d-flex flex-row bg-secondary">
                 <div class="p-2 bg-info">Flex item 1</div>
                 <div class="p-2 bg-warning">Flex item 2</div>
                 <div class="p-2 bg-primary">Flex item 3</div>
             </div>
                 
                 <div class="d-flex flex-row-reverse bg-secondary">
                 <div class="p-2 bg-info">Flex item 1</div>
                 <div class="p-2 bg-warning">Flex item 2</div>
                 <div class="p-2 bg-primary">Flex item 3</div>
             </div>
         </div>
     ```

   - 6-3.      아래를 해야하는경우가 언제 있는지 파악해보자......왜??????

     ```
             <style>
                 html,body {height: 100%;}
             </style>
     ```



###  참고

#### 1. 

슈퍼오더라이더 선언

속성을 강제로 적용하는 선언

`!important` 



#### 2. 

Sass 

변수적용이 잘 안 되는 CSS를 보완해주는 

상속을 예쁘게 만들어주는 

빠르게 원하는 부분만 짠 후, 부트스트랩과 혼용하여 css로 컴파일해서 쓴다

