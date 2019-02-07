s = []
for i in range(0,5):
    for j int range(0,5):
        a = array[i][j]
        up = abs(a-array[i-1][j])
        right = abs(a-array[i][j+1])
        down = abs(a-array[i+1][j])
        left = abs(a-array[i][j-1])        
        if i == 0 and j == 0:
            s.append(right+down)
        elif i == 0:
            s.append(left+down+right)
        elif j == 0:
            s.append(up+right+down)
        elif i == 4 and j == 0: 
            s.append()
        s.append(abs(a-array[x-1][y]+abs(a-array[x][y+1])+abs(a-array[x+1][y])+abs(a-array[x][y-1]))


