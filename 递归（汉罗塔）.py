#汉诺塔

def hlt(n,x,y,z):
    if n == 1:
        print(x, ' --> ',z)
    else:
        hlt(n-1,x,z,y)   #将前n-1个盘子借助z移动到y上
        print(x, ' --> ',z) #将最底下的盘子直接移动到z上
        hlt(n-1,y,x,z)   #将n-1个盘子借助x移动到z上
m = input('请输入盘子个数： ')
hlt(int(m),'X','Y','Z')
        
