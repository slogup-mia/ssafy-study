
# 불쌍한 달팽이 - 고전 수학문제

>달팽이는 낮 시간 동안에 기둥을 올라갑니다. 하지만 밤에는 잠을 자면서 어느 정도의 거리만큼미끄러집니다. (낮 시간 동안 올라간 거리보다는 적게 미끄러집니다) 달팽이가 기둥의 꼭대기에 도달하는 날까지 걸리는 시간을 계산하면 됩니다.

> 당신의 함수에 들어가야 하는 3개의 인자는 다음과 같습니다.
- 기둥의 높이(미터)
- 낮 시간 동안 달팽이가 올라가는 거리(미터)
- 달팽이가 야간에 잠을 자는 동안 미끄러지는 거리(미터)

```
snail(100, 5, 2)
33
```


```python
# 여기에 코드를 작성하세요
# snail(20,5,2)    20/(5-2) 


def sn(a,b,c):
    answer = a/(b-c)
    return answer

print(sn(100,5,2))


```

    33.333333333333336
    


```python
# 선생님 답 

def snail(height,day,night):
    count = 0
    while True: 
        count += 1
        height -= day
        if height <=0:
            return count
        height += night
    return count

print(snail(100,5,2))

```

    33
    

# 무엇이 중복일까

> 다음 리스트에서 중복되는 요소만 뽑아서 새로운 리스트에 옮기시오. 

```
입력)
duplicated(['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n', 'b'])

출력)
['b', 'n']
```


```python
# 여기에 코드를 작성하시오.
# 

def duplicated(li):
    dub = []
    for i in li:
        for a in li[i+1:]:
            if i == a:
                dub.append(i)
    return dub 
print(duplicated(['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n', 'b']))
            
        
                
    
```

    ['b', 'b', 'b', 'c', 'b', 'b', 'b', 'd', 'm', 'n', 'n', 'n', 'n', 'b', 'b', 'b']
    


```python
duplicated= ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n', 'b']
for i in duplicated[1:]:
    print(i)
```

    b
    c
    b
    d
    m
    n
    n
    b
    


```python
list(set(['b', 'n', 'b'])
```


```python
a = []

False or a.append('c')
print(a)
```


```python
#선생님 답 

def dup(alp):
    dup =[]
    for val in alp:
        if alp.count(val)> 1 and val not in dup:
            dup.append(val)
    return dup

print(dup(['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n', 'b']))
            
```

    ['b', 'n']
    


```python
#선생님 답 2 conprihension

def dup(alp):
    return list({val for val in alp if alp.count(val)>1})

print(dup(['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n', 'b']))
```

    ['b', 'n']
    

# 알파벳만 남기고 뒤집기

>문자열이 주어지면, 해당 문자열 중에서 알파벳이 아닌 문자는 전부 빼고 거꾸로 뒤집어 반환하는 함수를 작성하세요.

```
예시) 
reverse_letter("krishan")
"nahsirk"

reverse_letter("ultr53o?n")
"nortlu"
```


```python
# 여기에 코드를 작성하세요
# A1
reverse_letter = ("ultr53o?n")
p = re.compile("[^0-9]")
print("".join(p.findall(reverse_letter))
```


      File "<ipython-input-14-ce004f598eee>", line 5
        print("".join(p.findall(reverse_letter))
                                                ^
    SyntaxError: unexpected EOF while parsing
    



```python
#선생님 답 

def rev(word):
    nw =[]
    for char in word:
        if char.isalpha():
            nw.append(word)
            
    return nw
print(rev("krishan"))
```

    ['krishan', 'krishan', 'krishan', 'krishan', 'krishan', 'krishan', 'krishan']
    


```python
#선생님 답 

def rev(word):
    nw=[char for char in word if char.isalpha()]
    return "".join(reversed(nw))    #list니까 join으로 
print(rev("krishan"))
```

    nahsirk
    


```python
print(reverse_letter("krishan"))
print(reverse_letter("ultr53o?n"))
```

# 편-안한 단어

>(QWERTY 키보드를 사용하여 타이핑을 한다고 가정할 때) '편안한 단어'는 타이핑 할 때 손을
번갈아 칠 수 있는 단어를 말합니다.단어를 인자로 받아 그것이 '편안한 단어'인지 여부를 True/False로 반환하는 함수를 만드세요.(모든 단어는 a ~ z까지 오름차순으로 구성된 문자열입니다.)

>문자 목록
- 왼손: q, w, e, r, t, a, s, s, d, f, g, z, x, c, v, b
- 오른손: y, u, i, o, p, h, j, k, l, n, m


```python
# 여기에 코드를 작성하세요.
def cftb(word):
    left, right ='qwertassdfgzxcvb','yuiophjklnm'
    
    if len(word)==0:
        return True 
```


```python
#선생님답
def cftb(word):
    left, right ='qwertassdfgzxcvb','yuiophjklnm'
    
    l = True if word[0] in left else False 
    
    for letter in word[1:]:
        if letter in left and l:
            return False
        if letter in right and not l:
            return False
        l = not l 
    return True       # false인 경우를 다 통과하면 true가 뜨게 하는것 

print(cftb("qywu"))
```

    True
    


```python
print(comfortable_word("qywu"))
print(comfortable_word("apple"))
```

# 숫자패턴

>원하는 행까지 아래의 패턴을 생성하는 함수를 작성하세요. 만약 인자가 0이나 음의 정수인 경우 "" 즉, 빈 문자열로 반환하세요.짝수가 인수로 전달되면 패턴은 통과된 짝수보다 작은 최대 홀수까지 계속되어야 합니다.

```
예시 
pattern(9):

1
333
55555
7777777
999999999

pattern(6)
1
333
55555

유의
패턴에 공백은 없습니다.
```


```python
# 여기에 코드를 작성하세요

def pattern(a):
    for i in range(1,a+1):
        if i%2 == 1:
            print(str(i)*(i))
        else:
            pass 
        
return(pattern(10))
        
        
```

    1
    333
    55555
    7777777
    999999999
    


```python
#선생님 답 
#개미수열 문제도 있다. 참고 

def pt(a):
    result=[str(n)*n for n in range(1,a+1) if n%2]
    return '\n'.join(result)

pt(9)

```




    '1\n333\n55555\n7777777\n999999999'




```python
# 해당 코드를 통해 올바른 결과가 나오는지 확인하세요.
print(pattern(9))
print(pattern(6))
```

# 숫자가 좋아

> 스트링과 함께 섞여있는 문자열들 속에서 정수만 뽑아내 합을 반환하는 함수 `pick_and_sum`를 작성하세요.

예시)
```python
pick_and_sum("The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog") #=> 3635
```


