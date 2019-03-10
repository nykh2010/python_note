# myyield.py

# 此示例示意生成器函数的定义和调用
def myyield():
    '''这是一个生成器函数'''
    yield 2
    yield 3
    yield 5
    yield 7
    print("生成器函数调用结束")

gen = myyield()  # 调用生成器函数绑定,返回生成器并用gen绑定
it = iter(gen)  # 向生成器要迭代器，用it绑定
print(next(it))  # 2
print(next(it))  # 3
print(next(it))  # 5
print(next(it))  # 7
print(next(it))  # StopIteration异常
