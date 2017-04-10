ipt = input('请输入正整数： ')

def dg(x):
    if x == 1:
        return 1
    else:       
        return x * dg(x - 1)
m = dg(int(ipt))
print(m)
