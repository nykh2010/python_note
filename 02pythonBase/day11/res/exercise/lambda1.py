# 练习:
#   1. 写一个lambda 表达式, 判断这个数的2次方+1 能否被5整数,如果能整除返回True,否则返回False
#     fx = lambda n: .....
#     print(fx(3))  # True
#     print(fx(4))  # False


fx = lambda n: (n ** 2 + 1) % 5 == 0
# def fx(n):
#     return (n ** 2 + 1) % 5 == 0

print(fx(3))  # True
print(fx(4))  # False
