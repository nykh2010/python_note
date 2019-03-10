# 1. 写一个生成器函数myxrange([start,] stop[, stop]) 来生成一系列整数(功能等同于python2中的xrange或python3中的range)
#   (注:不允许调用range函数)

# def myxrange(...):
#     ...

# L = list(myxrange(10))
#   print(L)  # L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9d]
# for x in myxrange(1, 10, 3):
#     print(x)   # 打印 1 4 7
# L2 = [x in x myxrange(5, 10)]
# print(L2)  # [5, 6, 7, 8, 9]


def myxrange(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0
    if step > 0:
        while start < stop:
            yield start
            start += step
    elif step < 0:
        while start > stop:
            yield start
            start += step
    else:
        raise ValueError("传参错误")




L = list(myxrange(10))
print(L)  # L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9d]

for x in myxrange(1, 10, 3):
    print(x)   # 打印 1 4 7

L2 = [x for x in myxrange(5, 10)]
print(L2)  # [5, 6, 7, 8, 9]
