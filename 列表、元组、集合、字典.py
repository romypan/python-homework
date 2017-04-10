
#列表  使用中括号 
list1   =   [1,2,'aa','bb']
    #访问: (索引)list1[0]、(切片)
    #添加: append('11')、insert(2,'11')、extend(['11']) 、list1 + ['11']
    #删除: remove('11')、pop(索引)、clear() --全部清除
    #运算: list1 + ['22']、list1 * 2 、print(2 in list1)、not in 、== 、!= 

#元祖  使用小括号
tuple1  =   (1,2,'aa','bb')
    #访问: (切片)tuple1[1]、tuple1[2:] --取索引2及以后的元祖 tuple1[:2] --取2之前的
    #     tuple1[:] 对元祖的复制
    #添加: tuple1 + ('cc',) --元组中只包含一个元素时，需要在元素后面添加逗号来消除歧义
    #删除: del tuple1 --元祖元素值不允许删除，只能删除整个元祖
    #运算: tuple1 + ('cc',)、tuple1 * 2、print(2 in list1)、not in 、== 、!=  

#集合   使用大括号
set1    =   {1,2,'aa','bb'}
    #访问: set集合是【无序】的，不能通过索引和切片来做一些操作
    #添加: add('44') 、update('44')--把要传入的元素拆分，做为个体传入到集合中
    #删除: remove('44')
    #运算: set1 | {'5'}(合集) 、&(交集)、in 、not in 、== 、!=  
    
#字典   使用大括号 {key1:value1,key2:value2}
dict1   =  {'name1':'aa','name2':'bb'}
    #访问: dict1['name1']
    #添加: dict1['name3'] = 'cc' 、dict({'a':1,'b':2})
    #删除: del dict1['name3'] 、dict1.pop('name3') 、 del dict1 --删除整个字典
    #运算: dict1.keys() --返回键、dict1.values() --返回值、
    #     dict1.items() --返回一个包含所有（键，值）元祖的列表；
    #     dict1.copy() 返回一个字典浅拷贝的副本；dict1.has_key(key) 
    #       
    
    
    
