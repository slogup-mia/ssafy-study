

```python
from IPython.display import IFrame
```

# OOP with Python

## 용어 정리

```python
class Person:                      #=> 클래스 정의(선언) : 클래스 객체 생성
    name = '홍길동'                  #=> 멤버 변수(데이터 어트리뷰트)
    def greeting(self):            #=> 멤버 메서드(메서드)
        print(f'{self.name}')
```
    
    
```python
iu = Person()       # 인스턴스 객체 생성
daniel = Person()   # 인스턴스 객체 생성
iu.name             # 데이터 어트리뷰트 호출
iu.greeting()       # 메서드 호출
```


```python
class Person:                   
    name = '홍길동' 
    
    def greeting(self):         
        print(f'{self.name}')

iu = Person()
iu.greeting()
iu.name
```

    홍길동
    




    '홍길동'




```python
class Person:                   
    name = '홍길동'    # 모든 객채가 같은 내용으로 공유해야할 정보
    def __init__(self, input_name):
        self.name2 = input_name #각각의 객체가 가지는 정보를 넣는다. 
        
    def greeting(self):         
        print(f'{self.name}')

        
iu = Person('iu')
suzi = Person('suzi')
rm = Person('rm')
print(iu.name)
print(suzi.name)
print(rm.name)
print(Person.name)

print(iu.name2)
print(suzi.name2)
print(rm.name2)
```

    홍길동
    홍길동
    홍길동
    홍길동
    iu
    suzi
    rm
    


```python
class Person:                   
    number_of_people = 0    # 모든 객채가 같은 내용으로 공유해야할 정보
                            #사람이 생성될때마다 수를 올리고싶다.
        
    def __init__(self, input_name):
        self.name = input_name #각각의 객체가 가지는 정보를 넣는다. 
        Person. number_of_people += 1   #사람이 생성될때마다 init 이 돌아가므로 여기에 코딩
#얘는 앞에 self. 붙이면 안된다. Person에서 불러오는거니까 Person. 
            
    def greeting(self):         
        print(f'{self.name}')

print(Person.number_of_people)
iu = Person('iu')
print(Person.number_of_people)
suzi = Person('suzi')
print(Person.number_of_people)
        
```

    0
    1
    2
    


* 클래스와 인스턴스간의 관계를 확인해봅시다.


```python
dir(iu)
isinstance(iu,Person)  #iu가 person의 인스턴스니?라고 묻는것
isinstance(iu,int)
```




    False



##  `self` : 인스턴스 객체 자기자신

* C++ 혹은 자바에서의 this 키워드와 동일함. 

* 특별한 상황을 제외하고는 무조건 메서드에서 `self`를 첫번째 인자로 설정한다.

* 메서드는 인스턴스 객체가 함수의 첫번째 인자로 전달되도록 되어있다.


```python
# iu를 다시 인사시켜봅시다.
iu.greeting()
```

    아이유
    


```python
# 다르게 인사를 시킬 수도 있습니다.
# 실제로 이렇게 호출이 되는 것과 동일하기에 반드시 self로서 인스턴스 자기자신을 표현해야합니다.
Person.greeting 
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-7-eca601cb6a90> in <module>
          1 # 이렇게 인사시킬 수도 있습니다.
    ----> 2 Person.greetin(iu)
    

    AttributeError: type object 'Person' has no attribute 'greetin'


* 클래스 선언부 내부에서도 반드시 self를 통해 데이터 어트리뷰트에 접근 해야 합니다.


```python
# 예시를 봅시다.
name = '?'

class Person:
    name = '홍길동'
    
    def greeting(self):
        print(f'{name}')
```


```python

```

    홍길동
    ?
    

## 클래스-인스턴스간의 이름공간

* 클래스를 정의하면, 클래스 객체가 생성되고 해당되는 이름 공간이 생성된다.

* 인스턴스를 만들게 되면, 인스턴스 객체가 생성되고 해당되는 이름 공간이 생성된다.

* 인스턴스의 어트리뷰트가 변경되면, 변경된 데이터를 인스턴스 객체 이름 공간에 저장한다.

* 즉, 인스턴스에서 특정한 어트리뷰트에 접근하게 되면 인스턴스 -> 클래스 순으로 탐색을 한다.

    - '클래스의 내집합 인스턴스' '파이썬의 내집합은 공유안하는 사춘기 막내의 방' 이라고생각하면 쉬움
    - 내집합인 클래스 부터 탐색하지만(우선순위가 있지만) 웬만하면 겹치는 이름을 붙이지 않도록 한다.


```python



