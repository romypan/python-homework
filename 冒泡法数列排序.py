#冒泡法数列排序
def lpx(L):
    for i in range(len(L)):
        for j in range(len(L)-i-1):
            if L[j] > L[j+1]:
                temp = L[j]
                L[j] = L[j+1]
                L[j+1] = temp
    return L
                
