
# 문자열 계산하기

> 아래와 같이 문자열이 주어졌을 때, 바보같은 사용자를 위해 계산을 해주려고 한다.
>
> 이 계산기는 더하기와 빼기밖에 못한다.
>
> `calc(equation)`을 만들어봅시다.

---

예시)

```python
calc('123+2-124') #=> 1
calc('-12+12-7979+9191') #=> 1212
calc('+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1') #=> 0
```


```python
# 여기에 코드를 작성하세요

#앞에 -가 있는 숫자는 cal_min=[]에, 나머지는 cal_sum=[]에 넣는다. 
    # for a in calc: 
        # if a[i]== '-':
            # a[i+1] = cal_min=[] 
        #else:
            #a = cal_sum[]
#sum=[]에 있는 수를 모두 더한후 cal_min=[]에 있는 수를 모두 뺀다. 

def calc(equation):

```


      File "<ipython-input-9-8eade6c699fa>", line 11
        def calc(equation):
                           ^
    SyntaxError: unexpected EOF while parsing
    



```python
# 선생님 답 1 : 
def calc(equation):
    equation = equation.replace('+',' +')  #'123 +2-124'
    equation = equation.replace('-',' -')  #'123 +2 -124'
##     new_nums=[]
##     for num in equation.split():   #split ['123', '+2', '-124']
##         new_nums.append(int(num))
#    return [int(num) for num in equation.split()]   #[123, 2, -124]
#    return list(map(int,equation.split()))  #[123, 2, -124]
    return sum(map(int,equation.split()))

calc('123+2-124')
```




    1




```python
# 선생님 답 2 : 
def calc(equation):
    result=0
    tmp=''
    for char in equation:
        if tmp and not char.isdecimal():
            result += int(tmp)
            tmp = ''
        tmp += char 
    return result + int(tmp)

calc('123+2-124')
```




    1




```python
# 해당 코드를 통해 올바른 결과가 나오는지 확인하세요.
print(calc('123+2-124'))
print(calc('-12+12-7979+9191'))
print(calc('+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1'))
```

# 나만의 딕셔너리 생성기

> key의 리스트와 value의 리스트로 딕셔너리를 생성하여 return 하는 `create_dict(keys, values)` 함수를 작성하세요.
>
>만약에 value의 갯수가 key의 갯수보다 부족한 경우, None을 채워 넣어야 합니다. 반대로 key의 갯수가 부족한 경우, 초과하는 value들은 무시해도 됩니다.

예시)
```python
create_dict(['a', 'b', 'c', 'd'], [1, 2, 3]) #=> {'a': 1, 'b': 2, 'c': 3, 'd': None}
create_dict(['a', 'b', 'c'], [1, 2, 3, 4]) #=> {'a': 1, 'b': 2, 'c': 3}
```


```python
# 여기에 코드를 작성하세요.
#def create_dict(keys, values):
list[0] = my_key[]
list[1] = my_val[]
if len(my_key) > len(my_val):
    my_val.append("None")

list(zip) 

```


```python
# 선생님 답 
def create_dict(keys, values):
    new_dict = {}
    for i in range(len(keys)):
        if i < len(values):
#            new_dict[keys[i]] = values[i]
            new_dict.update({key[i]:values[i]})  #윗줄과 같은 의미 
        else:
#            new_dict[keys[i]] = None
            new_dict.update({key[i]:None})
    return new_dict

            
```


```python
# 선생님 답2 
def create_dict(keys, values):
    while len(keys)>len(values):
        values.append(None)
    new_dict = dict(zip(keys,values))
    return new_dict
```


```python
# 해당 코드를 통해 올바른 결과가 나오는지 확인하세요.
print(create_dict(['a', 'b', 'c', 'd'], [1, 2, 3]))
print(create_dict(['a', 'b', 'c'], [1, 2, 3, 4]))
```

    {'a': 1, 'b': 2, 'c': 3, 'd': None}
    {'a': 1, 'b': 2, 'c': 3}
    

# 시험 채점 시스템

> 첫 번째 인자는 정답이 들어있는 리스트, 두 번째 인자는 사용자의 답이 들어있는 리스트입니다. 두 리스트는 비어있지 않으며 길이가 같습니다.
>
> 정답의 경우 +4점, 오답의 경우 -1점, 공백 응답(빈 문자열)의 경우 0점입니다. 만약, 점수가 0보다 작으면 0을 return 합니다.
>
> 위와 같이 시험 점수를 체크하는 함수 `check_score(real_answers, my_answers)` 을 작성하세요.

예시)

```python
check_score(["a", "a", "b", "b"], ["a", "c", "b", "d"]) #=> 6
check_score(["a", "a", "c", "b"], ["a", "a", "b", ""]) #=> 7
check_score(["a", "a", "b", "c"], ["a", "a", "b", "c"]) #=> 16
check_score(["b", "c", "b", "a"], ["", "a", "a", "c"]) #=> 0
```


```python
# 여기에 코드를 작성하세요.
#선생님답 
def check_score(real_answers, my_answers):
    score = 0 
    for i in range(0,len(real_answers)):
        if real_answers[i] == my_answers[i]:
            score += 4
        elif my_answers == "":
            score += 0 
        else: 
            score += -1 
    
#     if score >= 0:
#         return score 
#     else:
#         return 0 
    return score if score >= 0 else 0


```


```python
def check_score(real_answers, my_answers):
    return list(zip(real_answers, my_answers))


#out
# [('a', 'a'), ('a', 'c'), ('b', 'b'), ('b', 'd')]
# [('a', 'a'), ('a', 'a'), ('c', 'b'), ('b', '')]
# [('a', 'a'), ('a', 'a'), ('b', 'b'), ('c', 'c')]
# [('b', ''), ('c', 'a'), ('b', 'a'), ('a', 'c')]
```


```python
def check_score(real_answers, my_answers):
    return [4 if r == m else -1 for r,m in list(zip(real_answers, my_answers))]
            
#out
"""
[4, -1, 4, -1]
[4, 4, -1, -1]
[4, 4, 4, 4]
[-1, -1, -1, -1]
"""
#이때 빈 스트링 일때는 커버하지 못한다 (=>아래)
```


```python
def check_score(real_answers, my_answers):
    return [4 if r == m else -1 for r,m in list(zip(real_answers, my_answers))if m]

#out
"""
[4, -1, 4, -1]
[4, 4, -1]
[4, 4, 4, 4]
[-1, -1, -1]
"""            
```


```python
def check_score(real_answers, my_answers):
    return sum([4 if r == m else -1 for r,m in list(zip(real_answers, my_answers))if m])

#out 
"""  
6
7
16
-3
""" 
#점수가 -값일때 0을 출력해야겠지 점수니까 (=>아래 )
```


```python
def check_score(real_answers, my_answers):
    return max(0, sum([4 if r == m else -1 for r,m in list(zip(real_answers, my_answers))if m]))

# max(0,10)  => 값을 0~10으로 제한한다. 
```


```python
# 해당 코드를 통해 올바른 결과가 나오는지 확인하세요.
print(check_score(["a", "a", "b", "b"], ["a", "c", "b", "d"]))
print(check_score(["a", "a", "c", "b"], ["a", "a", "b", ""]))
print(check_score(["a", "a", "b", "c"], ["a", "a", "b", "c"]))
print(check_score(["b", "c", "b", "a"], ["", "a", "a", "c"]))
```

    6
    7
    16
    0
    


```python

```
