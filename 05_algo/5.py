'''
연습문제 3

'''


dx = [0,1,0,-1]
dy = [1,0,-1,0]
dir_stat = 0  #0.우 1.아래 2.좌 3.위
'''
def isWall:
    if :
        return True
    if :
        return True
    if :
        return True 
'''

for i in range(25):
    cur_min = sel_min()
    sorted_ary[x][y] = cur_min
    X += dx[dir_stat]
    Y += dy[dir_stat]

    if isWall(X,Y):
        X -= dx[dir_stat]
        Y -= dy[dir_stat]
        dir_stat = (dir_satt+1)%4

