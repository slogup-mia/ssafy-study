#  Python_3_problems_1

###  문제1

hint. 1월1일(금) 부터 a월 b일까지는 몇일일까  =   a월(*각 월 일수)+ b일 

```
#선생님답

def solution(a,b):
    answer = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    month = [31,29,31,30,31,30,31,31,30,31,30,31]   #월별 날짜수

    if a>1:
        for i in range(0,a-1):
            b = b + month[i]
    return answer[b % 7 - 1]

solution(1,2)
```

###  문제2

hint.  ASCII CODE

A 	B	 C 	D	 E	 F 	G 	H	 I	 J	 K	 L	 M	 

65	66	67	68	69	70	71	72	73	74	75	76	77

N	 O	 P	 Q	 R	 S	 T	 U	 V	 W	 X	 Y	 Z 

78	79	80	81	82	83	84	85	86	87	88	89	90



a	 b	 c	 d	 e	 f	 g	 h	 i	 j	 k	 l	 m	 

97	98	99	100	101	102	103	104	105	106	107	108	109	

n	 o	 p	 q	 r	 s	 t	 u	 v	 w	 x	 y	 z 

110	111	112	113	114	115	116	117	118	119	120	121	122

```
#참고 : 아스키코드 사용 
#ASCII CODE
print(ord('A'),ord('B'))
print(chr(ord('A')+2))
print(chr(67))
```

```
#선생님답

def solution(s,n):
    s= list(s)
    
    for i in range(len(s)):
        if s[i].isupper():   #i번째 글자가 대문자인 경우
            s[i]=chr((ord(s[i])-ord('A')+n) %26 +ord('A'))   #GRAPE
            	  #i번째 글자코드- 65 +밀기n번  
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+n) %26 +ord('a'))
    answer = "".join(s)
    
    return answer

print(solution('Grape',5))
```

### 문제3

```
#찬미씨답						# 다시확인 

def updown(s):
    lst_s = s.split(" ")
    str_re = ""
    for i in lst_s:
        for j in i:
            if i.index(j) % 2 != 0:
                str_re += j.upper()
            else:
                str_re += j.lower()
        str_re += " "
    return str_re

updown("Hi My Name Is")
```

###  문제4

```
#선생님 답

def ratio(t):
    for i in range(t):
        scores = list(map(int,input().split()))  # [5 50 50 70 80 90 ]
        n = scores[0]
        scores = scores[1:]    # 50 50 70 80 90 
        avg = sum(scores)/n
        cnt = len([s for s in scores if s> avg])
        print(avg,"%.3f"%(100*cnt/n),end='%\n')
        
    


t=int(input("case"))

print(ratio())
```



### 문제 5



```
#선생님 답

def find_non_cons(a):
    i = a[0]             #2
    for n in a:          #[2,3,5,6,7]
        if n != i:       #2 !=2??
            return n 
        i += 1           #4
    return None
print(find_non_cons([2,3,5,6,7]))
```





