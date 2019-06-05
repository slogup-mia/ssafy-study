```python
from IPython.display import IFrame    
```

## 문자열 메소드 활용하기


```python
a = "hI! Everyone, I'm kim"
dir(a)
#dir() 사용할 수 있는 함수 리스트 보기 
```


    ['__add__',
     '__class__',
     '__contains__',
     '__delattr__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__getitem__',
     '__getnewargs__',
     '__gt__',
     '__hash__',
     '__init__',
     '__init_subclass__',
     '__iter__',
     '__le__',
     '__len__',
     '__lt__',
     '__mod__',
     '__mul__',
     '__ne__',
     '__new__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__rmod__',
     '__rmul__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     'capitalize',
     'casefold',
     'center',
     'count',
     'encode',
     'endswith',
     'expandtabs',
     'find',
     'format',
     'format_map',
     'index',
     'isalnum',
     'isalpha',
     'isascii',
     'isdecimal',
     'isdigit',
     'isidentifier',
     'islower',
     'isnumeric',
     'isprintable',
     'isspace',
     'istitle',
     'isupper',
     'join',
     'ljust',
     'lower',
     'lstrip',
     'maketrans',
     'partition',
     'replace',
     'rfind',
     'rindex',
     'rjust',
     'rpartition',
     'rsplit',
     'rstrip',
     'split',
     'splitlines',
     'startswith',
     'strip',
     'swapcase',
     'title',
     'translate',
     'upper',
     'zfill']

### 1. 변형

- `.capitalize()` : 앞글자를 대문자로 만들어 반환합니다.


```python
a.capitalize()
```


    "Hi! everyone, i'm kim"

- `.title()` : 어포스트로피나 공백을 이후를 대문자로 만들어 반환합니다.


```python
a.title()
```


    "Hi! Everyone, I'M Kim"

- `.upper()` : 모두 대문자로 만들어 반환합니다.


```python
a.upper()
```


    "HI! EVERYONE, I'M KIM"



- `lower()` : 모두 소문자로 만들어 반환합니다.


```python
a.lower()
```


    "hi! everyone, i'm kim"

- `swapcase()` : 대<->소문자로 변경하여 반환합니다.


```python
a.swapcase()
```


    "Hi! eVERYONE, i'M KIM"



- `.join(iterable)`

특정한 문자열로 만들어 반환합니다.


```python
#split()
#map(int,input(),split())
```


```python
#합쳐서(join)쓸건데 " "(공백으)로 나눌거다
b= " ".join(['hello','my','name','is','john'])
print(b)
```

    hello my name is john

- `.split()` 

```python
b.split()
```


    ['hello', 'my', 'name', 'is', 'john']



- `.replace(old, new[, count])`

바꿀 대상 글자를 새로운 글자로 바꿔서 반환합니다. 

count를 지정하면 해당 갯수만큼만 시행합니다.


```python
#'yay!' 에서 a를 _로 바꿔보자 
#'wooooow' 를 'wow'로 바꿔보자 

'yay'.replace('a','_')

'wooooow'.replace('oo','o',7)
#(뭘,어떻게,몇번바꿀지)#'woow'

'wooooow'.replace('oooo','')
```


    'wow'



### 2. 글씨 제거 

- `strip([chars])`

특정한 문자들을 지정하면,  양쪽을 제거하거나 왼쪽을 제거하거나(lstrip) 오른쪽을 제거합니다(rstrip)

지정하지 않으면 공백을 제거합니다.


```python
'            hello      '.strip()
#공백제거 #'hello'
```


    'hello'




```python
'            hello      '.lstrip()
#왼쪽공백제거 #'hello      '
```


    'hello      '




```python
'            hello      '.rstrip()
#오른쪽공백제거 #'            hello'
```


    '            hello'



###  3. 탐색 및 검증

- `.find(x)` : x의 첫 번째 위치를 반환합니다. 없으면, -1을 반환합니다.


```python
# ★★★★★★★★★★ 매우중요 
"ssafy".find('y')
#어디있는지 알려준다.# 4
"ssafy".find('s')
# 0 어디에 가장먼저 나오는지.
"ssafy".find('z')
# -1 = False

#비교 
's' in 'ssafy'
#True 
```


    -1