```

    아이유
    


```python
# 아래의 Python Tutor를 통해 순차적으로 확인해봅시다.
IFrame('https://goo.gl/ZgNaXB', width='100%', height='300px')
```





        <iframe
            width="100%"
            height="300px"
            src="https://goo.gl/ZgNaXB"
            frameborder="0"
            allowfullscreen
        ></iframe>
        



## 생성자 / 소멸자

* 생성자는 인스턴스 객체가 생성될 때 호출되는 함수이며, 소멸자는 객체가 소멸되는 과정에서 호출되는 함수입니다.

```python
def __init__(self):
    print('생성될 때 자동으로 호출되는 메서드입니다.')
    
def __del__(self):
    print('소멸될 때 자동으로 호출되는 메서드입니다.')
```

```
__someting__
```

위의 형식처럼 양쪽에 언더스코어가 있는 메서드를 스페셜 메서드 혹은 매직 메서드라고 불립니다.


```python
class Person:
    def __init__(self):
        print("응애!")
        
    def __del__(self):
        print("ㅂㅇ")
```


```python
p1 = Person()
```

    응애!
    ㅂㅇ
    


```python
# 소멸시켜봅시다.
del p1
```

    ㅂㅇ
    

* 생성자 역시 메소드이기 때문에 추가적인 인자를 받을 수 있습니다.


```python
# 생성자에서 이름을 추가적으로 받아서 출력해봅시다.
class Person2:
    def __init__(self,name):
        print(f"응애,{name}")
```


```python
# 홍길동이라는 이름을 가진 hong 을 만들어봅시다.
hong = Person2("홍길동")
```

    응애,홍길동
    

* 아래와 같이 모두 사용할 수 있습니다!

```python
def __init__(self, parameter1, parameter2):
    print('생성될 때 자동으로 호출되는 메서드입니다.')
    print(parameter1)

def __init__(self, *args):
    print('생성될 때 자동으로 호출되는 메서드입니다.')

def __init__(self, **kwagrs):
    print('생성될 때 자동으로 호출되는 메서드입니다.')
```

* 따라서, 생성자는 값을 초기화하는 과정에서 자주 활용됩니다. 

* 아래의 클래스 변수와 인스턴스 변수를 통해 확인해보겠습니다.

## 클래스 변수 / 인스턴스 변수

```python
class Person:
    population = 0           # 클래스 변수 : 모든 인스턴스가 공유함.
    
    def __init__(self, name):   
        self.name = name     # 인스턴스 변수 : 인스턴스별로 각각 가지는 변수
```        


```python
# 위의 생성자와 인사하는 메소드를 만들어봅시다. 
class Person3:
    population = 0
    
    def __init__(self,name):
        self.name =name
        Person3.population += 1
```


```python
# 본인의 이름을 가진 인스턴스를 만들어봅시다.
john = Person3('john')
soo = Person3('soo')
```


```python
# 이름을 출력해봅시다.
john.name
soo.name
```




    'soo'




```python
# 옆자리 친구의 이름을 가진 인스턴스를 만들어봅시다.
print(john.population)
```

    2
    


```python
# 이름을 출력해봅시다.

```




    '토마스'




```python
# population을 출력해봅시다.

```




    2




```python
# 물론, 인스턴스도 접근 가능합니다. 왜일까요?!
 # 상속을 지원한 OOP 때문에 
