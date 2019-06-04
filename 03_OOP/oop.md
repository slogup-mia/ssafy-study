
##  시작하기전에

<wikipedia - 객체지향 프로그래밍> 
>
> 객체 지향 프로그래밍(영어: Object-Oriented Programming, OOP)은 컴퓨터 프 로그래밍의 패러다임의 하나이다. 객체 지향 프로그래밍은 컴퓨터 프로그램을 명령어의 목록으로 보는 시각에서 벗어나 여러 개의 독립된 단위, 즉 "객체"들의 모임으로 파악하고자 하는 것이다. 각각의 객체는 메시지를 주고받고, 데이터를 처리할 수 있다.
>
> 명령형 프로그래밍인 절차지향 프로그래밍에서 발전된 형태를 나타내며, 기본 구성요소는 다음과 같다.

* 클래스(Class) - 같은 종류(또는 문제 해결을 위한)의 집단에 속하는 속성(attribute)과 행위(behavior)를 정의한 것으로 객체지향 프로그램의 기본적인 사용자 정의 데이터형(user define data type)이라고 할 수 있다. 클래스는 프로그래머가 아니지만 해결해야 할 문제가 속하는 영역에 종사하는 사람이라면 사용할 수 있고, 다른 클래스 또는 외부 요소와 독립적으로 디자인하여야 한다.


* 인스턴스 - 클래스의 인스턴스(실제로 메모리상에 할당된 것)이다. 객체는 자신 고유의 속성(attribute)을 가지며 클래스에서 정의한 행위(behavior)를 수행할 수 있다. 객체의 행위는 클래스에 정의된 행위에 대한 정의를 공유함으로써 메모리를 경제적으로 사용한다.


* 메서드(Method) - 클래스로부터 생성된 객체를 사용하는 방법으로서 객체에 명령을 내리는 것이라 할 수 있다. 메서드는 한 객체의 속성을 조작하는 데 사용된다.


```python
app.run()     # 주어.동사()로 이해하면 편하다
turtle.Turtle()
```


```python
# 복소수를 하나 만들어보고, 타입을 출력해봅시다.
#복소수 : 실수 +허수부 

a = 3+4j
print(type(a))
```

    <class 'complex'>



```python
# 허수부랑 실수부를 함께 출력해봅시다.
complex_number = a 
print(complex_number.real, complex_number.imag)
```

    3.0 4.0



```python
# 리스트를 하나 만들고 정렬해봅시다.
a=[1,5,2]
a.sort()
print(a)
```

    [1, 2, 5]



```python
# 리스트가 할 수 있는 것들을 알아봅시다.
print(dir(a))
```

    ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

### 실습 문제

> 프로그래밍으로 나와 친구의 이름을 저장해보세요.
>

**각자의 명함과 지갑을 만들어봅시다.**

* 내 생일, 전화번호, 이메일주소 정보를 담은 변수를 확인해봅시다.

* 주머니(pocket)에는 돈(won)을 포함하여 현재 가지고 있는 것을 작성해보세요.

* 나는 인사를 하면서 내 명함에 있는 정보 하나를 이야기합니다. `greeting` 함수를 만듭시다.

* 나는 주머니에 원하는 것과 갯수를 지정하여 넣을 수 있습니다. 

  기존에 값이 있으면, 갯수를 추가하고 없으면 새로 만드는 `in_my_pocket` 함수를 만듭시다.
  

**친구의 정보와 지갑도 만들어봅시다.**


```python
# 아래에 자유롭게 코드를 작성해보세요.
my_name ="Soowon Jung"
ur_name ="chanmi Jung"
my_bir ="0609"
ur_bir="0101"

my_pocket = {"won":500, "card":["woori","hyundai"],"otp":1}
ur_pocket = {"won":10000, "card":["shinhan","kookmin"]}

```


```python
# in_my_pocket 함수를 통해 내 주머니에 내용을 추가해봅시다.

def in_my_pocket(name, pocket, stuff, count):
    if pocket.get(stuff):
        pocket[stuff] += count
    else:
        pocket[stuff] = count
    return pocket 


print(in_my_pocket("Soowon Jung",my_pocket,"won",500))
print(in_my_pocket("Soowon Jung",my_pocket,"otp",2))


    
```

    {'won': 1000, 'card': ['woori', 'hyundai'], 'otp': 1}
    {'won': 1000, 'card': ['woori', 'hyundai'], 'otp': 3}