- `.index(x)` : x의 첫번째 위치를 반환합니다. 없으면, 오류가 뜹니다.


```python
"ssafy".index('y')
#4 
"ssafy".index('s')
#0
"ssafy".index('z')
#에러가 난다. 
```


```shell
ValueError                               
Traceback (most recent call last)

<ipython-input-36-8ccd45027c55> in <module>
      3 "ssafy".index('s')
      4 #0
----> 5 "ssafy".index('z')
```



### 4. 다양한 확인 메소드 

: 참/거짓 반환

```
.isaplha(), .isdecimal(), .isdigit(), .isnumeric(), .isspace(), .issuper(), .istitle(), .islower()
```


```python
'123'.isdigit()
```


    True




```python
'1 2 3'.isspace()
#여러가지 시도해보기 
```


    False



- `split()`

문자열을 특정한 단위로 나누어 리스트로 반환합니다.


```python
'hello world'.split()
#['hello', 'world']
```


    ['hello', 'world']




```python
'35 50'.split()
#['35', '50']

list(map(int,'35 50'.split()))
#[35, 50]
```


    [35, 50]



##  리스트 메소드 활용하기

###  값 추가 및 삭제

- `.append(x)`

리스트에 값을 추가할 수 있습니다.


```python
# 리스트 하나를 만들어봅시다.
caffe = ['starbucks', 'tomntoms', 'hollys']
```


```python
# 값을 추가해봅시다..
caffe.append('w cafe')
print(caffe)
```

    ['starbucks', 'tomntoms', 'hollys', 'w cafe', 'w cafe']



- `.remove()`

```python
# 값을 제거해봅시다..
caffe.remove('w cafe')
print(caffe)
```

    ['starbucks', 'tomntoms', 'hollys', 'w cafe']



```python
# 어렵게 넣어보도록 해봅시다.(append 사용하지 않고 list에 추가하는 방법)
caffe[len(caffe):]= ['w cafe']
print(caffe[len(caffe):])
print(caffe)
```

    []
    ['starbucks', 'tomntoms', 'hollys', 'w cafe', 'w cafe', 'w cafe', 'w cafe', 'w cafe']



```python
['starbucks', 'tomntoms', 'hollys', 'w cafe', 'w cafe']+['b cafe']
caffe+['b cafe']
```




    ['starbucks',
     'tomntoms',
     'hollys',
     'w cafe',
     'w cafe',
     'w cafe',
     'w cafe',
     'w cafe',
     'b cafe']



### `.extend(iterable)`

리스트에 iterable(list, range, tuple, string*유의*) 값을 붙일 수가 있습니다.


```python
# 앞서 만든 리스트에 추가해봅시다.
caffe.append('ediya')
print(caffe)
```

    ['starbucks', 'tomntoms', 'hollys', 'w cafe', 'w cafe', 'w cafe', 'w cafe', 'w cafe', 'ediya', 'ediya']



```python
# 앞서 배운 list concatenate와 동일합니다.
caffe.extend(['coffebean','빽다방','커피니','던킨도넛','크리스피크림'])
print(caffe)
```

    ['starbucks', 'tomntoms', 'hollys', 'w cafe', 'w cafe', 'w cafe', 'w cafe', 'w cafe', 'ediya', 'ediya', 'coffebean', '빽다방', '커피니', '던킨도넛', '크리스피크림', 'coffebean', '빽다방', '커피니', '던킨도넛', '크리스피크림']



```python
# append와 비교해봅시다.

```


```python
#1. concatenation : 원본수정 X 
print(caffe + ['바나프레소','엔젤리너스'])
# 그래서, 이때 caffe를 프린트 하면 '바나프레소','엔젤리너스'가 포함되지 않는 리스트가 출력됨
```

    ['starbucks', 'tomntoms', 'hollys', 'w cafe', 'w cafe', 'w cafe', 'w cafe', 'w cafe', 'ediya', 'ediya', 'coffebean', '빽다방', '커피니', '던킨도넛', '크리스피크림', 'coffebean', '빽다방', '커피니', '던킨도넛', '크리스피크림', '바나프레소', '엔젤리너스']



