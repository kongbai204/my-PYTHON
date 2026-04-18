#需求:持续提示用户输入一个数字，并对该数字进行平方运算。
#如果平方运算结果小于50，则停止输入。
while True:
    user_input = input("请输入一个数字：")
    
    try:
        num = float(user_input)       # 支持整数和小数
    except ValueError:
        print("输入无效，请输入一个有效的数字。")
        continue                      # 重新提示输入
    
    square = num ** 2
    print(f"{num} 的平方是 {square}")
    
    if square < 50:
        print("平方结果小于 50，程序结束。")
        break