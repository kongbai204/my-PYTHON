import random
def main():
    nums=list(range(1,10))
    random.shuffle(nums)
    secret=nums[:5]
    print("===猜数字游戏===")
    print("请猜5个1-9的不重复数字")
    attempts=0
    while True:
        attempts+=1
        guess=input("请输入:").strip()
        if len(guess)!=5 or not guess.isdigit():
            print("请输入5个数字!")
            continue
        g=[int(c) for c in guess]
        if len(set(g))!=5:
            print("数字不能重复!")
            continue
        a=sum(1 for i in range(5) if g[i]==secret[i])
        b=sum(1 for i in range(5) if g[i]!=secret[i] and g[i] in secret)
        print("结果:"+str(a)+"A"+str(b)+"B")
        if a==5:
            print("恭喜猜对了!答案:"+str(secret)+",尝试次数:"+str(attempts))
            break
main()