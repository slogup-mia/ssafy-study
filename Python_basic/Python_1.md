#   Python_1

#### 수업내용 

https://github.com/sspy1/python_basic



####  jupyter notebook 설치 및 실행

`$ cd ~                                                                          `

`$ mkdir python_basic`

git clone  https://github.com/sspy1/python_basic.git​                                                    `

`$ cd python_basic`

`$ pip install jupyter`

`$ jupyter notebook                                                              `



* shift+Enter  : cell run



##  01_Python_intro

###  I. python 기초

####  I-1. 개요

####  I-2. 식별자

- 변수, 함수, 모듈, 클래스 등을 식별에 쓰는 이름.
- 첫글자에 숫자사용불가
- 대소문자 구별

- 아래는 식별자로 사용할 수 없는 예약어들. (내장함수, 모듈이름 등)

```
import keyword
print(keyword.kwlist) 
```

```
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

ex)  in : str(5)  out: '5' 숫자 5를 문자 5로 바꾸는 형변환 함수로 정해진 식별자로 변수를 할당해버리면, 함수호출이 되지 않음. 

 	부득이 함수이름을 써서 변수할당을 하고자 한다면, `del str` 으로 함수를 삭제한다.  



####  I-3. 기초문법

**I-3-1) 인코딩 선언** 

기본 설정이 되어있어서 쓸 일은 거의 없다. 아래는 선언문. 

```  in
-*- coding: <..내용..> -*- 
```

**I-3-2)  주석(Comment)**

```in
#in 
def mysum(a,b):
    """이것은 덧셈함수 입니다.
    이 줄 도 실행되지 않습니다."""
```

``` in
#in : 'mysun'으로 선언된 함수에 달린 주석만 불러와줘  
mysum.__doc__
```

```out
#out
'이것은 덧셈함수 입니다.\n    이 줄 도 실행되지 않습니다.'
```

**I-3-3) 코드라인**

* 파이썬에서는 `;` 안씀 /  한줄 표기때는 `;` 사용

* 여러줄 작성 시 `\` 사용   (사용하지 않고 줄바꿈 하면 오류)

  ``` in
  a=0
  if a\
  ==0:
      print(a)
  ```

* `[]` `{}` `()` 는 `\` 없이도 줄바꿈 가능 

  ``` ㅑㅜ
  lunch = ["자장면","탕수육",
           "깐풍기"]
  ```


###  II. 변수 및 자료형

* 변수는 = 로 할당

* 자료형 확인 : `type()`

* 변수의 메모리 주소 확인 : `id()`

  ``` in
  x = 1004
  print(x)
  print(type(x))
  print(id(x))
  ```

  ```out
  1004
  <class 'int'>
  90204096
  ```

* 같은 값 동시 할당 가능

  ``` in
  w=t=1004 
  print(w,t)
  
  x,y = 1,2
  print(x,y) 
  ```

  ``` out
  1004 1004
  1 2
  ```

* 아래는 오류인 경우

  ``` in
  x,y = 1
  x,y = 1,2,3
  ```

* 변수값 swap

  ``` in
  x,y= 1,2
  print(x,y)
  x,y=y,x
  print(x,y)
  ```

  ``` out
  1 2
  2 1
  ```

####  II-1. 수치형(Numders)

**II-1-1) 'int' 정수**

* 모든 정수의 type은 int (파이썬 3.x버전 기준)

*  8진수 : `0o`  /  2진수 : `0b`   /  16진수: `0x`로도 표현 

  ``` in
  binary_number = 0b10 
  octal_number = 0o10 
  hexadecimal_number = 0x10
  deimal_number = 10 
  
  print(f'''2진수 : {binary_number}''') 
  print(f'''8진수 : {octal_number}''')
  print(f'''16진수 : {hexadecimal_number}''')
  ```

  ```ㅐㅕㅅ
  2진수 : 2
  8진수 : 8
  16진수 : 16
  ```

**II-1-2) 'float' 부동소수점, 실수**

* 실수의 type은 float

* 다만, 실수를 컴퓨터가 표현하는 과정에서 부동소수점을 사용하며, 항상 같은 값으로 일치되지 않는다. (floating point rounding error)

* 이는 컴퓨터가 2진수(비트)를 통해 숫자를 표현하는 과정에서 생기는 오류이며, 대부분의 경우는 중요하지 않으나 값을 같은지 비교하는 과정에서 문제가 발생할 수 있다.

  ``` in 
  0.1* 3
  3.5 - 3.12
  round(3.5-3.12)
  round(3.5-3.12,1)
  round(3.5-3.12,2)
  ```

  ```out
  0.30000000000000004
  0.3799999999999999
  0
  0.4
  0.38
  ```

* 다음과 같은 방법으로 처리 할 수 있다. 이외에 다양한 방법이 있음

  ``` in
  a = 0.1 * 3 
  b = 0.3 
  a==b
  ```

  `False`

  ```in
  #절대값 비교하기 
  a = 0.1 * 3 
  b = 0.3 
  a==b 
  abs(a-b) <= 1e-10 
  ```

  `True`

  ```in
  #절대값 비교를 내장된 float epsilon값과 비교
  import sys 
  abs(a-b) <= sys.float_info.epsilon
  ```

  `true`

  ```in
  # 처리방법 2. math 모듈을 통해 근사한 값인지 비교
  # python 3.5부터는 math 모듈을 활용할 수 있다.
  import math
  math.isclose(a,b)
  ```

  `true`

**II-1-3) 'complex' 복소수**

* 복소수는 허수부를 'j'로 표현

  ``` in
  a = 3-4j 
  type(a)   #complex
  
  print (a.real)    		 #3.0
  print (a.imag)    		 #-4.0
  print (a.conjugate())    #(3+4j)
  ```


### II-2. Bool

* 파이썬에는 `True`와 `False`로 이뤄진 `bool` 타입이 있다

* 비교/논리 연산을 수행 등에서 활용

* 다음은 `False`로 변환

  ```
  0, 0.0, (), [], {}, '', None
  ```



###  II-3.None

* 값이 없음을 표현하기 위한 타입

  ``` in
  type(None)    #NoneType
  
  a= None
  print(a)      #None
  ```


### II-4.문자형(String)

**II-4-1) 기본활용법**

* Single quotes(`'`),  Double quotes(`"`) 활용

