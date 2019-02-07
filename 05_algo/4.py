def select(list,k):
    for i in range(0,k):
        minIndex = i 
        for j in range (i+1, len(list)):
            if list[minIndex] > list[j]:
                minIndex = j