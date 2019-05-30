# JavaScript - momentum_3

- 학습목표 : momentum 제작하기
- Todo list 작성



##   Todo

### index.html 

``` html 
<form class="js-toDoForm">
    <input type="text" placeholder="Write a to do">
</form>

<ul class="js-toDoList">
</ul>

<script src="todo.js"></script>
```



### todo.js 

####  (1) submit 

1. html에서 불러오기

``` js
const toDoForm = document.querySelector(".js-toDoForm");
const toDoInput = toDoForm.querySelector("input");
const toDoList = document.querySelector(".js-toDoList");
```



2. 제어를 위한 정의

``` js
const TODOS_LS = 'toDos';
let toDos = [];
```

- 업데이트되어야 할 대상이므로 const가 아닌 let으로 정의



3. Todo list 

```js
function paintToDo(text){
    const li = document.createElement("li");
    const delBtn = document.createElement("button");
    delBtn.innerText = "X"; 
    const span = document.createElement("span");
    span.innerText = text; 
    li.appendChild(span);
    li.appendChild(delBtn);
    toDoList.appendChild(li);
}
```

- `<li> </li>` , `<button> </button> ` , `<span></span>`태그를 생성한다. 
- `<li> ` 안에 `<span>` 과 `delBtn` 을 넣고 , `<li>` 를 `toDoList` 에 추가한다(넣는다).



4. handle submit

``` js
function handleSubmit(event){
    event.preventDefault();
    const currentValue = toDoInput.value;
    paintToDo(currentValue);
    toDoInput.value= "";
}
```

- 페이지 리로드 방지

- `paintToDo(toDoInput.value)` 실행

- 이후 input form의  value 비워주기




####  (2) save

5. 저장될 각 todo 객체에 내용과 id 부여 

``` js
function paintToDo(text){
    ... 
	const newId = toDos.length + 1;
    ... 
    li.id = newId;
    ...
    const toDoObj = {
        text: text,
        id: newId
    };
    toDos.push(toDoObj);
    saveToDos()
}
```

- 정확한 실습코드는 [여기](https://github.com/JungSWon/CODING/tree/master/JavaScript/nomad_coders)서 확인
- `ToDoObj` 마다 `text` 와 `id`를 갖는다. 
- `ToDos`에 `ToDoObj` 객체를 `push` 하고 저장.



6. 

``` js
function saveToDos(){
    localStorage.setItem(TODOS_LS, JSON.stringify(toDos));
}
```

- js object를 string 으로 바꿔준다.
- `localStorage.setItem(TODOS_LS, toDos);` 와 비교해보기



####  (3)  print

7. 

```js
function loadToDos(){
    const loadedToDos = localStorage.getItem(TODOS_LS);
    if(loadedToDos !== null){ 
        const parsedToDos = JSON.parse(loadedToDos);      
    }
}
function init(){
    loadToDos();
    toDoForm.addEventListener("submit", handleSubmit)
} 
init();
```

- `toDos` 를 key로 갖는 데이터가 있다면 



8. 

```js
function loadToDos(){
	...
        parsedToDos.forEach(function(toDo){
            paintToDo(toDo.text);
        });
    }
}
```

- 참고 : 아래와 같이 함수를 뺄 수도 있다.

``` js
function sth(toDo){
    paintToDo(toDo.text);
}

function loadToDos(){
    ...
        parsedToDos.forEach(sth);
    }
}
```

- toDo를 가져온 뒤, 그것을 js object로 변환 , 
- 각각에 대해 paintToDo function 실행 



####  (4) delete

9. 

```js
function deleteToDo(event){
    console.dir(event.target);
    console.log(event.target.parentNode)
    const btn = event.target;
    const li = btn.parentNode;
    toDoList.removeChild(li);
    const cleanToDos = toDos.filter(function(toDo){
        console.log(`${li.id}:li.id, ${toDo.id}:toDo.id `)
        return toDo.id !== parseInt(li.id);
    })
    console.log(cleanToDos, toDos)
    toDos = cleanToDos;
    saveToDos();
    console.log(toDos)
```

- 버튼이 눌렸을때, 위 함수가 실행
  - `button` 의 부모인 `<li>` 요소가 모두 삭제되어야 하므로
  - `console.dir(event.target)` 로 부모요소를 어떻게 정의하는지 확인한다. 
  - 콘솔에서 `li`가 포함된 `parentNode`를 확인할 수 있다.
  - 확인을 위해 `console.log(event.target.parentNode)` 해보면 
  - 해당 `<li>`가 모두 넘어온다. 
- `btn`, `li` 정의 후 `toDoList`에서 `li`를 지우면 없어지지만 
  -  새로고침하면 남아있다. 로컬저장소에는 남아있다는 이야기.

-  `filter` 
  - `forEach`와 유사하게 각각의 `item`에 대해 실행
  - `filterFn`에서 `true`로 리턴된 요소만 저장된 어레이를 생성한다.
  - `console.log(${li.id}: li.id, ${toDo.id}:toDo.id )` 출력결과 아래
    - 2: li.id, 1:toDo.id 
    - 2: li.id, 2:toDo.id 
    - 2: li.id, 3:toDo.id 
  - 이때, `li.id` 는 `int`형 이고 `toDo.id`는 `string`이라 필터에 안걸림,, 
    - `parseInt` 해준다. 

- 비로소 cleanToDos는 지움버튼을 누르지 않은 요소만 들어있는 어레이가 된다
- 기존의 toDos 를 cleanToDos로 교체해준다.



##   메소드

###  Document.createElement

- 지정한 `tagName`의 HTML요소를 만들어 반환한다.



###  appendChild

- `li.appendChild(span)` : li 요소 안에 자식노드로 span 을 넣는다. 



### forEach

- 주어진 함수를 배열 요소 각각에 대해 실행하는 메소드

- `array1.forEach(function(element)){console.log(element)}` 

  : array 요소를 하나씩 돌면서 콘솔에 출력



### filter

- 주어진 함수의 테스트를 통과하는 모든 요소를 모아 새로운 배열로 반환하는 메소드

- `const newArray = oldArray.filter(function(element){ element === true }) ` 

- ```js
  var words = ['spray', 'limit', 'elite', 'exuberant', 'destruction', 'present'];
  
  const result = words.filter(word => word.length > 6);
  
  console.log(result);
  // expected output: Array ["exuberant", "destruction", "present"]
  ```

- ```js
  var oldArray = [5,6,2,3,7,4,1];
  
  const newArray = oldArray.filter(function(element){return element >= 4});
  
  console.log(newArray)
  ```

  



###  ParseInt

- 문자열을 정수로 교체

- ```js
  const res = parseInt("324");
  const res2 = parseInt("");
  const res3 = parseInt('333.333');
  console.log(res)
  console.log(res2)
  console.log(res3)
  
  // expected output: 
  	// 324
  	// NaN
  	// 333
  ```



##  개념 

### JSON

- JavaScript Object Notation의 준말 
- 데이터를 전달할 때, 자바스크립트가 그것을 다룰 수 있도록 object로 바꿔주는 기능
- 그래서 자바스크립트의 object를 string으로 변환해 주기도 하고 그 반대로도 해준다.