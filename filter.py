#filter过滤序列  生成素数

#生成器 构造一个从3开始的奇数序列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield  n
#定义一个筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0
#定义一个生成器
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)
for n in primes():
    if n < 1000:
        print(n)
    else:
        break



