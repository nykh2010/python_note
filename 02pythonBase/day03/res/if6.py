# 输入季度，输出季度对应的月份，如果输入的1-4之外的数据，提示 
#     输入错误？
a = int(input("请输入季度"))
if a == 1:
    print("1  2 3 月")
elif a == 2:
    print(" 4 5 6 月")
elif a == 3:
    print(" 7 8 9月")
elif a == 4:
    print("10 11 12月")
else:
    print("输入错误")

print("end")