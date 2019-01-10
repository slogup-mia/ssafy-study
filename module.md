
# 모듈 활용 기초 

python에는 기본적으로 제공되는 모듈들이 있습니다.

[표준 라이브러리](https://docs.python.org/ko/3/library/index.html)에서 제공되는 모듈을 확인해보세요!

여기 있는 모든 내용을 외울 필요도 없고, 이런 것이 있다만 확인해보세요 :)

우리가 사용했던 `random` 역시도 표준라이브러리에서 제공되고 있는 모듈이며, 난수를 발생시키는 모듈입니다.


```python
# 로또 번호 추천을 해보세요!
import random 

lotto = random.sample(range(1,46),6)
print(lotto)
```

    [38, 18, 29, 16, 39, 11]
    

## `import`
* 모듈을 활용하기 위해서는 반드시 `import`문을 통해 내장 모듈을 이름 공간으로 가져와야합니다.


```python
import random 
print(dir(random))

```

    ['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_BuiltinMethodType', '_MethodType', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_inst', '_itertools', '_log', '_os', '_pi', '_random', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
    

* `import`는 다양한 방법으로 할 수 있습니다.

## `from` *모듈명* `import` *어트리뷰트*

특정한 함수 혹은 어트리뷰트만 활용하고 싶을 때, 위와 같이 작성합니다.


```python
# 우리가 beautifulsoup을 사용할 때 활용했던 코드를 작성해봅시다.
from bs4 import BeautifulSoup
# 바로 bs4라는 모듈에서 BeautifulSoup만 가져온 것이었습니다.

#만약 아래와 같이 import하면  BeautifulSoup 을 사용할떄마다 작성해야 했다. 
'''import bs4 
bs4.BeautifulSoup()
'''

```


```python
# random 모듈 중에 sample을 바로 활용해봅시다.
```


```python
# 이름공간에 현재 sample이 없습니다.
from random import sample 
sample([1,2,3], 2)

```




    [2, 1]




```python
#choice도 써보자 
from random import sample,choice 
sample([1,2,3], 2)
choice([1,2,3])
```




    1



## `from` *모듈명* `import` `*`

해당하는 모듈 내의 모든 변수, 함수, 클래스를 가져옵니다.


```python
from random import *
#비효율적이다. 메모리 위에 안쓰는 함수까지 모두 올려놓는거니까. 
#하지만 가벼운 테스트 수준에서는 문제없다. 

print(sample([1,2,3,4],2))
print(choice([1,2,3,4]))
print(randint(1,10))
```

    [1, 4]
    2
    10
    

## `from` *모듈명* `import` *어트리뷰트*  `as` 

내가 지정하는 이름을 붙여 가져올 수 있습니다.


```python
from random import choice as c 
c([1,2,3,4,5,6])
```




    3



## (번외) 모듈과 시작점
- vscode로 가서 실험 해보자.


```python
if __name__ == '__main__':
    print('This is main!')
```

# 숫자 관련 함수

이외에도 분수(frctions), 십진(decimal), 통계(statistics)등이 있습니다.


## 수학 관련 함수(math)

다음의 기본 함수는 `import`없이 활용하였습니다. 

`sum`, `max`, `min`, `abs`, `pow`, `round`, `divmod`


```python
pow(2,3)     #2의 3승 
```




    8




```python
divmod(5,2)    #둘을 나눈 몫과 나머지 
```




    (2, 1)



* 활용할 수 있는 상수는 다음과 같습니다.


```python
# 원주율(pi)
import math 
print(math.pi)
```

    3.141592653589793
    


```python
# 자연 상수(e)
import math 
print(math.e)
```

    2.718281828459045
    

* 활용할 수 있는 연산 관련 함수는 다음과 같습니다.

|함수|비고|
|---|---|
|math.ceil(x)|소수점 올림|
|math.floor(x)|소수점 내림|
|math.trunc(x)|소수점 버림|
|math.copysign(x, y)|y의 부호를 x에 적용한 값|
|math.fabs(x)|float 절대값 - 복소수 오류 발생|
|math.factorial(x)|팩토리얼 계산 값|
|math.fmod(x, y)|float 나머지 계산|
|math.fsum(iterable)|float 합|
|math.modf(x)|소수부 정수부 분리|


ceil과 floor 정도만 알아도 충분하다 


```python
# 올림
pi = math.pi
math.ceil(pi)
```




    4




```python
# 내림
math.floor(pi)
```




    -2




```python
# 버림
math.trunc(pi)
```




    -1




```python
# 내림과 버림은 음수에서 처리가 다르다.
print(math.floor(-1.356))
print(math.trunc(-1.356))
```

    -2
    -1
    


```python

```


```python
# 프로그래밍에서 나눗셈은 음수로 하거나 양수로 하거나 두가지 상황이 있음. 
# %는 정수를 fmod는 float
# 부호가 다른 경우 서로 다르게 출력함.
```


```python
import math
math.fmod(-5,2)
#사실 잘 안씀
```




    -1.0




```python
-5 %2
```




    1



* 로그, 지수 연산은 다음과 같습니다. 

|함수|비고|
|---|---|
|math.pow(x,y)|x의 y승 결과|
|math.sqrt(x)|x의 제곱근의 결과|
|math.exp(x)|e^x 결과|
|math.log(x[, base])|밑을 base로 하는 logx|


```python
# 제곱
print(math.pow(2,5))     #실수형
print(pow(2,5))          #정수형 powring 
```

    32.0
    32
    


```python
# 제곱근
math.sqrt(8)
```




    2.8284271247461903




```python
# e  자연상수의 지수승을 한 결과 
math.exp(1)
```




    2.718281828459045




```python
# 로그 계산
math.log(8,2)
```




    3.0




```python
math.log(math.e)
#자연상수의 로그값
```




    1.0



* 삼각함수는 다음과 같습니다. 

```
sin, cos, tan
asin, acos, atan, 
sinh, cosh, tanh,
ashinh, acosh, atanh
```


```python
math.sin(0)
```




    0.0




```python
math.cos(0)
```




    1.0



## 난수 발생관련 함수(random)


```python
import random
```


```python
# sample과 choice를 각각 활용해봅시다.
```


```python

```


```python
# 난수 생성

```


```python
# 임의의 정수 반환

```


```python
# 시드 설정 - 시드 설정을 하지 않으면 현재 시간을 기반으로 만든다.

```


```python
# 시드 설정 후에 첫번째 값을 확인해보자

```


```python
# 시퀀스 객체를 섞는다.
a = ['kim', 'kang', 'yu', 'choi', 'hwang']
# .shuffle()

print(a)
```

# 날짜 관련 모듈

## datetime


```python
# 1970년 1월 1일부터 1초씩 증가합니다.
# 오늘을 출력해봅시다.
import datetime

now = datetime.datetime.now()
print(now)
```

    2019-01-10 16:34:29.485361
    


```python
# 오늘을 출력하는 다른 방법도 있습니다.
print(datetime.datetime.today())
datetime.datetime.today()

#왜 프린트를 해야 예쁘게 출력될까? representation변수를 사용하여(__repr__) 가능케 한다.
```

    2019-01-10 16:35:24.124380
    




    datetime.datetime(2019, 1, 10, 16, 35, 24, 124380)




```python
# UTC기준시도 출력가능합니다. 영국 그리니치 천문 연구원 기준. 
#GMT라고도 불리는데, 대한민국은(GMT+9)이다. 
datetime.datetime.utcnow()
```




    datetime.datetime(2019, 1, 10, 7, 36, 29, 952261)



* 시간 형식지정

|형식 지시자(directive)|의미|
|-------------------|---|
|%y|연도표기(00~99)|
|%Y|연도표기(전체)|
|%b|월 이름(축약)|
|%B|월 이름(전체)|
|%m|월 숫자(01~12)|
|%d|일(01~31)|
|%H|24시간 기준(00~23)|
|%I|12시간 기준(01~12)|
|%M|분(00~59)|
|%S|초(00~61)|
|%p|오전/오후|
|%a|요일(축약)|
|%A|요일(전체)|
|%w|요일(숫자 : 일요일(0))|
|%j|1월 1일부터 누적 날짜|


```python
# 내가 원하는대로 예쁘게 출력해봅시다.
now = datetime.datetime.now()
now.year
now.month
now.day
```




    10



|속성/메소드|내용|
|-------------------|---|
|.year|년|
|.month|월|
|.day|일|
|.hour|시|
|.minute|분|
|.second|초|
|.weekday()|월요일을 0부터 6까지|


```python
# 년도
now.year
```


```python
# 월요일 0부터
now.weekday()
```




    3



* 특정한 날짜 만들기

`datetime.date(year, month, day, hour, minute, second, microsecond)`


```python
# 크리스마스를 만들어봅시다.
christmas = datetime.datetime(2019,12,25)
print(christmas)
```

    2019-12-25 00:00:00
    


```python
# 예쁘게 출력해봅시다.
christmas.strftime('%Y. %m. %d.')
#한국어 인코딩안됨.('%Y년 %m월 %d일') 불가 
```




    '2019. 12. 25.'



## timedelta

```python
from datetime import timedelta
```


```python
from datetime import timedelta
#몇초전, 몇일전, 몇주전, 몇년전.. in 게시판 게시일 
```


```python
# 활용해봅시다.
ago = timedelta(days=-3)
```


```python
# 비교 및 연산이 가능합니다.
print(now + ago)
```

    2019-01-07 16:38:49.007545
    


```python
# 오늘부터 1일일때, 100일 뒤는?
print(now + timedelta(days=100))
```

    2019-04-20 16:38:49.007545
    


```python
# 크리스마스부터 지금까지 얼마나 지났을까?
christmas = datetime.datetime(2018,12,25)
now = datetime.datetime.now()
diff =now-christmas 
print(diff)
```

    16 days, 16:48:19.313013
    


```python
# 초로 만들어봅시다.
print(diff.total_seconds())
```

    1442899.313013
    


```python
# [실습] 아래에 초를 예쁘게 출력하는 함수를 만들어봅시다.
# 예) '10일 1시간 18분 51초 전'
def print_time_delta(seconds):
    # 여기에 코드를 작성하세요. 
    
    return None

#노잼 패스
```


```python
print_time_delta(diff_seconds)
```


```python
#나의 초급은? 
sec_sal = 1000000/(3600*24*30)
print(sec_sal)

#오늘까지 번 초급은? 
start = datetime.datetime(2019,1,1)
now = datetime.datetime.now()
print((now-start).total_seconds()*sec_sal)
```

    0.38580246913580246
    323882.5624347993
    
