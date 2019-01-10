
# 딕셔너리 메소드 활용

## 추가 및 삭제

### `.pop(key[, default])`

key가 딕셔너리에 있으면 제거하고 그 값을 돌려줍니다. 그렇지 않으면 default를 반환합니다.

default가 없는 상태에서 딕셔너리에 없으면 KeyError가 발생합니다.


```python
my_dict = {'apple': '사과', 'banana': '바나나'}
#dictionary는 순서가 없다. 
```


```python
my_dict.pop('apple')
```




    '사과'




```python
print(my_dict)
```

    {'banana': '바나나'}
    


```python
my_dict.pop('melon')
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-71-2a8b4f967f4a> in <module>
    ----> 1 my_dict.pop('melon')
    

    KeyError: 'melon'



```python
my_dict.pop('melon', 0)
# my_dict엔 melon이 없다! ('melon',0) -> melon이 없다면 에러를 내지않고  0을 출력해달라는 뜻
```




    0




```python

```

### `.update()`

값을 제공하는 key, value로 덮어씁니다. 


```python
my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
my_dict.update(apple='사과아')
my_dict.update({'apple'='사과'})
my_dict.update({'kiwi':'키위'})
print(my_dict)
```

    {'apple': '사과', 'banana': '바나나', 'melon': '멜론', 'kiwi': '키위'}
    

### `.get(key[, default])`

key를 통해 value를 가져옵니다. 

절대로 KeyError가 발생하지 않습니다. default는 기본적으로 None입니다.


```python
my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
my_dict['pineapple']
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-74-dae0385d9638> in <module>
          1 my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
    ----> 2 my_dict['pineapple']
    

    KeyError: 'pineapple'



```python
print(my_dict.get('pineapple'))
```

    None
    


```python
my_dict.get('apple')
```




    '사과'




```python
my_dict.get('pineapple', 0)
```




    0



## dictionary comprehension

dictionary도 comprehension을 활용하여 만들 수 있습니다. 


```python
cubic = {x: x**3 for x in range(1, 8)}   #딕셔너리를 축약하는 법 
cubic_list =[x**3 for x in range(1, 8)]
print(cubic)
```

    {1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343}
    


```python
cubic = {x**3 for x in range(1, 8)}   #key value를 설정하지 않으면 set이 된다. 
cubic_list =[x**3 for x in range(1, 8)]
print(cubic)
```

    {64, 1, 8, 343, 216, 27, 125}
    


```python
# 다음의 딕셔너리에서 미세먼지 농도가 80 초과 지역만 뽑아 봅시다.
# 예) {'경기': 82, '부산': 90}
dusts = {'서울': 72, '경기': 82, '대전': 29, '중국': 200}
{key: value for key, value in dusts.items() if  value > 80}

new_dict ={}
for d in dusts: 
    if dusts[d] >80:
        new_dict[d] =dusts[d]
print(new_dict)
```

    {'경기': 82, '중국': 200}
    


```python

```


```python
# 다음의 딕셔너리에서 미세먼지 농도가 80초과는 나쁨 80이하는 보통으로 하는 value를 가지도록 바꿔봅시다.
# 예) {'서울': '나쁨', '경기': '보통', '대전': '나쁨', '부산': '보통'}

dusts = {'서울': 72, '경기': 82, '대전': 29, '중국': 200}
{key: '나쁨' if value > 80 else '보통'  for key, value in dusts.items()}
```




    {'서울': '보통', '경기': '나쁨', '대전': '보통', '중국': '나쁨'}




```python
# 만약 elif 말해주면 이렇게 말해주자^_^ 강사용
# 한개 이상이 되면 비추. 비교하기가 어렵다. ,
{key: '매우나쁨' if value > 150 else '나쁨' if value > 80 else '보통' if value > 30 else '좋음'  for key, value in dusts.items()}
```




    {'서울': '보통', '경기': '나쁨', '대전': '좋음', '중국': '매우나쁨'}



## 정리! `map()`, `zip()`, `filter()`

### `map(function, iterable)`

* Iterable의 모든 원소에 function을 적용한 후 그 결과를 돌려줍니다. 

* 대표적으로 iterable한 타입 - list, dict, set, str, bytes, tuple, range

* return은 map_object 형태로 됩니다.


```python
a = [1, 2, 3]
# 위의 코드를 문자열 '123'으로 만들어봅시다.
''.join(map(str, a))
```




    '123'




```python
''.join([str(x) for x in a])
```




    '123'




