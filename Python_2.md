#  Python_2



##  I. 조건문

###  1. 조건문 문법

1)  `if` 문은 반드시 일정한 참/거짓을 판단할 수 있는 `조건식`과 함께 사용이 되어야한다. `if <조건식>:`

2-1)  `<조건식>`이 참인 경우 `:` 이후의 문장을 수행한다.

2-2)  `<조건식>`이 거짓인 경우 `else:` 이후의 문장을 수행한다.

- 이때 반드시 **들여쓰기를** 유의해야한다. 파이썬에서는 코드 블록을 자바나 C언어의 `{}`와 달리 `들여쓰기`로 판단하기 때문이다.

- 앞으로 우리는 `PEP-8`에서 권장하는 `4spaces`를 사용할 것이다.

  ``` py
  #조건문에서 아무것도 하지않고 넘어가기 'pass'
  
  pocket =['money','paper']
  
  if 'money' in pocket:
  	pass 
  else:
  	print('카드를 꺼내라')
  ```

  ```
  #택시를 타려면 현금 4000이상 또는 카드가 있어야 한다.  
  
  card = False
  money = 5000 
  
  if money>=4000 or card :
  	print('take a taxi')
  else:
  	print('you can\'t take a taxi')
  ```


###  2. 복수 조건문

2개 이상의 조건문을 활용할 경우 `elif <조건식>:`을 활용한다.

``` py
if dust>150:
	print("매우나쁨")
elif<조건식>:
	print("나쁨")
elif<조건식>:
	print("보통")
else:
	print("보통")
```

```
# 실습!
score = int(input("점수를 입력하세요 : "))
if score >= 90:
    print("A")
elif score >=80:
    print("B")
elif score >=70:
    print("C")
elif score >=60:
    print("D")
else:
    print("F")
```

####  중첩조건문

```py
# 실습!  95점 이상이면, "참잘했어요"를 함께 출력해주세요
score = 95
if score >= 90:
    if score >=95:
        print("A"+"\n"+"참잘했어요")
    else:
        print("A")
elif score >=80:
    print("B")
elif score >=70:
    print("C")
elif score >=60:
    print("D")
else:
    print("F")
```



```
# 연필:1000원, 펜:2000원, 10,000원 이상 구입시 10% 할인
# 연필과 펜의 수 입력받고 할인율 적용하여 최종 구입 금액 출력

c_pcil = int(input("연필갯수 : "))
c_pen = int(input("펜갯수: "))

p_pcil = c_pcil*1000
p_pen = c_pen*2000 

if p_pcil+p_pen >= 10000:
    print(p_pcil+p_pen*0.9)
else:
    print(p_pcil+p_pen)
```

### 3. 조건 표현식

​	**true_value if <조건식> else false_value**

- 표현식은 보통 조건에 따라 값을 정할 때 많이 활용된다.

``` 
a = int (input("숫자를 입력하세요: "))
print("3이 맞음") if a == 3 else ptint("3이 아님")
```

```
# 아래의 코드는 무엇을 위한 코드일까요?
num = int(input("숫자를 입력하세요 : "))
value = num if num >= 0 else 0
print(value)
```

```
# 위의 코드와 동일한 코드입니다.

if num >=0:
    num = num 
else:
    num = 0 

print(mun)

```

```
# 다음의 코드와 동일한 조건 표현식을 작성해보세요.
num = 2
if num % 2:
    result = '홀수입니다.'
else:
    result = '짝수입니다.'
print(result)
```

```
# 여기에 코드를 작성하세요.
num = int(input("숫자를 입력하세요 : "))
print("짝수입니다")if num%2==0 else print("홀수입니다.")
```

```
#표준입력으로 나이 입력.현재 교통카드엔 9000원이 있음. 
#시내버스 요금에 맞게 요금을 차감한 뒤 출력.
#청소년1500, 성인2000 

age=int(input("나이: "))
teen=1500
adu=2000
card=9000

if age>=19:
    card = card-adu
else:
    card = card-teen

result= card
print(result)

```





##  II. 반복문

###  1. while 문

###  2. for 문

​	`for`문은 정해진 범위 내(시퀀스)에서 순차적으로 코드를 실행합니다.

​	`for`문은 `sequence`를 순차적으로 **variable**에 값을 바인딩하며, 코드 블록을 시행합니다.

```
# 1~ 100 숫자 출력하면서 2의 배수일 떄는 'FIzz', 11의 배수일때는 'Buzz', 공배수일때는 'Fizzbuzz'출력
#내 답

i = 0
while i <=100:
    i = i+1 
    if i%2==0 and i%11==0:
        print("FizzBuzz")
    elif i%2==0 not i%11==0:
        print("Fizz")
    elif i%11==0 not i%2==0:
        print("Buzz")
    else:
        pass
print(i)

```

```
#선생님 답

for i in range(1,101):
    if i%2==0 and i%11==0:
        print("FizzBuzz")
    elif i%2==0 not
        print("Fizz")
    elif i%11==0 not
        print("Buzz")
    else:
    	print(i)
```

