# -*- coding:utf-8 -*-
#过滤非回数 回数是指从左向右读和从右向左读都是一样的数，例如12321，909
def is_palindrome(n):
	m = str(n)
	for i in range(len(m) // 2 + 1):
		return m[i] != m[len(m)-1-i]
output = filter(is_palindrome, range(1, 1000))
print(list(output))

def is_palindrome2(n):
    return str(n) != str(n)[::-1]
output = filter(is_palindrome2,range(1,1000))
print(list(output))
