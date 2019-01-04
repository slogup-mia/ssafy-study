#  Self_study_1

###  a = int(input("숫자입력하세요: "))

* '숫자입력하세요'입력칸에 숫자(int)를 입력받아 a라는 변수로 쓰겠다

  ```
  num = int(input("숫자를 입력하세요 : "))
  print("짝수입니다")if num%2==0 else print("홀수입니다.")
  ```

###  a,b,c = map(int,input())

* 입력칸에 문자를 입력받아 a,b,c라는 변수로 쓰겠다 한꺼번에 

  ```
  fir,sec,thir,last = map(str,input().split())
  sec_i= sec[0]
  thir_i=thir[0]
  print(fir+" "+sec_i+'.'+thir_i+'. '+last)
  ```

### b = input()

- 입력칸에 문자를 입력받아 b라는 변수로 쓰겠다

  ```
  name=input()
  print("hello"+ name)
  ```


###  r.append(i)   

* i 값을 r 이라는 [리스트] 안에 넣겠다. 

  ```
  result = []
  for i in range(1,300):
    if i%5==0:
    	result.append(i)    #[5,10,...] 
  print(sum(result))
  ```

### li = b.split()

- b라는 문자열을 li라는 [리스트]에 띄어쓰기 기준으로 잘라 넣겠다.

  ```
  name=input()
  names= name.split()
  ```

### len(li)

-  li라는 [리스트]의 요소갯수 

  ```
  name=input()
  names=name.split()
  for i in range(1,len(names)-1):
      names[i]=names[i][0]+'.'			
  print(' '.join(names))
  ```

### format(a,'.2f')

-  a라는 문자열을 소수점 둘째자리까지 확장 또는 끊기  

  ```
  a,b=map(int,input().split())
  tri= format(a*b/2,'.2f')
  print(tri)
  ```

  ```
  a=2.3
  format(a,'.2f')
  #out
  2.30
  ```

### round(a,2)

* 소수점 둘째자리 전에 끝나는 a라는 문자열 생성

  ```
  a=2.342627457
  round(a,2)
  
  #out
  2.34
  ```

  ```
  a=2.3
  round(a,2)
  
  #out 
  2.3
  ```


###  print(a,end=" ")

### print(a,end="/ ")

* a요소들을 프린트할때 줄바꾸지 않고 " (공백)"으로 분리 하겠다

* / 으로 분리하겠다 

  ```
  a=4
  for a in range(1,a+1):
      print(a,end=" ")  
      print(a,end="/")
  #out
  1 2 3 4 
  1/2/3/4/
  ```
