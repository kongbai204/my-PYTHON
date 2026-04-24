"""
需求:给定一个简单列表，对其元素进行排序。
简单列表:元素类型不是复合类型(列表/元组/字典)。示例:
形式1:[20,50,10,40,30]
形式2:["bb','ee','aa','dd','cc']
"""


"""
1.原地排序：直接修改原来的列表，不会生成新列表
"""
num=[20,50,10,40,30]
alpha=['bb','ee','aa','dd','cc']
num.sort()
print(num)
alpha.sort()
print(alpha)
#反转用    x.reverse()


"""
2.新建排序：不改动原列表，生成一个全新的排好序的列表
"""
num=[20,50,10,40,30]
alpha=['bb','ee','aa','dd','cc']
new_num=sorted(num)
print(new_num)
print(num)
new_alpha=sorted(alpha)
print(new_alpha)
print(alpha)
#反转用    list(reversed(list))
#         即：new_list=list(reverse(list))




''' 高阶用法:
    用sort内部的参数 即：sort(key=none,reverse=False)
    key默认为none，是比较大小              key是函数，可以定制排序规则，例如key=len就是长度判断
    reverse默认为False，即正序             reverse是布尔值 (True/False），可以控制升降序。
    
    同理：sorted(iterable, key=None, reverse=False)
            iterable:想要排序的可迭代对象，即我先前的num和alpha。所以可以看到reverse(list)
    所以：   
        num = [20, 50, 10, 40, 30]
        num.sort(reverse=True)         #如果想要降序就在()把reverse变为True。
        print(num)
        num.sort() 
        print(num)  
'''