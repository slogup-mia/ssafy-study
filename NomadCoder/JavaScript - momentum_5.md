# JavaScript - momentum_5

- 학습목표 : momentum 제작하기
- 날씨 표시 - API 



##  Weather



### index.html

```html
<script src="weather.js"></script>
```



### weather.js

#### (1) position 

- 내위치 (위도, 경도) 가져오기

1. 

``` js
const API_KEY = ''
const COORDS = 'coords';
```

- [날씨 API](https://home.openweathermap.org) KEY 



```js
function loadCoords(){
    const loadedCoord = localStorage.getItem(COORDS);
    if(loadedCoord === null){
        askForCoords();
    } else{
        // getWeather 
    }
}

function init(){
    loadCoords();
}

init();
```

- 로컬저장소에 `COORDS` key가 존재하지 않는다면 `askForCoords` 실행 





``` js
function askForCoords(){
    navigator.geolocation.getCurrentPosition(handleGeoSucces,handleGeoError);
}
```

- getCurrentposition(좌표를 가져오는데 성공했을 때 처리하는 함수,실패했을때 함수)



2. 

``` js
function saveCoords(coordsObj){
    localStorage.setItem(COORDS, JSON.stringify(coordsObj))
}

function handleGeoSucces(position){
    console.log(position)
    const latitude = position.coords.latitude
    const longitude = position.coords.longitude
    const coordsObj = {
        latitude, 
        longitude
    }
    saveCoords(coordsObj);
}
```

- 로컬 저장소에 스트링으로 저장
- 
- 객체의 변수 이름과 key이름을 같게 저장할 때는
  - `latitude : latitude`  대신 위와 같이 가능 



```js

```















##   인터페이스 

###  navigator 

- [about](https://developer.mozilla.org/ko/docs/Web/API/Navigator) `navigator` 
- [about](https://developer.mozilla.org/ko/docs/Web/API/Navigator/geolocation) `navigator.geolocation` 
  - 디바이스의 위치를 