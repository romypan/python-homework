#首字母大写 使用[map] (返回列表)
#用法：name = ['jArrY','tOM']
#     normalize(name)
def normalize(name):
    def fn(a):
        return a[:1].upper() + a[1:].lower()
    return list(map(fn,name))

#list求积 使用[reduce] (返回值)
from functools import reduce
def prod(L):
    def fn(x,y):
        return x * y
    return reduce(fn,L)

#字符串转浮点数 [map][reduce]
from functools import reduce
def str2float(s):
    def str2num(s):
        def fn(x,y):
            return x * 10 + y
        def char2num(a):
            return {'0':0,'1':1,'2':2,'3':3,'4':4
                    ,'5':5,'6':6,'7':7,'8':8,'9':9}[a]
        return reduce(fn,map(char2num,s))
    a,b = s.split('.')
    return str2num(a) + 0.1 ** len(b) * str2num(b)




