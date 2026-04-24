#需求:编写一个程序，计算a+aa+aaa+aaaa+...的值，
#其中a是一个数字，且加数的个数由键盘输入决定。
#例如，当a=2且共有5个数相加时，表达式为2+22+222+2222+22222.
a=input("想输入啥呀(0-9)")
nums=int(input("想输入几个数啊"))
sum=0
for i in range(1,nums+1):
    sum+=int(a*i)
print(sum)