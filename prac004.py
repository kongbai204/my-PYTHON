#需求:有四个数字:1、2、3、4，统计能组成多少个互不相同且无重复数字的三位数?各是多少?
count=0
for a in range(1,5):
    for b in range(1,5):
        if a==b:
            continue
        for c in range(1,5):
            if c==b or a==c:
                continue
            else:
                print(a*100+b*10+c)
                count+=1

