#需求:定义一个函数，
#该函数用于计算并返回给定半径的圆的面积(要求结果保留两位小数)。
import math
def circle(r):
    s=math.pi*r**2
    s=float(f"{s:.2f}")
    return s
r=float(input("想输入半径多少："))
print(f"面积为{circle(r)}")