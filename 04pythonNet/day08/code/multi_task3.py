# multi_task.py

# 思考两个任务函数能否同时执行
import time

def task1():
    print(1)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(3)
    time.sleep(1)
    print(4)
    time.sleep(1)

def task2():
    time.sleep(0.5)
    print("A")
    time.sleep(1)
    print("B")
    time.sleep(1)
    print("C")
    time.sleep(1)
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
