#需求:输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
letter=0
space=0
num=0
other=0
s=input("请输入字符:")
for i in s:
    if i.isalpha():
        letter+=1
    elif i.isdigit():
        num+=1
    elif i.isspace():
        space+=1
    else:
        other+=1
print(f"英文字母有{letter}个")
print(f"数字有{num}个")
print(f"空格有{space}个")
print(f"其他有{other}个")