# 이름공간
```




    2



## 정적 메서드 / 클래스 메서드 : 모든 인스턴스가 공유하는 친구 (~=클래스 변수와 비슷)

* 메서드 호출을 인스턴스가 아닌 클래스가 할 수 있도록 구성할 수 있습니다. 

* 이때 활용되는게 정적 메서드 혹은 클래스 메서드입니다.

* 정적 메소드는 객체(인스턴스)가 전달되지 않은 형태이며, 클래스 메서드는 인자로 클래스를 넘겨준다.

* 인스턴스 메서드는 인자로 ★★★인스턴스★★★를 넘겨준다.
* 클래스를 넘겨주면 클래스 메서드 
* 아무것도 넘겨주지 않으면 정적 메서드


## 멤버 메서드 / 인스터스 메서드 : 특정 인스턴스에만 속한 메서드 (~= 인스턴스 변수)




```python
# Person 클래스가 인사할 수 있는지 확인해보겠습니다.
class Person:
    population = 0 
    
    def __init__(self,name):
        self.name = name 
        Person.population += 1
                
    def greeting(self):
        print(f"{self.name}입니다. 안녕하세요")
        
    @staticmethod          # 어차피 전달하는게 없으니 없어도 되는데, 그 차이는 나중에.     
    def info():            #정적메소드는 self로 전달하지 않고 돌리는 정적 메소드
        print("사람입니다.")   # = 클래스의 데이터를 쓰지 않는 순수한 메서드들
        

    @classmethod          # = 클래스의 데이터를 사용하는 메서드들 
    def count(cls):
        print(f"현재 인구수는 {cls.population}명 입니다.")

me = Person("john")
me.greeting()
Person.greeting(me)   # 인스턴스 메서드    #그래서 Person.greeting() 로 돌리면 오류
Person.info()      #정적메서드 출력 

Person.count()    # @클래스메서드 라고 정의내렸기 때문에 Person.count() 로 돌리지않아도 돼 

```

    john입니다. 안녕하세요
    john입니다. 안녕하세요
    사람입니다.
    현재 인구수는 1명 입니다.
    


```python
# 이번에는 Dog class를 만들어보겠습니다.
# 클래스 변수 num_of_dogs 통해 개가 생성될 때마다 증가시키도록 하겠습니다. 
# 개들은 각자의 이름과 나이를 가지고 있습니다. 
# 그리고 bark() 메서드를 통해 짖을 수 있습니다. 자신의 이름과 나이를 함께 짖는다. 

class Dog: 
    num_of_dogs = 0 
    
    def __init__(self,age,name):
        self.age = age
        self.name = name
        Dog.num_of_dogs += 1 
    
    def bark(self):
        print(f"왈! 내왈!이름은왈! {self.name}이왈!")
        print(f"나이는 {self.age}살이오댕댕댕.")
        
    @staticmethod
    def info():
        print("댕댕이요")
        
pup = Dog(3,"댕댕")
pup.bark()
Dog.info()
        
```

    왈! 내왈!이름은왈! 댕댕이왈!
    나이는 3살이오댕댕댕.
    댕댕이요
    


```python
# 각각 이름과 나이가 다른 인스턴스를 3개 만들어봅시다.

```

* staticmethod는 다음과 같이 정의됩니다.

```python

@staticmethod
def methodname():
    codeblock
```


```python
# 단순한 static method를 만들어보겠습니다.

```


```python
# 3마리를 만들어보고,

```


```python

```

    개입니다.
    

* classmethod는 다음과 같이 정의됩니다.

```python

@classmethod
def methodname(cls):
    codeblock
```


```python
# 개의 숫자를 출력하는 classmethod를 만들어보겠습니다.

```


```python
# 3마리를 만들어보고,

```


```python

```

    3마리
    

## 실습문제 - 정적 메소드

> 계산기 class인 `Calculator`를 만들어봅시다.

* 정적 메소드 : 두 수를 받아서 각각의 연산을 한 결과를 반환(return)

    1. `add()` : 덧셈
    
    2. `sub()` : 뺄셈 
    
    3. `mul()` : 곱셈
    
    4. `div()` : 나눗셈



```python
# 아래에 코드를 작성해주세요.
class Calculator:
    @staticmethod
    def add(a,b):
        return a+ b
    def sub(a,b):
        return a- b
    def mul(a,b):
        return a* b
    def div(a,b):
        return a/ b
    
```


```python
Calculator.mul(1,3)