```python
a=[1,2,3,4]
b=(5,6)
#a+b는 오류가 난다. 그러나 아래는 작동.
a+=b

#concatenation과 동일한 경우이다. 이때 a원본은 [1,2,3,4] 그대로. 
```


```python
#1. 펠린드롬 판단 
word = 'hellososolleh'
def ispal(word):
    return word == word[::-1]

ispal(word)
```




    True




```python
#2. 띄어쓰기 된 word도 띄어쓰기 무시하고 펠린드롬 판단하기 'hell osos oll eh'
word = 'hello s oso ll eh'
def ispal(word):
    word = word.replace(" ","")
    return word == word[::-1]

ispal(word)
```




    True




```python
#3.slicing 쓰지않고 짜보기
```


```python
#4.한글자씩 비교해서 보기(character 단위로 비교하는 코드)
#  - 대소문자도 커버하는 판단 

word = 'HellosoSolleh'

def ispal_cha(word): 
    word= word.lower()
    fr=[]
    ba=[]
    for i in word[0:]:
        fr.append(i)

    for a in word[::-1]:
        ba.append(a)
    
    return fr == ba

ispal_cha(word)
```




    True




```python

```




    True




```python
#5.재귀로 짜보기
```

### `insert(i, x)`

정해진 위치 `i`에 값을 추가합니다. 


```python
# 앞서 만든 리스트의 가장 앞에 'hi'를 넣어주세요.
caffe.insert(0,'hi')
print(caffe)
```

    ['hi', '메가커피', 'starbucks', 'tomntoms', 'hollys', 'w cafe', 'w cafe', 'w cafe', 'w cafe', 'w cafe', 'ediya', 'ediya', 'coffebean', '빽다방', '커피니', '던킨도넛', '크리스피크림', 'coffebean', '빽다방', '커피니', '던킨도넛', '크리스피크림']



```python
# 앞서 만든 리스트의 가장 뒤에 'bye'를 넣어주세요.
caffe.insert(len(caffe),'bye')
print(caffe)
```

    ['bye', 'hi', '메가커피', 'starbucks', 'tomntoms', 'hollys', 'w cafe', 'w cafe', 'w cafe', 'w cafe', 'w cafe', 'ediya', 'ediya', 'coffebean', '빽다방', '커피니', '던킨도넛', '크리스피크림', 'coffebean', '빽다방', '커피니', '던킨도넛', 'bye', '크리스피크림', 'bye']



```python
# 길이를 넘어서는 인덱스는 무조건 마지막에 하나만 붙습니다.
caffe= ['1','2']
caffe.insert(99,'마지막에붙는다')
print(caffe)
```

    ['1', '2', '마지막에붙는다']


### `remove(x)`

리스트에서 값이 x인 것을 삭제합니다. 


```python
numbers = [1, 2, 3, 1, 2]
numbers.remove(3)
print(numbers)
```

    [1, 2, 1, 2]



```python
# 중복된 값 1을 삭제 해봅시다.
numbers.remove(1)
print(numbers)
```

    [2, 1, 2]



```python
# 한번 더 삭제해봅시다.
numbers.remove(1)
print(numbers)
```

    [2, 2]



```python
# remove는 값이 없으면 오류가 발생합니다. 확인해봅시다.
numbers.remove(2)
print(numbers)
```


    ---------------------------------------------------------------------------
    
    ValueError                                Traceback (most recent call last)
    
    <ipython-input-75-d65fc5666819> in <module>
          1 # remove는 값이 없으면 오류가 발생합니다. 확인해봅시다.
    ----> 2 numbers.remove(2)
          3 print(numbers)


    ValueError: list.remove(x): x not in list


### `.pop(i)`

정해진 위치 `i`에 있는 값을 삭제하며, 그 항목을 반환합니다.

`i`가 지정되지 않으면 마지막 항목을 삭제하고 되돌려줍니다.


```python
a = [1, 2, 3, 4, 5, 6]
```


```python
# 가장 앞에 있는 것을 삭제해봅시다. return도 확인해보세요.
a.pop(0)
print(a)
```

    [2, 3, 4, 5, 6]



```python

```


```python
# 값이 return이 된다는 것은 별도의 변수에 저장할 수 있다는 것입니다. 

```

## 탐색 및 정렬

### `.index(x)`

원하는 값을 찾아 index 값을 반환합니다.


