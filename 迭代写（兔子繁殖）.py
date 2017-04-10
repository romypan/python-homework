#迭代写兔子繁殖总和
def ddcount(n):
    n1 = 1
    n2 = 1
    n3 = 1
    if n == 1:
        return n1
    elif n == 2:
        return n1+n2
    else:
        x = 0
        y = n1+n2
        while x <= n - 3:
            n3 = n1 + n2
            n1 = n2
            n2 = n3
            x = x + 1
            y = y + n3
        return y
    
ipt = input('输入月数：')
print(dd(int(ipt)))

#迭代写兔子当月繁殖数量
def ddnum(n):
    n1 = 1
    n2 = 1
    n3 = 1
    if n == 1:
        return n1
    elif n == 2:
        return n1+n2
    else:
        x = 0
        while x <= n - 3:
            n3 = n1 + n2
            n1 = n2
            n2 = n3
            x = x + 1
        return n3

        
        
