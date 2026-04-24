#需求:给定一个字典，其中每个人的姓名作为键，对应的年龄作为值。
#请找出年龄最大者的姓名与年龄，并将其打印出来
people = {
    "张三": 23,
    "李四": 38,
    "王五": 29,
    "赵六": 45,
    "孙七": 31
}
value_dic=people.values()
max_age=max(value_dic)
for name,age in people.items():
    if age==max_age:
        print(name,max_age)