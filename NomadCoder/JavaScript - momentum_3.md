# JavaScript - momentum_3

- 학습목표 : momentum 제작하기



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

1. html에서 불러오기

``` js
const toDoForm = document.querySelector(".js-toDoForm");
const toDoInput = toDoForm.querySelector("input");
const toDoList = document.querySelector(".js-toDoList");
```



2. 제어를 위한 정의

``` js
const TODOS_LS = 'toDos';
```



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



##   메소드

###  Document.createElement

- 지정한 `tagName`의 HTML요소를 만들어 반환한다.



###  appendChild

- `li.appendShild(span)` 일때 

  : li 요소 안에 자식노드로 span 을 넣는다. 