```python
a = ['1', '2', '3']
# 위의 코드를 [1, 2, 3]으로 만들어봅시다.
list(map(int, a))
```




    [1, 2, 3]




```python
[int(x) for x in a]
```




    [1, 2, 3]



* function은 사용자 정의 함수도 가능하다!


```python
# 세제곱의 결과를 나타내는 함수를 만들어봅시다.
def cube(n):
    return n**3
```


```python
a = [1, 2, 3]
list(map(cube, a))
```




    [1, 8, 27]



### `zip(*iterables)` 

* 복수 iterable한 것들을 모아준다.

* 결과는 튜플의 모음으로 구성된 zip object를 반환한다.


```python
# 예시를 봅시다.
girls = ['jane', 'iu', 'mary','joe']
boys = ['justin', 'david', 'kim','sep']
list(zip(girls, boys))
```




    [('jane', 'justin'), ('iu', 'david'), ('mary', 'kim'), ('joe', 'sep')]




```python
# for문으로 한 명씩 순서대로 매칭시켜봅시다.
# 예) {'jane': 'justin', 'iu': 'david', 'mary': 'kim'}
{x: y for x in girls for y in boys}
# 이렇게 하면 이중 for문이라 key는 유일하니까 마지막 값으로 덮어씌어진다!!!
```




    {'jane': 'kim', 'iu': 'kim', 'mary': 'kim'}




```python
{x: y for x, y in zip(girls, boys)}
```




    {'jane': 'justin', 'iu': 'david', 'mary': 'kim'}



* 그리고 아래와 같이 사용가능하다.


```python
a = '123'
b = '567'

for digit_a, digit_b in zip(a, b):
    print(digit_a, digit_b)
```

    1 5
    2 6
    3 7
    

* zip은 반드시 길이가 같을 때 사용해야한다. 가장 짧은 것을 기준으로 구성한다.


```python
num1 = [1, 2, 3]
num2 = ['1', '2']
list(zip(num1, num2))
```




    [(1, '1'), (2, '2')]



* 물론 길이가 긴 것을 맞춰서 할 수도 있지만, 기억 저 멀리 넣어놓자.


```python
from itertools import zip_longest
list(zip_longest(num1, num2, fillvalue=0))
```




    [(1, '1'), (2, '2'), (3, 0)]



### `filter(function, iterable)`

* iterable에서 function의 반환된 결과가 참인 것들만 구성하여 반환한다.


```python
# 짝수인지 판단하는 함수를 작성해봅시다.
def even(n):
    return not n%2     # n%2 가 0 이면 return 0
```


```python
a = [1, 2, 3]
list(filter(even, a))
```




    [2]




```python
# 다음의 list comprehension과 동일하다.
[x for x in [1, 2, 3] if even(x)
 
```




    [2]




```python
# 다음의 list comprehension과 동일하다.
[x for x in [1, 2, 3] if not x%2 ]
```




    [2]



# 세트 메소드 활용

## 추가 및 삭제

### `.add(elem)`
elem을 세트에 추가합니다. 


```python
a = {1, 2, 3, 4}
a.add(5)
a.add(5)
print(a)
```

    {1, 2, 3, 4, 5}
    

### `update(*others)`

여러가지의 값을 순차적으로 추가합니다.

여기서 반드시 iterable한 값을 넣어야합니다.


```python
a = {1, 2, 3}
a.update({5, 5, 5, 2}, {7, 9})
print(a)

#set은 집합의 성격을 띄므로 중복요소는 없애준다. 
#로또번호 뽑을때 set을 사용한 걸 생각해보자. 무작위 비복원
```

    {1, 2, 3, 5, 7, 9}
    

### `.remove(elem)`

elem을 세트에서 삭제하고, 없으면 KeyError가 발생합니다. 


```python
# 에러를 확인해봅시다.
a.remove(7)
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-5-91e88d8f5a19> in <module>
          1 # 에러를 확인해봅시다.
    ----> 2 a.remove(7)
    

    KeyError: 7



```python
a.remove(3)
print(a)
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-7-24b6210634f1> in <module>
    ----> 1 a.remove(3)
          2 print(a)
    

    KeyError: 3


### `discard(elem)`
x를 세트에서 삭제하고 없어도 에러가 발생하지 않습니다.


```python
a = {1, 2, 3}
a.discard(5)
print(a)
```

    {1, 2, 3}
    

### `pop()`

임의의 원소를 제거해 반환합니다.


```python
a = {7, 6, 21, 1}
a.pop()
```




    1


