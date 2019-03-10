# multi_task.py

# 思考两个任务函数能否同时执行
import time
# 用线程的event 实现两个任务的互相唤醒来快速完成两个任务
# 的执行
from threading import Event

e1 = Event()  # 此事件用于阻塞task1
e2 = Event()  # 此事件用于组塞task2

e2.clear()  # 置为False

def task1():
    print(1)
    e2.set()
    e1.clear()
    e1.wait()
    print(2)
    e2.set()
    e1.clear()
    e1.wait()
    print(3)
    e2.set()
    e1.clear()
    e1.wait()
    print(4)
    e2.set()

def task2():
    e2.wait()  
    print("A")
    e2.clear()
    e1.set()
    e2.wait()
    print("B")
    e2.clear()
    e1.set()
    e2.wait()
    print("C")
    e2.clear()
    e1.set()
    e2.wait()
    print("D")

# 希望执行结果是: 1A2B3C4D
# 用多进程来实现
from threading import Thread
p1 = Thread(target=task1)
p2 = Thread(target=task2)
p1.start()
p2.start()
p1.join()
p2.join()
print("程序正常退出")
