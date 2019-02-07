import array


'''
def iswall(x,y):
    if x < 0 or x>= 5 : return True
    if y < 0 or y>= 5 : return True 
'''

li = [[1,1,1,1,1],[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1],[1,1,1,1,1]]
s=[]
for i in range(0,5):
    for j in range(0,5):
        a = li[i][j]
        up = abs(a-li[i-1][j])
        right = abs(a-li[i][j+1])
        down = abs(a-li[i+1][j])
        left = abs(a-li[i][j-1])
        if i-1 < 0:
            up = 0
        if j+1 > 4:
            right = 0
        if i+1 > 4:
            down = 0 
        if j-1 < 0:
            left = 0 
        s.append(up+right+down+left)
sum(s)



