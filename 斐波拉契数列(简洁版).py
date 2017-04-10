def df1(max):
    n,a,b = 0, 0, 1
    while n < max:
        print(b)
        b,a = a + b, b
        n = n + 1
    return 'done'
        
        
        
