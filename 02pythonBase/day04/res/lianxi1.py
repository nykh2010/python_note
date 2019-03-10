# 练习：输入一个整数x，求x的5倍的值？
#     （x*5）

x = int(input("请输入数据"))
#x*2**2+x= x*4+x =x*5
a = (x<<2) + x
print(a)
