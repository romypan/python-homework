#阶乘函数#
ipt = input('请输入一个正整数：')
def jc(x):
    for i in range(1,int(x)):
        x = int(x) * i
    return x
m = jc(ipt)
print(m)
