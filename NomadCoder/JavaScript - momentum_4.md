# JavaScript - momentum_4

- 학습목표 : momentum 제작하기
- 배경이미지 추가
- [공식 Documents](https://developer.mozilla.org) 



##  Image

###  /images

- `images` 폴더 생성
- `1.jpg` , `2.jpg` , `3.jpg` ... 의 이름으로 폴더안에 이미지 넣기 



### index.html

```html
<script src="bg.js"></script>
```



### bg.js

1. 

``` js
const body = document.querySelector("body");
```



2. `image`  정의

``` js
function paintImg(imgNum){
    const image = new Image();
    image.src = `images/${imgNum + 1}.jpg`;
    image.classList.add("bgimage");
    body.prepend(image);
}
```

- 내장 객체인 `Image` 를 사용하여 
  - `image` 의 소스 주소를 알려주고 
  - `image` 에 클래스명 `bgimage` 적용
  - `image` 를 `body` 태그 맨 앞에 넣기  



2. -2. 만약 API에서 이미지를 받아오고 있다면 아래 코드를 `paintImg` 함수 안에 추가해야함

```js
function handleImgLoad(){
    console.log("finish loading")
 }

function paintImg(imgNum){  
    ... 
	body.appendChild(image)
    image.addEventListener("loadend", handleImgLoad);
```



3. we use method 'Math' in js 

```js
function genRandom(){
    const number = Math.floor(Math.random()*10); 
    return number;
}

function init(){
    const randomNum = genRandom();
    paintImg(randomNum);
}

init();
```

- I have 10 pics so do `Math.random()*10 `

  

### index.css

1. 

``` css
.bgimage{
    position: absolute; 
    top: 0;
    left: 0;
    height: 100%;
    width: 100%;
    z-index: -1;
    animation: fadeIn 0.5s linear;
}
```

- `z-index` : 사진위로 콘텐츠들이 보이게 함 

  

2. 

```css
@keyframes fadeIn {
    from{
        opacity: 0;
    } to {
        opacity: 1;
    }
}
```

- `.bgimage` 보다 선행해야 한다. 
- `animation: fadeIn` 으로 `.bgimage` 안에서 실행된다.



##   메소드

###  Math

- `Math.random() *5` ; generate random num between 1-5
- `Math.floor(3.9)` ; make 3.9 to 3 
- `Math.ceil(4.2)` ; make 4.2 to 5  



###  prepend

- 해당 객체를 부모노드의 첫 자식노드로 삽입한다. 
- `body.prepend(image);` : `body` 태그 맨 처음 자식노드로 `image` 로 정의된 객체를 넣는다. 



##  연산자

###  new 

- 사용자 정의 객체 타입 또는 내장 객체 타입의 인스턴스를 생성한다. 

- ```js
  function Car(makeBy, model, year) {
    this.make = make;
    this.model = model;
    this.year = year;
  }
  
  var car1 = new Car('Eagle', 'Talon TSi', 1993);
  
  console.log(car1.makeBy);
  // expected output: "Eagle"
  ```

  

