# coroutine_greenlet.py

from greenlet import greenlet

# 用greenlet实现协程
def task1():
    print(1)
    gr2.switch()  # 切换到协程2
    print(2)
    gr2.switch()  # 切换到协程2
    print(3)
    gr2.switch()  # 切换到协程2
    print(4)
    gr2.switch()  # 切换到协程2

def task2():
    print("A")
    gr1.switch()  # 切换到协程1
    print("B")
    gr1.switch()  # 切换到协程1
    print("C")
    gr1.switch()  # 切换到协程1
    print("D")
    gr1.switch()  # 切换到协程1

# 希望执行结果是: 1A2B3C4D

gr1 = greenlet(task1)
gr2 = greenlet(task2)  # 创建协程对象

gr1.switch()  # 切换到gr1协程，让他先运行
print("程序退出")