```python
a = [1, 2, 3, 4, 5]
a.index(1)
```




    0




```python
# index는 없을 시 오류가 발생합니다. 확인해봅시다. 
# 앞서 remove 역시도 같은 에러가 발생하였습니다. (ValueError)

```

### `.count(x)`

원하는 값의 갯수를 확인할 수 있습니다.


```python
a = [1, 2, 5, 1, 5, 1]
a.count(5)
```




    2




```python
# 따라서 원하는 값을 모두 삭제하려면 다음과 같이 할 수 있습니다.
a = [1, 2, 1, 3, 4]
for i in range(a.count(1)):
    a.remove(1)
print(a)
```

    [2, 3, 4]



```python
# 모두 삭제되었는지 검증해봅시다.

```

### `.sort()`

정렬을 합니다. 

sorted()와는 다르게 원본 list를 변형시키고, None을 리턴합니다.


```python
import random
lotto = random.sample(range(1,46),6)

#1. sorted()
sorted_lotto = sorted(lotto)
print(sorted_lotto)

#2. [].sort()
print(lotto.sort())
```

    [4, 5, 11, 14, 25, 33]
    None



```python

```

### `reverse()`

반대로 뒤집습니다. (정렬 아님)


```python
classroom = ['Tom', 'David', 'Justin']
print(reversed(classroom))
print(classroom)
```

    <list_reverseiterator object at 0x00C461D0>
    ['Tom', 'David', 'Justin']



```python
print(list(reversed(classroom)))
print(classroom)

print(classroom.reverse())
print(classroom)
```

    ['Justin', 'David', 'Tom']
    ['Tom', 'David', 'Justin']
    None
    ['Justin', 'David', 'Tom']


## 복사


```python
b = a 
b[0] = 0 
print(a)
#mutable 자료형 [list],{dictionary}
#은 복사할 때 값이 복사되는것이아니라 주소가 복사되어 원본이 바뀐다.
```


```python
# 리스트 복사를 해봅시다.
original_list = [1, 2, 3]
new_list = original_list   #복사가 아님
print(id(new_list))
print(id(original_list))

```

    12915016
    12915016



```python
new_list = original_list[:]
print(id(new_list))
print(id(original_list))
```


```python
print(original_list is new_list) #==
# b의 값을 바꾸고 a를 출력해봅시다.

```


```python
# 숫자를 확인해봅시다.
a=12
b=a
print(b == a)  #True
print(b is a)  #True
```

    True
    True



```python
# 딕셔너리도 확인해봅시다.
student = {"name":"John","age":"34"}
new_student = student
print(new_student is student)
```

    True



```python
student = {"name":"John","age":"34"}
new_student = student.copy()
print(new_student is student)
```

    False



```python
IFrame('https://goo.gl/vx1yGx', width='100%', height='300px')
```


```python
IFrame('https://goo.gl/N43pw6', width='100%', height='300px')
```

* 파이썬에서 모든 변수는 객체의 주소를 가지고 있을 뿐입니다. 

```
num = [1, 2, 3]
```

* 위와 같이 변수를 생성하면 hong이라는 객체를 생성하고, 변수에는 객체의 주소가 저장됩니다.


* 변경가능한(mutable) 자료형과 변경불가능한(immutable) 자료형은 서로 다르게 동작합니다.

따라서, 복사를 하고 싶을 때에는 다음과 같이 해야한다.


```python
a = [1, 2, 3]
b = a[:]
b[0] = 5
print(a)
```

    [1, 2, 3]



```python
a = [1, 2, 3]
b = list(a)
b[0] = 5
print(a)
```

    [1, 2, 3]



```python
IFrame('https://goo.gl/ZH6yZd', width='100%', height='300px')
```

* 하지만, 이렇게 하는 것도 일부 상황에만 서로 다른 얕은 복사(shallow copy)입니다.
* 아래 shallow copy의 한계 예 


```python
a = [1, 2, [1, 2]]
b = a[:]
b[2][0] = 3
print(a)

# a = [1, 2, [  ]] 까지만 복제되고, a = [     [1, 2]] 한번 더들어가는 부분은 복제되지 않는다.

```

    [1, 2, [3, 2]]