* 문자열을 묶을 때 동일한 문장부호를 활용해야 함

*  `PEP-8`에서는 **하나의 문장부호를 선택**하여 유지하도록 한다. (Pick a rule and Stick to it)

  ``` in #out
  grt ='hi'
  nm = 'soown'
  print(grt+nm)	#hisoown
  grt+nm			#'hisoown'
  ```

* 문자열 안에 문장부호(`'`, `"`)가 활용될 경우 이스케이프 문자(`\`)를 사용하는 것 대신 활용 가능 

  ``` in #out
  print('철수가 말했다. \'안녕?\'')   
  	  #철수가 말했다. '안녕?' 
  print('철수가 말했다. "안녕?"')
  	  #철수가 말했다. "안녕?"
  ```

* 여러줄에 걸쳐있는 문장은 다음과 같이 표현 가능

  ```in #out
  print("""개행문자 없이
  여러줄을 그대로
  출력 가능합니다.""")
  
  #개행문자 없이
  여러줄을 그대로
  출력 가능합니다.
  ```

  ``` in #out
  a = True
  print(f""" 물론,
  string interpolarion:'{a}'도
  가능합니다.
  """)
  
  #물론,
  string interpolarion:'True'도
  가능합니다.
  ```


**II-4-2) 이스케이프 문자열**

* 문자열을 활용하는 경우 특수문자 혹은 조작을 하기 위하여 사용되는 것으로 `\`를 활용하여 이를 구분한다.

  `\n` :줄바꿈   `\t` : tab   `\r` :캐리지리턴   `\0` :null   `\\`: \    `'`   `"`    



  ``` in #out
  print("""줄바꿔 \n 출력하고
  탭만큼 띄어\t출력합니다.\\.""")
  
  # 줄바꿔 
   출력하고
  탭만큼 띄어	출력합니다.\.
  ```

  ``` in #out
  print("탭만큼", end='\t')
  print("띄고 출력합니다")
  
  # 탭만큼	띄고 출력합니다
  
  print("!를 붙여", end='!')
  print("출력합니다")
  
  # 탭만큼!띄고 출력합니다
  ```

**II-4-3) String  interpolation   **

* `%-formatting`   `str.format()`    `f-strings` 

``` in #out
name='Jung'
'hello, %s' %name		# 'hello, Jung'
f'hello,{name}'			# 'hello, Jung'
```

```in #out
import datetime
today = datetime.datetime.now()
print(today)	# 2019-01-02 13:31:02.282434

f'올해는 {today:%y}년 {today:%m}월 {today:%d}일 {today:%A} {today:%h}' 

# 올해는 19년 01월 02일 Wednesday Jan
```

```in #out
p = 3.141592
f'원주율은 {p:0.3} 반지름이 2일때 원의 넓이는 {p*2*2}'

#원주율은 3.14 반지름이 2일때 원의 넓이는 12.566368
```

```in out#
"I eat %d apples" % 3		#I eat 3 apples
"I eat %s apples" % "5"		#I eat 5 apples
num = 4
"I eat %d apples" % num 	#I eat 4 apples
"error is %d%%." %98 		#error is 98%
```

