#需求:编写一个程序，该程序用于打印9*9乘法口诀表。
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i}*{j}={i*j}",end=" ")
    print()