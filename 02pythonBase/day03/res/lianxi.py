# 1、输入一年中的月份（1-12），输出的是月份在那个季节，输入的数据
# 如果是1-12之外的数据，显示输入错误？



# a = int(input("请输入数据"))

# if 1<=a<=3:
#     print("春季")
# elif 4<=a<=6:
#     print("夏季")
# elif 7<=a<=9:
#     print("秋季")
# elif 10<=a<=12:
#     print("冬季")
# else:
#     print("输入出错")
# 2、BMI=体重/身高**2
#   如果，BMI  小于18.5 过轻
#         18.5-25：正常
#         25-28    过重
#         28-32    肥胖
b = float(input("请输入身高数据"))
c = float(input("请输入体重数据"))
bmi=c/(b**2)
if bmi<18.5:
    print("体重过轻")
elif 18.5<=bmi<=25:
    print("正常")
elif 25< bmi <=28:
    print("过重")
elif 28< bmi<32:
    print("肥胖")
else:
    print("太.......")

print("end")



