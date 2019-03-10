# coroutine_yield_send.py

# 思考两个任务函数能否同时执行
def task1():
    print(1)
    r = yield "111111111"
    print('task2发送过来的数据是:', r)  # 'AAAAAA
    print(2)
    yield
    print(3)
    yield
    print(4)

def task2():
    s = co.send(None)  # next(co)  第一次send必须是None
    print("task1发送过来的数据是:", s)
    print("A")
    co.send('AAAAAA')  # next(co)
    print("B")
    co.send('BBBBBB')  # next(co)
    print("C")
    try:
        co.send('CCCCCCCC')  # next(co)
    except StopIteration:
        pass
    print("D")

# 希望执行结果是: 1A2B3C4D
co = task1()  # 创建生成器

task2()