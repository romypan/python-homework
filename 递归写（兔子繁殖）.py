#递归写兔子当月繁殖数量
def ddcount(x):
    if x <= 2:
        return 1
    else:
        return  ddcount(x-1) + ddcount(x-2)

ipt = input('请输入月数： ')
m = 0
for i in range(1,int(ipt)+1):
    m = m + ddcount(i)
print(str(m))

#列表生成式 [1,1,2,3,5]
L = [ddcount(i) for i in range(1,int(ipt)+1)]
print(L)