#전혀 클래스, 인스턴스와 상관없는 OOP와 상관없는 함수를 넣을때 정적메서드사용 
```




    3



## 실습문제 - 종합1

> 사실 이전에 작성한 Mylist는 완벽하지 않았습니다. 
>
> 한번 제대로 된 자료구조를 만들어보겠습니다. 
>
> `Stack` 클래스를 간략하게 구현해봅시다.

> [Stack](https://ko.wikipedia.org/wiki/%EC%8A%A4%ED%83%9D) : 스택은 LIFO(Last in First Out)으로 구조화된 자료구조를 뜻합니다.

1. `empty()`: 스택이 비었다면 참을 주고,그렇지 않다면 거짓이 된다.

2. `top()`: 스택의 가장 마지막 데이터를 넘겨준다. 스택이 비었다면 None을 리턴해주세요.

3. `pop()`: 스택의 가장 마지막 데이터의 값을 넘겨주고 해당 데이터를 삭제한다. 스택이 비었다면 None을 리턴해주세요.

4. `push()`: 스택의 가장 마지막 데이터 뒤에 값을 추가한다. 리턴값 없음

**다 완료하신 분들은 __repr__을 통해 예쁘게 출력까지 해봅시다.**


```python
# 여기에 코드를 작성해주세요.
class Stack:
    def __init__(self):
        self.items = []
        
    def empty(self):
        return self.items
    
    def top(self):
        if self.items:
            return self.items[-1]
    
    def pop(self):
        if self.items:
            elem = self.items.pop()
            return elem
    
    def push(self, elem):
        self.items.append(elem)
        
    def __repr__(self):
        return '스택 : ' + ','.join(self.items)
```


```python
# 인스턴스를 하나 만들고 메소드 조작을 해봅시다.
s1 = Stack()
```


```python
s1.push('hi')
```


```python
print(s1)
```

    스택hi
    


```python
s1
```




    스택hi



## 연산자 오버라이딩(중복 정의)

* 파이썬에 기본적으로 정의된 연산자를 직접적으로 정의하여 활용할 수 있습니다.
* = 원래있는 연산에 내 나름의 연산능력을 더 한다 

* 몇가지만 소개하고 활용해봅시다.

```
+  __add__   
-  __sub__
*  __mul__
<  __lt__
<= __le__
== __eq__
!= __ne__
>= __ge__
>  __gt__
```


```python
# 사람과 사람을 같은지 비교하면, 이는 나이가 같은지 비교한 결과를 반환하도록 만들어봅시다.
class Person:
    population = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.population += 1
        
    def greeting(self):
        print(f'{self.name}입니다. 만나서 반가워요')
        
    def __gt__(self, other):
        if self.age > other.age:      #나이기준으로 비교
            return '왼쪽이 나이 더 많아'
        else:
            return '오른쪽이 나이 더 많아'
    
    def __eq__(self, other):
        if self.name == other.name:
            return '이름이 같네요'
        else:
            return '이름이 다르네요'
    
```


```python
# 연산자를 호출해봅시다.
p1 = Person('아저씨', 40)
p2 = Person('애기', 0)

p1 > p2

```




    '왼쪽이 나이 더 많아'




```python
p1 = Person('아저씨', 40)
p2 = Person('아저씨', 0)
p3 = Person('아재', 0)

p1 == p2   # '이름이 같네요'
p2 == p3   # '이름이 다르네요' == Person.__eq__(p2,p3)
```




    '이름이 다르네요'




```python
# 원하는 연산자를 사람과 사람을 비교해보세요.
```


```python
# 파이썬 내부를 살펴봅시다.
print(1 + 3)
print('1' + '3')
# 이렇게 + 연산자가 서로 다르게 활용될 수 있는 이유는 파이썬 내부적으로 각각 다른 클래스마다 다른 정의가 있기 때문입니다.
```

    4
    13
    

# 상속 

## 기초

* 클래스에서 가장 큰 특징은 '상속' 기능을 가지고 있다는 것이다. 

* 부모 클래스의 모든 속성이 자식 클래스에게 상속 되므로 코드재사용성이 높아집니다.

* 


```python
class DerivedClassName(BaseClassName):
    code block
```


```python
# 인사만 할 수 있는 간단한 사람 클래스를 만들어봅시다.
class Person:
    def __init__(self, name):
        self.name = name
        
    def greeting(self):
        print(f'{self.name} 입니다.')
```


```python
# 사람 클래스를 상속받아 학생 클래스를 만들어봅시다.
class Student(Person):         # Person이란 클래스를 마치 인자처럼 받고있다. 바로 이것이 상속. 
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
```


```python
# 학생을 만들어봅시다.
s1 = Student('민교', '12311')
```


```python
# 부모 클래스에 정의를 했음에도 메소드를 호출 할 수 있습니다.
s1.greeting()    #greeting은 (s1이 정의된)학생에 속한 메소드가 아닌데, 오류가 나지 않는이유 
                # : 스튜던트 클래스가 Person 클래스를 상속받기 때문에
