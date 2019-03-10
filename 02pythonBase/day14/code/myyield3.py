# myyield.py

# 此示例示意生成器函数的定义和调用
def myyield():
    '''这是一个生成器函数'''
    print("即将生成2")
    yield 2
    print("即将生成3")
    yield 3
    print("即将生成5")
    yield 5
    print("即将生成7")
    yield 7
    print("生成器函数调用结束")

it = iter(myyield())  # it 绑定迭代器
x = next(it) # 当向迭代器要数据时，生成器函数才开始执行
             # 并遇到yield 将停止执行，并返回数据给next函数




             