```python
#위를 이해를 돕기위한 비교 
a = [1, 2, [1, 2]]
b = a[:]
b[1] = 3
print(a)
```

    [1, 2, [1, 2]]



```python
IFrame('https://goo.gl/FZcYbJ', width='100%', height='300px')
```

* 만일 중첩된 상황에서 복사를 하고 싶다면, 깊은 복사(deep copy)를 해야합니다. 

* 즉, 내부에 있는 모든 객체까지 새롭게 값이 변경됩니다.


```python
import copy     #위의 shallow copy의 한계를 극복하기 위한 모듈 
                #리스트 구조 모든 단계를 카피한다. 
a = [1, 2, [1, 2]]
b = copy.deepcopy(a)
b[2][0] = 3
print(a)
```


```python
IFrame('https://goo.gl/dtnCzY', width='100%', height='300px')
```

## 삭제

리스트의 모든 항목을 삭제합니다.


```python
numbers = list(range(1, 46))
numbers.clear()
print(numbers)
```

# List Comprehension

List를 만들 수 있는 간단한 방법이 있습니다.

## 사전 준비

> 다음의 리스트를 만들어보세요. 

1. 1~10까지의 숫자 중 짝수만 담긴 리스트 `even_list`

2. 1~10까지의 숫자로 만든 세제곱 담긴 리스트 `cubic_list`


```python
even_list =[]  #짝수만 담아야지 
for i in range(1,11):
    if i%2 ==0:
        even_list.append(i)
print(even_list)
```

    [2, 4, 6, 8, 10]



```python
#[채워넣을 값에 해당하는 변수]

numbers = [x for x in range(1,6)]

# =>  for i in range(1,6):
#        numbers.append(i)

print(numbers)
```

    [1, 2, 3, 4, 5]



```python
[x*2 for x in range(1,6)]
```




    [2, 4, 6, 8, 10]




```python
[i**3 for i in range(1,11)]
```




    [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]



## 활용법

여러개의 `for` 혹은 `if`문을 중첩적으로 사용 가능합니다.



## 연습 문제

### 짝짓기 - 곱집합

> 주어진 두 list의 가능한 모든 조합을 담은 `pair` 리스트를 만들어주세요.

1. 반복문 활용
2. list comprehension 활용

---

```
girls = ['jane', 'iu', 'mary']
boys = ['justin', 'david', 'kim']

예시 출력)
    
[('justin', 'jane'), ('justin', 'iu'), ('justin', 'mary'), ('david', 'jane'), ('david', 'iu'), ('david', 'mary'), ('kim', 'jane'), ('kim', 'iu'), ('kim', 'mary')]
```




```python
# 아래에 반복문을 활용하여 만들어주세요.
girls =['j','s','w']
boys =['k','h','j']

pair =[]
for girl in girls:
    for boy in boys:
        pair.append((boy,girl))
print(pair)
```

    [('k', 'j'), ('h', 'j'), ('j', 'j'), ('k', 's'), ('h', 's'), ('j', 's'), ('k', 'w'), ('h', 'w'), ('j', 'w')]



```python
# 아래에 List comprehension을 활용하여 만들어주세요.
[(boy,girl)for boy in boys for girl in girls]
# 결과물은 리스트로, 요소들은 튜플로 나옴을 알아야 한다. 
```




    [('k', 'j'),
     ('k', 's'),
     ('k', 'w'),
     ('h', 'j'),
     ('h', 's'),
     ('h', 'w'),
     ('j', 'j'),
     ('j', 's'),
     ('j', 'w')]



### 피타고라스 정리

> 주어진 조건(x < y < z < 50) 내에서 피타고라스 방정식의 해를 찾아보세요.

1. 반복문 활용

2. list comprehension 활용

```
예시 출력)
[(3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 15, 17), (9, 12, 15), (9, 40, 41), (10, 24, 26), (12, 16, 20), (12, 35, 37), (15, 20, 25), (15, 36, 39), (16, 30, 34), (18, 24, 30), (20, 21, 29), (21, 28, 35), (24, 32, 40), (27, 36, 45)]
```


