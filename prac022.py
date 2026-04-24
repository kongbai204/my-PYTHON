#需求:定义一个名为factorial的函数，该函数用于计算并返回给定整数的阶乘值。
#阶乘:一个正整数的阶乘是所有小于及等于该数的正整数的积，0的阶乘为1。
#示例:5的阶乘:1*2*3*4*5;10的阶乘:1*2*3*4*5*6*7*8*9*10。
def factorial(a):
    res=1
    for i in range(1,a+1):
        res=res*i
    return res
a=int(input("想输入什么数:"))
print(factorial(a))