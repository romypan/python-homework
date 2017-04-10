# -*- coding: utf-8 -*-
#杨辉三角
def triangles(max):
    L = [1]
    n = 0
    while n < max:
        M = []
        M.append(1)
        for i in range(len(L)):
            if i > 0:
                M.append(L[i-1]+L[i])
        if n > 0:
            M.append(1)
        print(M)
        L = M
        n = n + 1
        
            
            
                
            
        
