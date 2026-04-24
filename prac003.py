#需求:编写一个程序，该程序用于计算从1到100(包含1和100)所有整数的和，并将结果打印出来。
result=0
for i in range(1,101,1):
    result+=i
print(result)