```python
# greeting 함수를 통해 인사를 해봅시다.
def greeting(name,bday):
    #print("안녕,{name}야, 생일은 {bday}이구나. 반갑다.".format(name,ur_bir))
    print(f"안녕,{name}야, 생일은 {bday}이구나. 반갑다.")

greeting("chanmi Jung","0101")
```

    안녕,chanmi Jung야, 생일은 0101이구나. 반갑다.


## 클래스 및 인스턴스

###  클래스 객체

```python
class ClassName:
    
```

* 선언과 동시에 클래스 객체가 생성됨.

* 또한, 선언된 공간은 지역 스코프로 사용된다.

* 정의된 어트리뷰트 중 변수는 멤버 변수로 불리운다.

* 정의된 함수(`def`)는 메서드로 불리운다.


```python
# name = 'john'
# age = '34'


class TestClass:
    """Test Class 입니다."""
    
```


```python
print(type(TestClass))    #가장 상위 단계에 있는 클래스의 타입은 '타입'이다
```

    <class 'type'>


* 선언시 self는 반드시 작성해주세요! 나중에 설명드립니다.

### 인스턴스 객체

* 인스턴스 객체는 `ClassName()`을 호출함으로써 선언된다.

* 인스턴스 객체와 클래스 객체는 서로 다른 이름 공간을 가지고 있다.

* 인스턴스 -> 클래스 -> 전역 순으로 탐색을 한다.


```python
# 클래스 Person의 iu라는 인스턴스(오브젝트)를 만들어봅시다.
#오브젝트 중심으로 짜는 코드이기 때문에, oop인거시다 
class Person:
    name = 'Guildong Hong'    #클래스는 단순히 생각하면 '코드들의 묶음'
    def hello(self):   #클래스 안에 들어가는 인자에는 항상 self가 들어가야 한다.
        print(f'hello, {self.name}')
    
iu = Person()   #여기에 정의된 모든 속성들이 포함된 객체가 만들어진다.음? 
#아이유라는 사람 하나를 만들겠다. 
iu.hello()

#결과out을 보면 hello,+고정된name이 출력되는 것을 알수있다. 잘못!!  
#아래에 고쳐본다. 
```

    hello, Guildong Hong



```python
# 클래스 Person의 iu라는 인스턴스(오브젝트)를 만들어봅시다. 
class Person:
    def __init__(self,input_name):   #init : initialize의 줄임 
        self. name = input_name     #파이썬에서는 self 대신 me 를 써도 가능한데, 일반적으로 self쓴다.
        #name과 input_name의 역할과 불려오는 인자를 구분하자
        
    def hello(self): 
        print(f'hello, I am {self.name}')
    
iu = Person('iu')   
iu.hello()
```

    hello, I am iu



```python
# 클래스 Person의 iu라는 인스턴스(오브젝트)를 만들어봅시다.
class Person:
    def __init__(me, input_name, age, is_female):  
        me. name = input_name 
        me.age = age
        me.is_female = is_female 
        #attribute,어트리뷰트, 속성
        
    def hello(me): 
        print(f'  hello, I am {me.name}.')
        print(f'{me.age}years old',)
        print(f'and I am a woman' if me.is_female else 'and I am a man')
        #method,메소드, 행동
    
iu = Person('IU',27,True)   
iu.hello()
john = Person('John',40,False)   
john.hello()


#john.age에 들어가있는 데이터 : 속성,attribute = 
#john.hello에 들어가있는 데이터 : 행동, method =클래스안에 정의될때, 클래스를 조작하는,인스턴스를 활용할 수 있는. 
```

      hello, I am IU.
    27years old
    and I am a woman
      hello, I am John.
    40years old
    and I am a man


총평,다시: 
- 예전에는 절차적인 프로그래밍, 이거일땐 이렇게 저거일때 저렇게.=> 사람이 알아볼수없다.
- 인지구조와 비슷하게 만들기 시작했다. 의식의 흐름대로 보다보니 공통적인 부분이 있음 
- 위의 예시대로, 사람이라면 이름이있고 성별 나이가 있다. => 분류하기 시작했다.
- 개념이라는 것을 만들때, 분류하여 인지하는 상식적인 과정으로 프로그래밍하자!
- 산발되어있는 정보를 분류하는것이 oop의 시작이고, 가장먼저가 class라는 묶음으로 분류하는 것. 
- 분류 => 속성의 나열, 이때 속성이 attribute 
- ex) 인간이라함은 속성(어트리뷰트)을가지고 행동(메소드)을 한다.
- 인간 아이유, 존, 정수원은 class의 예인데, 이 세사람은 모두 예로서 인스턴스(객체,오브젝트)이다. 세사람은 모두 다른 속성과 메소드를 가지고 있다. 

