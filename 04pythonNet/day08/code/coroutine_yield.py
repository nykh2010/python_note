# multi_task.py

# 思考两个任务函数能否同时执行
def task1():
    print(1)
    yield
    print(2)
    yield
    print(3)
    yield
    print(4)

def task2():
    next(co)
    print("A")
    next(co)
    print("B")
    next(co)
    print("C")
    try:
        next(co)
    except StopIteration:
        pass
    print("D")

# 希望执行结果是: 1A2B3C4D
co = task1()  # 创建生成器

task2()