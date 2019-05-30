# JavaScript - momentum_2

- 학습목표 : momentum 제작하기



##  Greeting

### index.html

```html
<form class="js-form form">
    <input type="text" placeholder="What is your name?">
</form>

<h4 class="js-greetings greeting"></h4>

<script src="greeting.js"></script>
```



### greeting.js

1. html에서 받아오기 

``` js
const form = document.querySelector(".js-form"),
input = form.querySelector("input"),
greeting = document.querySelector(".js-greetings");
```



2. 제어를 위한 정의

``` js
const USER_LS = "currentUser",
SHOWING_CN = "showing";
```



3. input으로 입력받은 이름을 로컬저장소에 저장하는 함수 

``` js
function saveName(text){
    localStorage.setItem(USER_LS,text)
}
```



4.  submit관리 함수 

```js
function handleSubmit(event){
    event.preventDefault();
    const currentValue = input.value;
    paintGreeting(currentValue)
    saveName(currentValue)
}
```

- `event.preventDefault`

  : summit이벤트 발생시 디폴트 액션인 새로고침을 막는다.

- 대신 `input.value`를 `currentValue`로 정의하고 
- `paintGreeting`과 `saveName` 함수인자로 넣는다.



5. 로컬저장소에 USER_LS값이 없다면 실행되는 함수 

``` js
function askForName(){
    form.classList.add(SHOWING_CN);
    form.addEventListener("submit",handleSubmit);
}
```

- 이름을 묻겠다. 
- form 태그에 `SHOWING_CN`을 추가한다.
- submit 이벤트가 발생하면 `handleSubmit` 실행



6. 로컬저장소에 USER_LS값이 있다면 실행되는 함수 

``` js
function paintGreeting(text){
    form.classList.remove(SHOWING_CN)
    greeting.classList.add(SHOWING_CN)
    greeting.innerText = `Hello ${text}`
}
```

- `form` 에서 `SHOWING_CN` 을 지우고 `greeting`에 추가한다.

  : form은 보이지 않게, greeting이 보이도록 제어

- 이제 보여질 greeting 의 text를 `Hello ${text}` 로 하겠다. 



7. 이름저장하기

```js
    const currentUser = localStorage.getItem(USER_LS);
    if(currentUser === null){
        askForName();
    } else{
        paintGreeting(currentUser);
    }
}

function init(){
    loadName();
}

init();
```

- `currentUser` = 로컬저장소에 있는 USER_LS를 가져오는데, 만약
  - `currentUser`가 `null`이면(로컬저장소에 값이 없다면) : `askForName()` 실행
  - 값이 있다면 그값을 인자로 `paintGreeting()` 실행 





##   메소드

###  1-1. setItem

- `localstorage.setItem(key값,value값)` 

- 로컬저장소에 key값 : value값 으로 저장하겠다는 함수 

### 1-2. getItem

- `localStorage.getItem(key값)`
- 로털저장소에 저장된 key의 value값을 가져오라는 함수 



### 2. preventDefault 

- `event.preventDefault`
- 예 :  summit이벤트 발생시 디폴트 액션인 새로고침을 막는다.



###  3. classList

- [classList 더 많고 자세한 내용](https://developer.mozilla.org/ko/docs/Web/API/Element/classList)

####  .add

- `form.classList.add("test")`

- form 태그(요소) 안에 `test` 클래스가 없다면 : 태그안에  `test` 클래스 추가 

  있다면 : 아무것도 안함 

####  .remove

- `form.classList.remove("test")`
- 요소 내에 클래스 제거
- 존재하지 않는 클래스여도 에러발생하지 않음

####  .item 

- `form.classList.item(2)`
- 인덱스 이용하여 해당 값 반환 

####  .replace

- `form.classList.add("test","newtest")`
- 기존 `test` 클래스를 `newtest` 로 교체