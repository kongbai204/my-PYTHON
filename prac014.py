#需求:接收用户输入的三个数字，并按从小到大的顺序输出。
"""

方法1：
num=[]
for i in range(1,4):
    a=float(input("输入你想输入的数字:"))
    num.append(a)
num.sort()
for i in num:
    print(i)

    """

num1=float(input("输入你想输入的数字:"))
num2=float(input("输入你想输入的数字:"))
num3=float(input("输入你想输入的数字:"))
if num1 >num2:
    num1,num2 =num2,num1
if num2 >num3:
    num2,num3 =num3,num2
if num1 >num2:
    num1,num2 =num2,num1
print(num1,num2,num3)