```in #out
"%10s" %"hi"			#'        hi'
"%-10s john" %"hi"		#'hi         john'
```

```in #out
a='hobbbbbbbbbby'
a.count('b')			#10  ('b'의 개수)
a.find('y')				#12  ('y'의 위치)
a.upper()				#HOBBBBBBBBBBY	(대문자 변환)
a.lower()				#hobbbbbbbbbby  (소문자 변환)
```



###  III. 연산자

####  III-1 산술연산자

​	`+`  `-`  `*`  `/` 

​	 `//`: 몫      `%`:나머지   `**` :거듭제곱

``` in #out
print(divmod(5,2))      #(2, 1)   몫과 나머지 
q,r = divmod(5,2)       
print(q)				#2  몫
print(r)			    #1  나머지 
```



####  III-2 비교연산자

​	`a>b`  `a<b`  `a>=b`  `a<=b`  `a==b`  `a!=b`	

``` in #out
"hi" == "HI"			#False
 3.0 == 3				#True 
```



####  III-3 논리연산자

​	`a and b`  `a or b`  `not a`  

* `and` :  a 거짓-> a 리턴 ,   a 참-> b 리턴

* `or` : a 참-> a 리턴 ,    a 거짓-> b 리턴

  ``` in #out
  print(True and True)			#True
  print(True and False)			#False
  print(True or False)			#True
  print(False or False)			#False
  print(not True)					#False
  print(not False)				#True
  ```

  ``` in #out
  print(3 and 0)			#0
  print(3 or 0)			#3
  print(0 or 3)			#3
  print(3 and 4)			#4
  print(3 or 1)			#3
  ```



####  III-4 복합연산자

* 반복문을 통해서 카운트하는 경우에 가장 많이 활용

​	`+=` `-=` `*=` `/=` `//=` `%=` `**=` 

``` in #out
cnt = 0 
while cnt < 5:
    print(cnt)
    cnt += 1
    
#0
 1
 2
 3
 4
```



####  III-5 기타연산자

**III-5-1) Concatenation**

* 숫자가 아닌 자료형은 `+` 연산자를 통해 합칠 수 있다

  ```in #out
  [1,2,4] + [3,5,7]     #[1,2,4] + [3,5,7]
  ```

  ``` in
  print("="*50)
  print("my program")
  print("="*50)
  ```

  ```
  nm = 'kim'
  nm +nm					#'kimkim'
  nm*2					#'kimkim'
  ```


**III-5-2) Containment Test**

* `in` 연산자를 통해 속해있는지 여부를 확인할 수 있다.

**III-5-3) Identity**

* `is` 연산자를 통해 동일한 object인지 확인할 수 있다.

  ```in #out
  a = 3
  b = 3 
  a is b     				# true
  print(id(a), id(b))     #1874512048 1874512048
  ```


**III-5-4) Indexing/Slicing**

* `[]`를 통한 값 접근 및 `[:]`을 통한 슬라이싱

  ```in #out
  a= 'life is too short, you need Python'
  a[5]		#i
  a[-1]		#n
  a[3:10]		#e is to
  a[0]+a[10]  #lo
  a[:10]		#life is to
  a[19:-7]	#you need
  a[19:]		#you need Python
  ```

  ``` in#out
  "hello"[2]	#l
  ```


####  III-6 연산자 우선순위

1. `()`을 통한 grouping
2. Slicing
3. Indexing
4. 제곱연산자 **
5. 단항연산자 +, - (음수/양수 부호)
6. 산술연산자 *, /, %
7. 산술연산자 +, -
8. 비교연산자, `in`, `is`
9. `not`
10. `and`
11. `or`



###  IIII. 기초 형변환 (Type conversion, Typecasting)

​	파이썬에서 테이터타입은 서로 변환 가능

####  IIII-1 암시적 형변환 Implicit Type Conversion

​	사용자가 의도하지 않았지만 자동 형변환 하는 경우. 아래 상황에서만 가능

* bool

* Numbers (int, float, complex)

  ``` in#out
  True +3			#4
  type(True +3)	#int 
  ```

  ``` in#out
  int_number = 3
  float_number = 0.5
  type(int_number)					#int
  type(float_number)					#float 
  type(int_number + float_number)  	#float 
  ```

  ``` in#out
  complex_number = 3+5j
  type(int_number+ complex_number)	#complex
  ```


####  IIII-2 명시적 형변환 Explicit Type Conversion

​	**암시적 형변환을 제외하고 모두 명시적 형변환 해야함**

- string -> intger : 형식에 맞는 숫자만 가능

- integer -> string : 모두 가능

  **암시적 형변환이 되는 모든 경우도 명시적 형변환 가능**

