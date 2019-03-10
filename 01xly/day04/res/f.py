# 请输入（1-4）代表季度，
# 请输入每一个季度都有那几个月？
n = int(input("请输入代表的季度(1-4)"))
if n == 1:
    print("春天在1,2,3月")
elif n == 2:
    print("夏天在4,5,6月")
elif n == 3:
    print("秋季在7,8,9月")
elif n == 4:
    print("冬季在10,11,12月")
else:
    print("数据输入错误，请重新输入数据")

print("ends.....")