```
# 세 정수 A,B,C중 두번째로 큰 정 수 출력 
# 내답

A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))

if A > B and A > C:
    if B > C:
        print(B)
    else:
        print(C)
elif  B > A and B > C:
    if A > C:
        print(A)
    else:
        print(C)
elif  C > A and C > B:
    if B > A:
        print(B)
    else:
        print(A)
```

```
#선생님답
a,b,c = map(int,input().split())

if((a>=b and b>=c) or (c>=b and b>=a)):
    print(b)
elif((b>=c and c>=a) or (a>=c and c>=b )):
    print(c)
else:
    print(a)
```

```
dol,yen,eur,we = map(int,input().split())


```

```
amount = user_in[0]
currency 
```

```
#영어이름을 받아 미들네임을 축약해서 나타내는 코드 작성
#Alice Betty Catherine David -> Alice B.C. David 
#내 답

fir,sec,thir,last = map(str,input().split())

sec_i= sec[0]
thir_i=thir[0]

print(fir+" "+sec_i+'.'+thir_i+'. '+last)
```

```
#선생님 답 

name=input()
names= name.split()
for i in range(1,len(names)-1):
	print(names[i])
	names[i] =names[1][0]+'.'
print(''.join(names))
```

```
#실습문제0 
#1부터 1000까지의 자연수 중 5의 배수에 해당되는 자연수들의 총합을 구하세요.

sum = 0
for i in range(1,1001):
    if i % 5 == 0:
        sum= sum+i      # sum += i
print(sum)
    
```

```
#선생님의 또다른 답

result = []

for I in range(1,1001):
	if i%5==0;
		result.append(i)    #[5,10,...]
print(sum(result))
```

```
# 반복문과 조건문만 활용하여 1~30까지 숫자 중에 홀수만 담긴 리스트를 만드세요
list_odd=[]
for i in range(1,31):
    if i % 2==1:
        list_odd.append(i)
print(list_odd)
```

```
# n이 입력으로 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하세요.
n=int(input())
sum=0 
for i in range(1,n+1):
     sum+=i 
print(sum)    
```

```
#1부터 100까지 자연수 모두 더해 출력
sum=0
for i in range(1,101):
    sum+=i
print(sum)
```

```
#선생님 답
result = 0 
i = 1
while i <=100:
	result+=i
	i+=1
print(result)
```



```
#1부터 1000까지 자연수 중 3의 배수의 합 
sum=0
for i in range(1,1001):
    if i % 3 == 0:
        sum+=i
print(sum)
```

```
#선생님 답
result = 0 
i = 1
while i <=1000:
	if i %3 ==0:
		result+=i
	i+=1
	
print(result)
```

```
# 역삼각형의 asrterisk를 출력하는 코드 작성, while문 이용
# 다시풀기

ast=8
for i in range(0,8):
    ast-=i
    print(" "*i + "*"*ast)
    
    
*******
.*****
..***
...*





ast=8
for i in range(1,8):
    ast-=i
    print(" "*i +"*"*ast+"\n")
```

```
#선생님의 답 

star =7
space =0

while star > 0:
	if star>0:
		print(''*space+'*'*star)
	star -=2
	space +=1
    
 #while문 break 
while true:
	if star>0:
		print(''*space+'*'*star)
	star -=2
	space +=1
	if star <=0
		break

```

```
#0~73숫자중3으로 끝나는 숫자만 출력
#다시풀기 

li=[]
for i in range(1,74):
    li.append(i)
for a in li:
    if str(a)[-1] == '3':
        print(a)
```

```
#0~73숫자중3으로 끝나는 숫자만 출력
#다시풀기

for i in range(1,74):
    if i%10 ==3:
        print(i)
```

```
# 한잔에 300원인 커피 10개를 팔수 있는 자판기 코드 
# 내답


price= 300

while i<=10:
    get=int(input())
    i -= get
    print("가격:"+ price*get)
    print("남은 커피:"+i)
    if i < get:
        print("커피가"+i+"잔 뿐입니다")
    elif i<=0:
        print("판매종료")
```

```
#선생님답

coffee =10

while true:
    money = int(input("돈을 넣어주세요: "))
    
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffe-1
    elif money >300:
        print("거스름돈 %d를 주고 커피를 줍니다.")%(money-300))
        coffee = coffee-1 
    else:
        print("")
    ...
    ...
   #사진 참고 
```

```
#구구단

for i in range(2,10):
	for a in range(2,10):
		print(i *a )
```

```
# 표준 입력으로 삼각형의 높이가 입력됩니다. 입력된 높이만큼 산 모양으로 별을 출력하는 프로그램을 만드세요. 모양이 같더라도 공백이나 빈 줄이 더 들어가면 틀린 것으로 처리됩니다.    
...*
..***
.*****
*******


```







####  	1) index와 함께 for문 활용하기 