- `int()` : string, float를 int로 변환

- `float()` : string, int를 float로 변환

- `str()` : int, float, list, tuple, dictionary를 문자열로 변환



###  V. 시퀀스(sequence) 자료형

​	시퀀스 : 데이터 순서대로 나열된 형식 , 이때 나열 != 정렬 

​	파이썬에서 기본적인 시퀀스 타입

​	: 리스트, 튜플, 레인지, 문자열, 바이너리 

####  v-1 list

​	[value1, value2, value3]

``` in#out
i =[]
print(i)		#[]
type(i)			#list
```

```in#out
student = ["kim","jung","lee"]
for k in student:
    print(k)  
#
kim
jung
lee
```

``` in#out
student[1]			#Jung 
```

```in#out
student[0] = 'kang'
print(student)		#['kang', 'jung', 'lee']
```

```in#out
del student[2]
print(student)		#['kang', 'jung']
```

####  v-2 tuple

​	(value1, value2)

* 수정 불가능(immutable)

``` in#out
tu_ex =(1,3)
print(type(tu_ex))			#<class 'tuple'>

is_tu = 1,2
print(type(is_tu))			#<class 'tuple'>
```

####  v-3 range()

​	숫자의 시퀀스를 나타내기 위해 사용

기본형 : `range(n)`

> 0부터 n-1까지 값을 가짐

범위 지정 : `range(n, m)`

> n부터 m-1까지 값을 가짐

범위 및 스텝 지정 : `range(n, m, s)`

> n부터 m-1까지 +s만큼 증가한다

```in#out
list(range(10))			#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(3,7))		#[3, 4, 5, 6]
list(range(0,20,4))		#[0, 4, 8, 12, 16]
```



####  v-4 시퀀스에서 활용할 수 있는 연산자/함수

`x in s` : containment test

`x not in s` : containment test

`s1 + s2` :concatenation

`s * n`: n번만큼 반복하여 더하기

`s[i]`: indexing

`s[i:j]`:slicing   `s[i:j:k]`:k간격으로 slicing

`len(s)`:길이

`min(s)`:최솟값   `max(s)`:최댓값

`s.count(x)`: x의 갯수

```in#out
s ="string"
print("a"in s)			#False
print("a"not in s)		#True
```

``` in#out
g = [2,7,4,5,1]
print(min(g))			#1
max(g)					#7
```



###  VI. set, dictionary

​	순서가 없다.

####  VI-1 set

​	{value1, value2, value3}

```in#out
seta = {1,2,3}
setb = {3,6,9}
print(seta-setb)			#{1,2}			차집합
print(seta|setb)			#{1,2,3,6,9}	합집합
print(seta.union(setb))		#{1,2,3,6,9}	합집합
print(seta&setb)				#{3}		교집합
print(seta.intersection(setb))	#{3}		교집합

```

``` in#out
i = [1,2,3,1,2,3,4]
list(set(i))			#[1, 2, 3, 4]  리스트화 한다
```



####  VI-2 dictionary

​	{Key1:Value1, Key2:Value2, Key3:Value3, ...}

- `key`와 `value`가 쌍
- `{}`를 통해 만들며, `dict()`로 만들 수도 있음
- `key`는 immutable한 모든 것이 가능(불변값 : string, integer, float, boolean, tuple, range)
- `value`는 `list`, `dictionary`를 포함한 모든 것이 가능

```in #out
ph_bk = {"서울":"02", "경기":"031", "인천":"032"}
ph_bk["서울"]				#02

ph_bk.keys()			 #dict_keys(['서울', '경기', '인천'])
```

```in#out
a={1:"a"}
print(a)
a[2]="b"
a

#
{1: 'a'}
{1: 'a', 2: 'b'}
```

```in#out
student = {"a":10, "b":15, "c":20}
sum(student.values())				#45
```





###  VII. 정리 

####  VII-1 데이터 타입

####  VII-2 Type Conversion 







``` 
#workshop 
# 정수 n과 m. 반복문을 사용하지 않고 별(*) 문자를 이용해 가로 길이 n, 세로 길이 m인 직사각형 형태를 출력하기 

n = 5
m = 9
print(("*"*n + "\n") * m )
```

```
#workshop 
#다음 딕셔너리에서 평균 점수를 출력

student = {'python':80, 'algorithom':99, 'django':89, 'flask':83}
print(sum(student.values())/len(student))
```

```
#workshop 
#학생들의 혈액형(A, B, AB, O)데이터. for문을 이용하여 각 혈액형별 학생수의 합계

blood_types = ['A','B','A','O','AB','AB','O','A','B','AB']
result = {}

for type in blood_types:
    if type in result: 
        result[type] += 1
    else: 
        result[type] = 1
print(result)

```











