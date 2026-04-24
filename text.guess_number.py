import random
import time

def main():
    print("=" * 40)
    print("       欢迎来到猜数字游戏!")
    print("=" * 40)
    print("\n请选择难度:")
    print("1. 简单   (1-50, 8次机会)")
    print("2. 中等   (1-100, 7次机会)")
    print("3. 困难   (1-200, 6次机会)")
    print("4. 史诗   (1-500, 5次机会)")
    print("5. 挑战   (1-1000, 8次机会, 每次输入数字)")
    
    while True:
        try:
            choice = int(input("\n请选择 (1-5): "))
            if choice in [1, 2, 3, 4, 5]:
                break
            print("请输入1-5之间的数字!")
        except ValueError:
            print("输入无效，请输入数字!")
    
    difficulties = {
        1: (1, 50, 8),
        2: (1, 100, 7),
        3: (1, 200, 6),
        4: (1, 500, 5),
        5: (1, 1000, 8)
    }
    
    min_num, max_num, chances = difficulties[choice]
    secret = random.randint(min_num, max_num)
    
    print(f"\n游戏开始! 数字在 {min_num} 到 {max_num} 之间")
    print(f"你有 {chances} 次机会!\n")
    
    for attempt in range(1, chances + 1):
        remaining = chances - attempt
        
        while True:
            try:
                if choice == 5:
                    guess = int(input(f"第 {attempt}/{chances} 次, 输入数字: "))
                else:
                    guess = int(input(f"第 {attempt}/{chances} 次, 猜一个数字: "))
                break
            except ValueError:
                print("请输入有效数字!")
        
        if guess == secret:
            print(f"\n🎉 恭喜! 你在第 {attempt} 次猜对了!")
            print(f"答案是 {secret}")
            
            if attempt == 1:
                print("⭐ 太强了! 一次就猜中! ⭐")
            elif attempt <= chances // 2:
                print("很厉害哦!")
            
            print(f"\n游戏用时: {time.time():.1f} 秒")
            break
        
        elif guess < secret:
            print(f"太小了!", end=" ")
        else:
            print(f"太大了!", end=" ")
        
        if remaining > 0:
            print(f"还剩 {remaining} 次机会")
        else:
            print(f"\n😢 游戏结束! 正确答案是 {secret}")
            print("再接再厉!")
    else:
        pass
    
    print("\n" + "=" * 40)
    again = input("再来一局? (y/n): ").lower()
    if again == 'y' or again == '是' or again == '':
        main()
    else:
        print("谢谢游玩! 再见! 👋")

if __name__ == "__main__":
    main()
