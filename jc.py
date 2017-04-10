def jc(x):
    if not isinstance(x,int):
        raise TypeError('bad operand type')
    if x == 1:
        return 1
    else:
        return x * jc(x-1)

    
