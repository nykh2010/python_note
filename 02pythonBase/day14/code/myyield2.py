# myyield.py

# 此示例示意生成器函数的定义和调用
def myyield():
    '''这是一个生成器函数'''
    yield 2
    yield 3
    yield 5
    yield 7
    print("生成器函数调用结束")

for x in myyield():
    print(x)