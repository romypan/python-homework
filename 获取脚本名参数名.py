#获取脚本名称，脚本中参数名
from sys import argv
a = argv
for i in range(0,len(a)):
    if i == 0:
        print('脚本名：',a[0])
    else:
        print('参数'+str(i)+'：',a[i])
