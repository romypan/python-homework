# -*- coding: utf-8 -*-
#杨辉三角 产生器
def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i-1]+L[i] for i in range(len(L))] #列表生成列式
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
