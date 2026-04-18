#需求:用户输入一个数字，
#实现十进制向二进制、八进制、十六进制的转换功能，
#并打印出转换结果。
                               #二进制
"""#方法1(拉完了)
b=0
c=num
s=""
if num!=1 and num!=0:
    while c-2**b>=0:
        b+=1
    for i in range(b-1,-1,-1):
        if c-2**i>=0:
            s+="1"
            c=c-2**i
        else:
            s+="0"
    print(f"{num}的二进制为{s}")
else:
    print(f"{num}的二进制为{num}")
"""
                #方法二(夯爆了)！！！一次性全都解决。
num=int(input("想输入啥："))
n=int(input("要输入几进制啊（2,8,16）"))
c=num
s=""
if num==0:
    print(f"{num}的{n}进制为0")
    exit()
while c!=0:
    d=c%n
    if d>=10:
        s+=chr(d+55)
    else:
        s+=str(d)
    c=c//n
print(f"{num}的{n}进制为{s[::-1]}")

"""有内置函数
print(bin(20))  # 0b10100   二进制
print(oct(20))  # 0o24      八进制
print(hex(20))  # 0x14      十六进制
"""