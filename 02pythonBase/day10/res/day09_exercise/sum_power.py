# 1. 定义两个函数:
#    sum3(a, b, c)  用于返回三个数的和
#    pow(x) 用于返回x的三次方(立方)

#   用以上函数计算:
#     1) 计算  1的立方 + 2 的立方 + 3的立方
#     2) 计算 1 + 2 + 3的和的立方

def sum3(a, b, c):
    return a + b + c

def pow(x):
    return x ** 3

s = sum3(pow(1), pow(2), pow(3))
print("1的立方 + 2 的立方 + 3的立方=", s)
print("1 + 2 + 3的和的立方", pow(sum3(1, 2, 3)))