- 파이썬의 oop는 class 하위로 들어가면서 계층화해서 쓰게끔 만든다. 
- ********************************************
- self : 내 객체의 정보를 첫번쨰 인자로 넘겨준다. 
- __init__ : 생성자 함수이다. 
- Person('IU',27,True)를 만났을때 Person이라는 class 를 실행하는 애가 __init__ 이다. 
- 메소드는 해당 클래스 안에서 정의가 되어야해 
- 바깥에서 정의된 함수는 이 함수 안에서는 돌릴 수 없ㅓ어어어어어어어엉엉
- ******************************************
- 파이썬에서 생성자 함수를 쓰는 이유 : class 를 객체지향적으로 만들기 위해 (역사적인 설계과정에서는 oop가 아니었으므로 class개념을 이후에 적용)
- 어트리뷰트와 메소드는 모든 인스턴스가 공유하고 있다. 
- 
- ******************************************
- 


```python
class Person:
    dna= 46
    def __init__(me, input_name, age, is_female, dna=None):  
                               #dna = None /dna를 생성자 함수안에 넣을때 
        me. name = input_name 
        me.age = age
        me.is_female = is_female 
        if dna == not None:   # dna를 생성자 함수안에 넣을때 
            me.dna = dna      # dna를 생성자 함수안에 넣을때 
        
    def hello(me): 
        print(f'  hello, I am {me.name}.')
        print(f'{me.age}years old',)
        print(f'and I am a woman' if me.is_female else 'and I am a man')
        print(f'my dna is {me.dna}'
    
john = Person('John',40,False)   
john.hello()

```

      hello, I am John.
    40years old
    and I am a man
    my dna is 46





```python
# 인사하는 메서드를 호출해봅시다.

```


```python
# iu의 이름을 확인해봅시다.

```


```python
# iu로 이름을 바꿔주세요.
```


```python
# iu가 인사를 합니다.

```


```python
# iu와 Person이 같은지 확인해보겠습니다.

```


```python
# iu와 Person이 같은지 확인해보겠습니다.

```


```python
# iu를 출력해봅시다.

```


```python
# iu를 출력해봅시다 2.

```


```python
# type을 확인해봅시다.
print(type(iu))

print(type(1))
print(type("글자"))
# class int    파이썬안에 int라는 class가 존재한다 
# class str    파이썬안에 str라는 class가 존재한다

print(iu)     #<__main__.Person object at 0x0189C0B0> 건조하게 출력 
```

    <class '__main__.Person'>
    <class 'int'>
    <class 'str'>
    <__main__.Person object at 0x0189C0B0>



```python
class Person:
    def __init__(me, input_name, age, is_female):  
        me. name = input_name 
        me.age = age
        me.is_female = is_female   
        
    def __repr__(self):
        return f"Person class의 instance인 {self.name}입니다" 
        
    def hello(me): 
        print(f'  hello, I am {me.name}.')
        print(f'{me.age}years old',)
        print(f'and I am a woman' if me.is_female else 'and I am a man')
        print(f'my dna is {me.dna}'
    
```


      File "<ipython-input-36-68dbd91c41c3>", line 15
        
        ^
    SyntaxError: unexpected EOF while parsing




```python
#print(iu)     #<__main__.Person object at 0x0189C0B0> 건조하게 출력 됐던게 
#    def __repr__(self):
#        return f"Person class의 instance인 {self.name}입니다" 
#위의 코드로 인해 

print(iu)     #예쁘게 출력된다. 
```

* 파이썬 출력의 비밀 : repr, str


```python
class Person:
    name = '홍길동'
    def sayhello(self):
        print(f'hello, {self.name}')
    
    # repr 호출시 없으면 호출 x : for 개발자 (객체 인식 공식 문자)
    # 주피터 노트북으로 [1, 2, 3] 블록을 실행하면 나오는 것
    
    # str 호출시 없으면 repr 호출 : for 사용자
    # print() 호출시 나오는 것
    
    def __repr__(self):
        return f'<Person object: {self.name}>'
    
    def __str__(self):
        return f'Person\n 이름 : {self.name}'
```




