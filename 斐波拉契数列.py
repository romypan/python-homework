def df1(n):
    n1 = 1
    n2 = 1
    n3 = 1
    L = []
    if n <= 2:
        for i in range(1,n+1):
          L.append(1)
    else:
        L.extend([1,1])
        while n > 2:
            n3 = n1 + n2
            n1 = n2
            n2 = n3
            n = n - 1
            L.append(n3)
    return L
ipt = input('输入正整数：')
L = df1(int(ipt))
print(L)
    