```python
# 아래에 반복문을 활용하여 만들어주세요.
ptgrs=[]
for x in range(1,51):
    for y in range(x,51):
        for z in range(y,51):
            if x**2 + y**2 == z**2:
                ptgrs.append((x,y,z))

print(ptgrs)
                
```

    [(3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 15, 17), (9, 12, 15), (9, 40, 41), (10, 24, 26), (12, 16, 20), (12, 35, 37), (14, 48, 50), (15, 20, 25), (15, 36, 39), (16, 30, 34), (18, 24, 30), (20, 21, 29), (21, 28, 35), (24, 32, 40), (27, 36, 45), (30, 40, 50)]



```python
# 아래에 List comprehension을 활용하여 만들어주세요.
[(boy,girl)for boy in boys for girl in girls]

[(x,y,z)for x in range(1,51) for y in range(x,51) for z in range(y,51) if x**2 + y**2 == z**2]
```




    [(3, 4, 5),
     (5, 12, 13),
     (6, 8, 10),
     (7, 24, 25),
     (8, 15, 17),
     (9, 12, 15),
     (9, 40, 41),
     (10, 24, 26),
     (12, 16, 20),
     (12, 35, 37),
     (14, 48, 50),
     (15, 20, 25),
     (15, 36, 39),
     (16, 30, 34),
     (18, 24, 30),
     (20, 21, 29),
     (21, 28, 35),
     (24, 32, 40),
     (27, 36, 45),
     (30, 40, 50)]



### 모음 제거하기

> 다음의 문장에서 모음(a, e, i, o, u)를 모두 제거하시오.

1. list comprehension만 사용해보세요.

``` 
    words = 'Life is too short, you need python!'

    예시출력)
    Lf s t shrt, y nd pythn!
```


```python
# 참고
words = 'Life is too short, you need python!'
print(words.split())
result = [char for char in words]
print(result)
```

    ['Life', 'is', 'too', 'short,', 'you', 'need', 'python!']
    ['L', 'i', 'f', 'e', ' ', 'i', 's', ' ', 't', 'o', 'o', ' ', 's', 'h', 'o', 'r', 't', ',', ' ', 'y', 'o', 'u', ' ', 'n', 'e', 'e', 'd', ' ', 'p', 'y', 't', 'h', 'o', 'n', '!']



```python
# 아래에 List comprehension을 활용하여 만들어주세요.
words = 'Life is too short, you need python!'
vowers = 'aeiou'      # =['a','e','i','o','u']도 가능 
result = [char for char in words if char not in vowers]
"".join(result)
```




    'Lf s t shrt, y nd pythn!'



# 딕셔너리 메소드 활용

## 추가 및 삭제

### `.pop(key[, default])`

key가 딕셔너리에 있으면 제거하고 그 값을 돌려줍니다. 그렇지 않으면 default를 반환합니다.

default가 없는 상태에서 딕셔너리에 없으면 KeyError가 발생합니다.


```python
my_dict = {'apple': '사과', 'banana': '바나나'}
```


```python

```


```python

```


```python

```


```python

```

### `.update()`

값을 제공하는 key, value로 덮어씁니다. 


```python
my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}

```

### `.get(key[, default])`

key를 통해 value를 가져옵니다. 

절대로 KeyError가 발생하지 않습니다. default는 기본적으로 None입니다.


```python
my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}

```


```python

```


```python

```


```python

```

## dictionary comprehension

dictionary도 comprehension을 활용하여 만들 수 있습니다. 

* 추후에 zip, map 등을 배우고 다시 다루도록 하겠습니다 :)


```python

```

# 세트 메소드 활용

## 추가 및 삭제

### `.add(elem)`
elem을 세트에 추가합니다. 


```python
a = {1, 2, 3, 4}

```

### `update(*others)`

여러가지의 값을 순차적으로 추가합니다.

여기서 반드시 iterable한 값을 넣어야합니다.


```python
a = {1, 2, 3}

```

### `.remove(elem)`

elem을 세트에서 삭제하고, 없으면 KeyError가 발생합니다. 


```python
# 에러를 확인해봅시다.

```


```python
a.remove(3)

```

### `discard(elem)`
x를 세트에서 삭제하고 없어도 에러가 발생하지 않습니다.


```python
a = {1, 2, 3}

```

### `pop()`

임의의 원소를 제거해 반환합니다.


```python
a = {7, 6, 21, 1}

```
