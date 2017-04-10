def df1(max):
    n,a,b = 0,0,1
    while n < max:
        yield b     #生成器 generator
        a,b = b,a+b #相当于 t = (b,a+b) t是一个tuple
                    #a = t[0] b = t[1]
        n = n + 1
    return 'done'
#用法(取不到返回值)
# for i in df1(3):
#     print(i)

#取出返回值
# g = df1(3)
# while True:
#      try:
#          x = next(g)
#          print('g:',x)
#      except StopIteration as e:
#          print('Generator return value:',e.value)
#          break
    
        
