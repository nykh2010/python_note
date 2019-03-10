# 　　2.  写一个类 Fibonacci 实现迭代器协议，此类的对象可以用为可迭代对象生成相应的斐波那契数,即
#       1 1 2 3 5 8 13...
#     类定义如下:
#         class Fibonacci:
#             def __init__(self, n):
#                 ....
#       实现如下操作:
#         for x in Fibonacci(10):
#             print(x)  # 1 1 2 3 5 8 13 ...


class Fibonacci:
    def __init__(self, n):
        self.count = n  # 总个数
    def __iter__(self):
        return  Fibonacci_iter(self.count) # return 迭代器

class Fibonacci_iter:
    def __init__(self, n):
        self.count = n  # 记录个数
        self.cur_count = 0  # 已经生成的数的个数
        self.a = 0  # 表示当前斐波那契数的前一个
        self.b = 1  # 表示当前斐波那契数

    def __next__(self):
        if self.cur_count >= self.count:
            # 说明已经生成完毕
            raise StopIteration
        # 生成一个数字
        r = self.b
        # 生成下个数,为下次取数做准备
        self.a, self.b = self.b, self.a + self.b
        # 将已生成的个数做加1操作
        self.cur_count += 1
        # 返回生成的数字
        return r
for x in Fibonacci(100):
    print(x)  # 1 1 2 3 5 8 13 ...
