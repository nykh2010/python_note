n = float(input("输入成绩"))
if 0<=n<=100:
    if n<60:
        print("不及格")
    elif 60<=n<85:
        print("合格")
    else:
        print("优秀")
else:
    print("输入不合法")