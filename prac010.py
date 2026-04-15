'''
需求:给定一个学生信息列表，根据学生的成绩进行排序。
学生成绩数据格式:复杂列表，元素是字典或者元组。
示例:[
{'sno': 101,'sname': "小",'sgrade': 88},
{'sno': 102, 'sname': "小", 'sgrade': 77},
{'sno': 103, 'sname': "小李",'sgrade': 99},
{'sno': 104, 'sname': "小赵",'sgrade': 66}
]
'''
student=[
{'sno': 101,'sname': "小",'sgrade': 88},
{'sno': 102, 'sname': "小", 'sgrade': 77},
{'sno': 103, 'sname': "小李",'sgrade': 99},
{'sno': 104, 'sname': "小赵",'sgrade': 66}
]
new_list=sorted(student,key=lambda stu: stu.get('sgrade'))
print(new_list)