# 写一个生成器函数 myodd(x) 来生成一系列奇数
#  如:
#   # myodd(10) 可以生成 1 3 5 7 9
#   def myodd(n):
#       ....  # <<< 此处自己实现
#   L = [ x for x in myodd(10)]  # L = [1, 3, 5, 7,9]
#   for x in myodd(6):
#       print(x)  # 打印 1, 3, 5


def myodd(n):
    i = 0
    while i < n:
        if i % 2 == 1: # 是奇数，送回给next(it)调用
            yield i
        i += 1

L = [ x for x in myodd(10)]  # L = [1, 3, 5, 7, 9]
print(L)  # 
for x in myodd(6):
    print(x)  # 打印 1, 3, 5