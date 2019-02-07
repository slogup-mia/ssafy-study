



'''
arr = [3,6,7,1,5,4,-3,-4,-2,-6]

n = len(arr)
count =0
for i in range(1,1<<len(arr)):
    summ = 0
    for j in range(len(arr)):
        if i & (1<<j):
            summ += arr[j]
            print(arr[j],end= ', ')
    if summ == 0:
        count += 1
         
    print()
print(count)
'''


arr = [3,6,7,1]

n = len(arr)

for i in range(1<<n):
    for j in range(n+1):
        if i & (1<<j):
            print(f'{i} {j} {arr[j]}',end= ', ')
    print()
print()

'''
i j arr[j]
1 0 3,
2 1 6,
3 0 3, 3 1 6,
4 2 7,
5 0 3, 5 2 7,
6 1 6, 6 2 7,
7 0 3, 7 1 6, 7 2 7,
8 3 1,
9 0 3, 9 3 1,
10 1 6, 10 3 1,
11 0 3, 11 1 6, 11 3 1,
12 2 7, 12 3 1,
13 0 3, 13 2 7, 13 3 1,
14 1 6, 14 2 7, 14 3 1,
15 0 3, 15 1 6, 15 2 7, 15 3 1,

ex) 1 0 3 
if 

'''