```

    민교 입니다.
    

* 이처럼 상속은 공통된 속성이나 메소드를 부모 클래스에 정의하고, 이를 상속받아 다양한 형태의 사람들을 만들 수 있습니다.


```python
# 진짜 상속관계인지 확인해봅시다.
issubclass(Person, Student)
```




    False




```python
issubclass(Student, Person)
```




    True



## super()

* 자식 클래스에 메서드를 추가 구현할 수 있습니다.

* 부모 클래스의 내용을 사용하고자 할 때, `super()`를 사용할 수 있습니다.


```python
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email 
        
    def greeting(self):
        print(f'안녕, {self.name}')
        
class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        self.name = name           ####중복###
        self.age = age             ####중복###
        self.number = number       ####중복###
        self.email = email         ####중복###
        self.student_id = student_id
        
p1 = Person('홍길동', 200, '0101231234', 'hong@gildong')
s1 = Student('학생', 20, '12312312', 'student@naver.com', '190000')
```

* 위의 코드를 보면, 상속을 했음에도 불구하고 동일한 코드가 반복됩니다. 


```python
# 이를 수정해봅시다.
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email 
        
    def greeting(self):
        print(f'안녕, 난 {self.name}')
        
class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        super().__init__(name, age, number, email)     # super(). 대신  person(). 으로 돌려도 무방 
        self.student_id = student_id
        
p1 = Person('홍길동', 200, '0101231234', 'hong@gildong')
s1 = Student('학생', 20, '12312312', 'student@naver.com', '190000')
```

## 메소드 오버라이딩

* 메서드를 재정의할 수도 있습니다.


```python
# 학생은 공손하게 이야기를 해봅시다.

class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        super().__init__(name, age, number, email)
        self.student_id = student_id
        
    def greeting(self):
        print(f'안녕하세요, {self.name}입니다.')
```


```python
s1 = Student('학생', 20, '12312312', 'student@naver.com', '190000')
s1.greeting()
```

    안녕하세요, 학생입니다.
    

## 상속관계에서의 이름공간

* 기존에 인스턴스 -> 클래스순으로 이름 공간을 탐색해나가는 과정에서 상속관계에 있으면 아래와 같이 확장됩니다.

* 인스턴스 -> 자식 클래스 -> 부모 클래스 -> 전역

## 실습1 

> Teacher 클래스를 만들어보고 Student와 Teacher 클래스에 각각 다른 행동의 메소드들을 하나씩 추가해봅시다.


```python
# 아래에 코드를 작성해주세요.
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email 
        
    def greeting(self):
        print(f'안녕, {self.name}')
        
class Teacher(Person):
    def __init__(self,name,age,number,email,teacher_major):
        super().__init__(name,age,number,email)
        self.teacher_major = teacher_major
    
    def greeting(self):
        print(f'반갑습니다, {self.teacher_major} 일타강사 {self.name}입니다.')
        
tea = Teacher('정선생','46','1313','g@g.com','알고리즘')
tea.greeting()

```

    반갑습니다, 알고리즘 일타강사 정선생입니다.
    

#### 다중상속 

- 언어상에서 다중상속은 레퍼런스상 문제가 될 수 있어서 
- 다른언어에서는 막는데, 
- 파이썬은 가능하다. 
- 그러나 파이썬에서도 되도록이면 일직선 상속라인을 유지하는 것이 관례이다.  

- 웬만한 수준에서는 다중상속 받는 일은 없다고 보면 됨 


```python
'''
class Teacher(Person):
    
class Master_Teacher(Teacher, Person):
    
    def __init__(self):
        super.__init__     #이경우는 첫번째 부모인 Teaher을 적용한다. Person 상속을 적용받고 싶다면 : Person.__init__ 
'''
```

## 실습2

> 사실 사람은 포유류입니다. 
>
> Animal Class를 만들고, Person클래스가 상속받도록 구성해봅시다.
>
> 변수나, 메소드는 자유롭게 만들어봅시다.


```python
# 아래에 코드를 작성해주세요.
```
