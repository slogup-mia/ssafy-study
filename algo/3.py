
'''

def seq(a,n,key):
    i = 0 
    while i <n and a[i] != key :
        i = i+1
    if i < n :
        return i
    else:
        return -1 


a = [2,5,7,8,1]
print(seq(a,5,8))

'''

'''
def bin(a,key):
    start = 0
    end = len(a)-1

    while start <= end :
        mid = (start+end)//2
        if a[mid] == key:
            return mid
        elif a[mid] >key :
            end = mid -1
        else :
            start = mid +1
    return False

a= [2,4,5,7,9,12,15,17,22]
print(bin(a,8))
'''