```python
# 강다니엘을 만들어봅시다.

```


```python
# 강다니엘을 출력해봅시다.
```


```python
# 강다니엘을 출력해봅시다. 2
```

### 실습 문제 발전

> 지금까지 배운 것을 통해서 Person 클래스를 만들고, 친구와 나를 표현해봅시다.
>
> 이름과 주머니의 정보를 가지고 있고 (멤버 변수==속성, 어트리뷰트)
> 
> 인사(`greeting()`)와 주머니에 내용을 추가(`in_my_pocket()`)할 수 있습니다. (메서드)
>
> 추가적으로 `get_my_pocket()`으로 지갑에 담긴 정보를 가져와 봅시다.
>
> 그리고 사람을 출력하면, 지갑을 제외한 정보를 보여주세요. 


```python
# 아래에 코드를 작성해주세요.    
class Person: 
    def __init__(self,name):   #여기에 왜 ,wallet이 안들어가지??? 
        self.name = name
        self.wallet = {}
        #key : 물건, value: 개수  
    
    def greeting(self):
        print(f'안녕하세요 ,저는 {self.name}입니다.')
              
    def in_my_pocket(self,thing):
        if self.wallet.get(thing):
            self.wallet[thing] += 1 
        else:
            self.wallet[thing] = 1
        #만약 물건이 있었다면, 개수를 하나 올려주고,
        #없었다면 물건을 추가하고 개수를 1로 해준다. 
              
    def get_my_pocket(self):
        return self.wallet 
```


```python
# 나를 만들어 봅시다.
john = Person("John")
john.greeting()
```

    안녕하세요 ,저는 John입니다.



```python
# greeting, in_my_pocket, get_my_pocket
john.in_my_pocket('신용카드')
john.in_my_pocket('5만원지페')
john.get_my_pocket()

```




    {'신용카드': 2, '5만원지페': 2}



## MyList만들기

> 이제 배운 것을 활용하여 나만의 리스트 객체를 만들 수 있습니다. 
>
> `class MyList:`
>

```
* 멤버변수, 속성, 어트리뷰트
data : 비어 있는 리스트

* 메서드 
append : 값을 받아 추가합니다.
pop : 마지막에 있는 값을 없애고, 해당 값을 리턴합니다.
reverse : 제자리에서 뒤집고 리턴 값은 없습니다.
count(x) : x의 갯수를 반환합니다.
clear : 값을 모두 삭제합니다.

__repr__ : ex) '리스트 내용 1, 2, 3'
```

- 리스트를 클래스 수준에서 만들 수 있다. 
- 리스트의 커스터마이징화 
- 크게 다른건 없다. 다만 위처럼 __repr__를 사용하여 출력을 이쁘게 할 수 있다. 


```python
# 아래에 코드를 작성해주세요.

class MyList:
    data = []
    
    def append(self,value):
        self.data.append(value)
        
    def pop(self,value):
        return self.data.pop(value)
        
    def reverse(self):
        self.data = reversed(self.data)
        #self.data.reverse 가능
    
    def count(self,value):
        return self.data.count(value)
    
    def clear(self):
        self.data=[]
        
    def __repr__(self):
        cont = ', '.join(map(str,self.data))#join 안에는 스트링이 들어가야 한다. 
        #cont = ', '.join(str(x) for x in self.data) 도 가능  
        return f"리스트 내용 {cont}"
        
myNewList = MyList()

```


```python
myNewList.append(3)
myNewList.append(3)
myNewList.append(3)
myNewList.append(5)
myNewList.append(4)
myNewList.pop(3)
print(myNewList)
```

    리스트 내용 3, 3, 3, 4


### 자유롭게 만들어보기

> 이 세상에 있는 무엇인가를 자유롭게 표현해주세요.


```python
# 아래에 코드를 작성해주세요.
a=[3,2,1]
reverse()
```


    ---------------------------------------------------------------------------
    
    NameError                                 Traceback (most recent call last)
    
    <ipython-input-44-c5c4500b0a1d> in <module>
          1 # 아래에 코드를 작성해주세요.
          2 a=[3,2,1]
    ----> 3 reverse()


    NameError: name 'reverse' is not defined



```python

```

