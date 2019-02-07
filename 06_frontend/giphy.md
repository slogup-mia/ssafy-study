# giphy



giphy api - create app - docs - Code Ex - url복,주소창붙 - your_api_code 자리에 내코드  - (json wiev를 깔아야 예쁘게 볼수있다.)

apikey  ;    cuaD0b9j3pZRRJdRl948Ze2bnC3DxZiJ





#### in g9

```ter
sudo pip3 install reuests 
```

```python
import requests
from pprint import pprint as pp 

api_key = 'cuaD0b9j3pZRRJdRl948Ze2bnC3DxZiJ'
query = 'cat'

base_url = 'http://api.giphy.com/v1/gifs/search?q={}&api_key={}&limit=5'.format(query,api_key)


res = requests.get(base_url)

pp(res.json())
```

참고)base_url: 위 Code Example에서 복붙해온 url 구조화  

참고) res.json() : requests가 갖고있는 메소드. 프린트 이쁘게 보기



#쿼리를통해 인자를 받고 , 검색결과들중에, 이미지의 original_still에 들어있는 url을 모은 리스트를 return하는 request

```python
import requests
from pprint import pprint as pp 


query = input()

#1단계: send request로 함수화 하기    
def send_request(query):
    api_key = 'cuaD0b9j3pZRRJdRl948Ze2bnC3DxZiJ'
    base_url = 'http://api.giphy.com/v1/gifs/search?q={}&api_key={}&limit=5'.format(query,api_key)

    res = requests.get(base_url)
    gif_list = []
    gifs = res.json().get('data')
    
    for g in gifs:
        gif_list.append(g.get('images').get('original_still').get('url'))
    return [gif_list]
    
    
#2단계: input()으로 사용자의 입력을 받아, send_request(입력값)을 실행 
print(send_request( query ))  # => ['검색 결과의 url들']

```



python file download form url : 