​	`enumerate()`를 활용하면, 추가적인 변수를 활용할 수 있다.

```
#in
lunch = ["자장면","초밥"]
for idx, menu in enumerate(lunch):
    print(idx,menu)
    
#out
0 자장면
1 초밥
```

```
#in
classroom = ["kim","Jung","choi"]
list(enumerate(classroom))

#out
[(0, 'kim'), (1, 'Jung'), (2, 'choi')]
```

```
#in: 1부터 시작하는 리스트를 만들어달라
classroom = ["kim","Jung","choi"]
list(enumerate(classroom,start=1))

#out
[(1, 'kim'), (2, 'Jung'), (3, 'choi')]
```

```
#colors = ['Apple', 'Banana', 'Coconut', 'Deli', 'Ele', 'Grape'] 다음 리스트에서 0번째 4번째 5번째 요소를 지운 새로운 리스트를 생성하시오.


colors = ['Apple', 'Banana', 'Coconut', 'Deli', 'Ele', 'Grape'] 
fruit = [color for (a,color) in enumerate(colors) if a not in (0,4,5)]
print(fruit)

```





```
#50점 이상의 점수들의 총합. for문 이용
#선생님의 답

scores=[20,55,67,82,45,33,90,87,100,25]
sum=0 
for i in scores:
    if i >= 50:
        sum+= i
print(sum)

```

```
#50점 이상의 점수들의 총합. while문 이용
#선생님의 답

scores=[20,55,67,82,45,33,90,87,100,25]

result = 0 
while scores:
    picker = scores.pop()
    if picker >=50:
        result+=picker
print(result)
```



####  	2) dictionary 반복문 활용하기

* dictionary에서 `for` 활용하는 4가지 방법

  ```
  # 0. dictionary (key 반복)
  for key in dict:
      print(key)
  
  # 1. key 반복
  for key in dict.keys():
      print(key)
  
  # 2. value 반복    
  for val in dict.values():
      print(val)
  
  # 3. key와 value 반복
  for key, val in dict.items():
      print(key, val)
  ```

  실습 : classroom = {"teacher": "Kim", "student1": "Hong", "student2": "Kang"}

  ```
  #in 
  cr = {"teacher": "Kim", "student1": "Hong", "student2": "Kang"}
  for key in cr:
      print(key)
      
  #out
  teacher
  student1
  student2
  ```

  ```
  #in
  #out
  ```

  ```
  #in
  #out
  ```

  ```
  #in
  #out
  ```




###  3. 'break','continue','else'

####  	1) break 

​	`break`문은 반복문을 종료하는 표현입니다.

```
#in 
for i in range(10):
    if i !=0:
        break
    print(i)
#out
0
```

```
# 3이 있을 경우 True를 print하고, 아닐 경우 False를 print
# numbers = [1, 5, 10]
# 내답 (오답)

for num in enumerate(numbers):
    if numbers == 3:
        print("true")
    else:
        print("False")
    break
```

```
# 3이 있을 경우 True를 print하고, 아닐 경우 False를 print
# numbers = [1, 5, 10]
# 선생님답

result= False 
for num in enumerate(numbers):
    if numbers == 3:
        result=True 
        break
print(result)
```



####  	2) continue

​	`continue`문은 continue 이후의 코드를 수행하지 않고 다음 요소를 선택해 반복을 계속 수행합니다.



####  	3)else

​	`else`문은 끝까지 반복문을 시행한 이후에 실행됩니다.

​	(`break`를 통해 중간에 종료되지 않은 경우만 실행)

```
#in 
for i in range(4):
    if i ==3:
        print(f'{i}에서break')
        break
    else:
        print('break 시행안됨')
#out 
break 시행안됨
break 시행안됨
break 시행안됨
3에서break
```

1번 

```
#내답,확인하기

r2=0
r1=0
for m in range(1,101):
    m=m**2
    r1+=m
for n in range(1,101):
    r2+=n
print(r1-r2)

```

2번

```
#선생님답
samples = ['level', 'asdwe', 's', 'abceda', 'gsdwrtfg']
words=[]

for i in samples:
	if len(i)>=2 and i[0]== i[-1]:
		words.append(i)
print(len(words))
```

3번

```
#선생님답 
items = [10,20,40,20,10,30,50,60,40,80,50,40,20,30,10] 
number = []

for i in items:
	if i not in number:
		number.append(i)
print(number)



items = [10,20,40,20,10,30,50,60,40,80,50,40,20,30,10] 
number = items[0]

for i in items:
	if i not in number:
		number.append(i)
	print(number)

```

4번 

```
#선생님 답
fruit=[]

for color in colors:
	if colors.index(color) not in(0,4,5):
		fruit.append(color)
print(fruit)

#선생님 답
delete_index =[0,4,5]
fruit = []

for i in range(0,len(colors)):
	if i not in delete_index:
		fruit.append(color[i])
print(fruit)
```

5번

```

```

6번

```
숙제ㅔㅔ에에에


```



