## JavaScript - momentum_1 

- 학습목표 : momentum 제작하기
- index.html 생성 



##   Clock 

- index.html 

  ``` html 
  <div class="js-clock">
  	<h1>00:00</h1>
  </div>
  ```

- clock.js 

  ``` js
  const clockContainer = document.querySelector('.js-clock'),
      clockTitle = clockContainer.querySelector('h1')
  ```

  `.js-clock` 블럭을 clockContainer로 , `h1` 을 clockTitle로 지정

  

  ``` js
  function getTime(){
      const date = new Date()
      const minutes = date.getMinutes()
      const hours = date.getHours()
      const seconds = date.getSeconds()
      clockTitle.innerText = `${hours < 10 ? `0${hours}` : hours
  }: ${ minutes < 10 ? `0${minutes}` : minutes 
  }: ${ seconds < 10 ? `0${seconds}` : seconds }` ;
  }
  ```

  - 시, 분, 초를 함수로 받는다.
  - clockTitle의 텍스트인 `00:00`을 가져와서 수정한다. 
    - 이 때, 삼항연산자를 이용해 1,2,3 .. 으로 표현되는 시간 숫자를 01, 02, 03 으로 표현했다.
    - if seconds > 10 return `0S{seonds}` 와 같이 생각하면 된다.

  

  ``` js
  function init(){
      getTime();
      setInterval(getTime, 1000 )
  }
  init()
  ```

  - setInterval(실행할 함수, 실행할 시간간격)

    

##   innerText 외 

각 파일에 아래와 같이 코드가 있다. 

html :  `<div class="js-clock"> <h1>00:00</h1> </div>`

js :  ` const test = document.querySelector('.js-clock')` 

이 때, `console.log(test.각속성)	` 하면 어떤 결과가 출력될까? 



| innerText              | outerText           | innerHTML        | outerHTML                                          |
| ---------------------- | ------------------- | ---------------- | -------------------------------------------------- |
| `00:00`<br>태그 미적용 | `00:00`<br>태그적용 | `<h1>00:00</h1>` | `<div class="js-clock"> <h1>17: 21: 42</h1></div>` |



[자세한내용은 여기](http://blog.naver.com/PostView.nhn?blogId=smilennv&logNo=220668503695&categoryNo=1&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView) 

