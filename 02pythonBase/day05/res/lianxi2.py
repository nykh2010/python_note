# 练习：写一个程序，判断输入的数据是不是回文？
#     ABCCBA  ABCBA 
s = input("请输入数据")

s1 =　s[::-1]
if s == s1:
    print("是回文")
else:
    print("不是回文")

