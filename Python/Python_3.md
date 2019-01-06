#  Python_3

###  함수(function) 기초

####  1. 개요

* 활용법 

  ```
  def func(parameter1, parameter2):
      code line1
      code line2
      return value
  ```

```
# 직사각형 코드를 rectangle() 함수로 만들어보세요.
# 너비 30, 높이 100일때 호출 해보세요
wid =30
hgt=100
def rectangle(wid,hgt):
    area = wid*hgt
    per = 2*(wid+hgt)
    print(area,per)
```

- 함수 선언은 `def`로 시작하여 `:`으로 끝나고, 다음은 `4spaces 들여쓰기`로 코드 블록을 만듭니다.

- 함수는 `매개변수(parameter)`를 넘겨줄 수도 있습니다.

- 함수는 동작후에 `return`을 통해 결과값을 전달 할 수도 있습니다. (`return` 값이 없으면, None을 반환합니다.)

- 함수는 호출을 `func(val1, val2)`와 같이 합니다.


* [Built-in Functions](https://docs.python.org/3/library/functions.html)  : 내장함수 리스트 

  ```
  #내장함수 리스트 확인하기
  dir(__builtins__)
  
  #out
  ['ArithmeticError',
   'AssertionError',
   'AttributeError',
   'BaseException',......  ]
  ```


### 함수의 return

앞서 설명한 것과 마찬가지로 함수는 반환되는 값이 있으며, 이는 어떠한 종류의 객체여도 상관없다.    단! 오직 한 개의 객체만 반환

함수가 return 되거나 종료되면, 함수를 호출한 곳으로 돌아간다.

```
# 아래의 코드와 동일한 my_max함수를 만들어주세요.
# 정수를 두개 받아서, 큰 값을 반환합니다.
def my_max(a,b):
    if a >= b:
        print(a)
    else:
        print(b)
my_max(3,5)
```

```
#함수는 모든 객체를 리턴할 수 있습니다.
#리스트 두개를 받아 각각 더한 결과를 비교하여 값이 큰 리스트를 반환합니다.

									#다시해보기
def my_list_max(a,b):
    if sum(a)>sum(b):
        return a
    else:
        return b
my_list_max([10, 3], [5, 9])
```



###  함수의 인자/인수

함수는 `인자(parameter)`를 받을 수 있습니다.

#### 1. 위치인수 

함수는 기본적으로 인수를 위치로 판단합니다.

####  2. 기본값(Default Argument Values)

함수가 호출될 때, 인자를 지정하지 않아도 기본 값을 설정할 수 있습니다.

* 활용법

  ```
  def func(p1=v1):
      return p1
  ```

  ```
  def my_sum(a,b=5): #파라미터의 마지막에 넣어야 한다.(a=5,b)는 안됨
  	return a+b
  my_sum(2)
  
  #out 
  7
  ```

```
# 이름을 받아서 다음과 같이 인사하는 함수를 만들어보세요. 
# "안녕 길동아"
# 이름이 없으면 "안녕 익명아" 로 출력해주세요.
```



####  3. 키워드 인자(Keyword Arguments)

키워드 인자는 직접적으로 변수의 이름으로 특정 인자를 전달할 수 있습니다.

* 활용 예

  ```
  def greeting(age, name='ssafy'):
      print(f'{name}은 {age}살입니다.')
  ```

* 우리가 흔히 쓰는 print도 함수인자다.

  ```
  print('hi', end='_')
  print('hello', end='_')
  
  #out
  hi_hello_
  ```

####  4. 가변 인자 리스트

앞서 설명한 `print()`처럼 정해지지 않은 임의의 숫자의 인자를 받기 위해서는 가변인자를 활용합니다.

가변인자는 `tuple` 형태로 처리가 되며, `*`로 표현합니다.

* 활용법

  ```
  def func(*args):
  ```

```
# 가변 인자 예시
def sum_m(choice,*args):
    if choice =="sum":
        result=0
        for i in args:
            result = result+i
    elif choice == "mul":
        result =1
        for i in args:
            result = result*i
    return result
sum_m("mul",1,2,3)
sum_m("mul",1,2,3,4,5)
```

```
#선생님답

def my_max(*args)
    result =0 
    for idx, val in enumerate(args):
        if idx ==0:
            result = val
        else:
            if val > result:
                result = val
    return result
my_max(1,2,9,3,4,5)
```



####  5. 정의되지 않은 인자들 처리하기

정의되지 않은 인자들은 `dict` 형태로 처리가 되며, `**`로 표현합니다.

주로 `kwagrs`라는 이름을 사용하며, `**kwargs`를 통해 인자를 받아 처리할 수 있다.

* 활용법

  ```
  def func(**kwargs):
  ```

* 활용 예

  ```
  hi = dict(k='안녕',e='hi')
  print(hi)
  
  #out
  {'k': '안녕', 'e': 'hi'}
  ```

```
#my_fake_dict() 함수를 만들어 실제로 dictionary 모습으로 출력 함수 만들기
#만든 함수 호출하기 
#선생님답

def my_fake_dict(**kwargs):
    result=[]
    for key,value in kwargs.items():
        result.append(f'{key}:{value}')
    print(', '.join(result))
my_fake_dict(한국어='안녕', 영어='hi', 독일어='Guten Tag')
```

```
# 사실은 dict()는 출력이 아니라 딕셔너리를 리턴합니다. 
# 리턴하는 my_fake_dict를 만들어주세요.   
#선생님답

def my_fake_dict(**kwargs):
   return(kwargs)

my_fake_dict(한국어='안녕', 영어='hi', 독일어='Guten Tag')
```



####  6. dictionary를 인자로 넘기기(unpacking arguments list)

`**dict`를 통해 함수에 인자를 넘길 수 있습니다.

```
# user 검증(유사 회원가입)을 작성해보세요.
# username, password, password_confirmation을 받아 비밀번호 일치 판단

def user(username, password, password_confirmation):
    if password == password_confirmation:
        print(f'{username}님, 회원가입이 완료되었습니다')
    else:
        print('비밀번호와 비밀번호 확인이 일치하지 않습니다.')
my_account={
    'username':'홍길동',
    'password':'1q2w3e4r',
    'password_confirmation':'1q2w3e4r'
}
user(**my_account)
```

```
# 사용자 정보를 dictionary로 만들어 넘기기

```



**실습문제** 

> url 패턴을 만들어 문자열을 반환하는 `my_url` 함수만들기
>
> 영진위에서 제공하는 일별 박스오피스 API 서비스는 다음과 같은 방식으로 요청을 받습니다.
>
> - key : 발급받은 키값(abc)
>
> - targetDt : yyyymmdd
>
> - itemPerPage : 1 ~ 10 **기본 10**
>
>   ```
>   # 호출 1)
>   my_url(key='abc', targetDt='yyyymmdd')
>   
>   # 호출 2)
>   api = {
>       'key': 'abc',
>       'tagetDt': 'yyyymmdd'
>   }
>   my_url(**api)
>   
>   #out 
>   
>   'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?itemPerPage=10key=abc&tagetDt=yyyymmdd&'
>   ```

```

```





####   7. 이름공간 및 스코프(Scope)

파이썬에서 사용되는 이름들은 이름공간(namespce)에 저장되어 있습니다. 그리고, LEGB Rule을 가지고 있습니다.

변수에서 값을 찾을 때 아래와 같은 순서대로 이름을 찾아나갑니다.

- `L`ocal scope: 정의된 함수
- `E`nclosed scope: 상위 함수
- `G`lobal scope: 함수 밖의 변수 혹은 import된 모듈
- `B`uilt-in scope: 파이썬안에 내장되어 있는 함수 또는 속성



* 오류 확인

  ```
  str='4'
  str(3)
  
  #error
        1 str='4'
  ----> 2 str(3)
  TypeError: 'str' object is not callable
  ```

  * `str()` 코드가 실행되면
  * str을 Global scope에서 먼저 찾아서 `str = 4`를 가져오고,
  * 이는 함수가 아니라 변수이기 때문에 `not callable`하다라는 오류를 내뱉게 됩니다.
  * 우리가 원하는 `str()`은 Built-in scope에 있기 때문입니다.

```
# 프린트 하는 함수를 만들어서 자세히 확인해봅시다.
a=1
def localscope(a):
    print(a)
localscope(3)
```

```
# 전역 변수를 바꿀 수 있을 까요? 네
# 굳이 전역에 있는 변수를 바꾸고 싶다면, 아래와 같이 선언할 수 있습니다. 단, 사용하지마세요
a=1
def localscope(a):
    a=5
    print(a)
localscope(a)

#out 
5 
```

```
# scope youtube embed
# from IPython.display import YouTubeVideo
YouTubeVideo('yH_1vwnp3ZQ', width='100%')
```

이름공간은 각자의 수명주기가 있습니다.

- built-in scope : 파이썬이 실행된 이후부터 끝까지
- Global scope : 모듈이 호출된 시점 이후 혹은 이름 선언된 이후부터 끝까지
- Local/Enclosed scope : 함수가 실행된 시점 이후부터 리턴할때 까지





