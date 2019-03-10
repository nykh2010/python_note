# thread_communication.py

# 此示例示意用全局变量进行进程间通信
from threading import Thread
import time
from threading import Lock  # 导入线程锁类

alock = Lock()  # 创建线程锁

myvar = 10000

def thread_task2():
    global myvar
    for _ in range(1000000):
        alock.acquire()  # 此外永远阻塞 
        myvar += 1
        # alock.release()  引起死锁
    print("子线程任务结束")

t = Thread(target=thread_task2)
t.start()

def main_task():
    global myvar
    for _ in range(1000000):
        alock.acquire()  # 也会永远阻塞
        myvar -= 1
        alock.release()
    print("主线程任务结束")

main_task()

t.join()
print("变量的值是:", myvar)







