# python_3_problems_2

### 문제 1

```
def triangle(row):
    dicts ={'GG':'G','BB':'B','RR':'R','BR':'G','BG':'R','GB':'R','GR':'B','RG':'B','RB':'G'}
    if len(row) >2 :
        s =''
        for i in range(len(row)-1):
            s = s +dicts[row[i:i+2]]
        row = s
        return triangle(row)
    elif len(row) > 1:     #lenth=2
        return dicts[row]
    else:
        return row

print(triangle('RRR'))
```

```
def triangle(row):
    if len(row)==1:
        return row[0]
    colors = set(["B","G","R"])
    newrow = []
    for (l,r) in zip(row,row[1:]):
        if l == r:
            newrow.append(l)
        else:
            newrow.extend(colors-set([l,r]))
            
    return triangle(newrow)
print(triangle('RRGBRGBB'))
```





###  문제 2

```
def even_and_odd(arr):
    even =[]
    odd = []
    for i in sorted(set(arr)):  #set자료형은 중복 불허
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
            #print(type(odd))
    return even + odd[::-1]
print(even_and_odd([14,17,2,7,20,3,6,13]))

```



### 문제3 

```
def rout(num_lst):
    result_lst = []
    for i in num_lst:
        if (i**0.5) % 1 == 0:
            result_lst.append(int(i**0.5))
        else:
            result_lst.append(i**2)
    return result_lst

print(rout([1, 2, 3, 4, 9]))
```



###  문제4

```
#내답 

def nums(n):
    if n<=0:
        print("")
    for i in range(1,n+1):
        if i%2==0:
            pass
        else:
            print(str(i)*i)
print(nums(7))    
```

```
#선생님답
#다시보기 

def pattern(n):
    string =""
    a=n
    
    if a %2 ==0: 
        a -= 1
    for x in range (1, a+1):
        if x % 2 != 0:
            string += str(x) * x
            
            if x != a : 
                string += "\n"
    return string

print(pattern(20))
```



### 문제 5

```
#내답 

# 단어 word를 리스트로?받는다. 
# left, right 리스트 생성.
# odd=[], even=[] 
# 만약 word의 홀수 번째 알파벳이 모두 left, 짝수번이 right 에 있거나,
# 홀수 번째 알파벳이 모두 right, 짝수번이 left 에 있다면 

odd=[]
even=[]
def type(word):
    left,right = 'qwertasdfgzxcvb','yuiophjklnm'
    for i in word:
        if word.ord[i]%2 != 0:
            str(i).append(even)
        else:
            str(i).append(odd)
    if odd in left and even in right:
        return True
    elif even in left and odd in right:
        return True
    else:
        return False 
    

print(type('apple'))
print(type('qpwo'))
```



```
# 선생님답
#다시보기 

def cftb_wd(word):
    left,right = 'qwertasdfgzxcvb','yuiophjklnm'
    l= True if word[0] in left else False # l true
    
    for letter in word [1:]: #ywu
        if letter in left and l:
            return False
        if letter in right and not l:
            return False
        l= not l #false
    return True

print(cftb_wd("qywu"))
print(cftb_wd("apple"))
```