```python
# 여기에 코드를 작성하세요.
def pick_and_sum():
    for i in li:
        if i 
    
```


```python
#지명님 답 
def pick_and_sum(word):
    a=[char if char.isdecimal else" "for char in word]
    a="".join(a)
    return sum([int(i) for i in a.split()])
pick_and_sum("The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog")
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-30-7044119c6d8a> in <module>
          4     a="".join(a)
          5     return sum([int(i) for i in a.split()])
    ----> 6 pick_and_sum("The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog")
    

    <ipython-input-30-7044119c6d8a> in pick_and_sum(word)
          3     a=[char if char.isdecimal else" "for char in word]
          4     a="".join(a)
    ----> 5     return sum([int(i) for i in a.split()])
          6 pick_and_sum("The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog")
    

    <ipython-input-30-7044119c6d8a> in <listcomp>(.0)
          3     a=[char if char.isdecimal else" "for char in word]
          4     a="".join(a)
    ----> 5     return sum([int(i) for i in a.split()])
          6 pick_and_sum("The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog")
    

    ValueError: invalid literal for int() with base 10: 'The30quick20brown10f0x1203jumps914ov3r1349the102l4zy'



```python
#다른학생의 답 
def pick_and_sum(word):
    res = [int(i) for i in word if i.isdecimal()]
    return sum(res)
    
print(pick_and_sum("The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog"))
```

    53
    


```python
# 선생님답 step.1
def pick_and_sum(word):
    for c in word:
        if not c.isdecimal():
            word = word.replace(c," ")
    return word
print(pick_and_sum("The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog"))
```

       30     20     10 0 1203     914  3 1349   102 4      
    


```python
# 선생님답 step.2 
def pick_and_sum(word):
    for c in word:
        if not c.isdecimal():
            word = word.replace(c," ")
    return word.split()
print(pick_and_sum("The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog"))
```

    ['30', '20', '10', '0', '1203', '914', '3', '1349', '102', '4']
    


```python
# 선생님답 step.3
def pick_and_sum(word):
    for c in word:
        if not c.isdecimal():
            word = word.replace(c," ")
    return [int(a) for a in word.split()]
print(pick_and_sum("The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog"))
```

    [30, 20, 10, 0, 1203, 914, 3, 1349, 102, 4]
    


```python
# 선생님답 step.4
def pick_and_sum(word):
    for c in word:
        if not c.isdecimal():
            word = word.replace(c," ")
    return sum([int(a) for a in word.split()])
print(pick_and_sum("The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog"))
```

    3635
    


```python
# 선생님답 step2 -> map먹이기 
def pick_and_sum(word):
    for c in word:
        if not c.isdecimal():
            word = word.replace(c," ")
    return sum(list(map(int,word.split())))  
    #map(함수이름,적용할 자료구조) 리스트가 아니더라도 순회하면서 맵의 인자로 넣을수있다. 자료구조는 순회할 수 있는 것을 넣는다. 
    #sum(리스트, 딕셔너리, 순회할수있는 모든 자료구조)
                    
print(pick_and_sum("The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog"))
```

    3635
    


```python
# 해당 코드를 통해 올바른 결과가 나오는지 확인하세요.
print(pick_and_sum("The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog1"))
```

### map 연습
   1. 내가 정의한 함수를 적용시키기 
   


```python
# 각각 숫자에 2를 더한 값을 넣어보세요 . 

def add_two(num):
    return num+2 

num = [1,2,3,4,5,6]

        # 1. for를 써서 순회하며 새로운 리스트를 만들기 
# sum=[]
# for i in num:
#     sum.append(add_two(i))
# print(sum)

        # 2. list comprehension을 사용하기
# print([add_two(x) for x in num])
    
        # 3. map 사용하기 
print(set(map(add_two,num)))
```

    {3, 4, 5, 6, 7, 8}
    


```python

```


```python

```
