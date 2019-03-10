# thread_demo1.py

from threading import Thread
import time

def thread_task1():
    for i in range(10):
        print("子线程中的i=", i)
        time.sleep(2)
    print("线程1执行结束")

t = Thread(target=thread_task1)
t.start()  # 启动线程
print("子线程的名字是:", t.getName())
t.setName("MyThread-1000")
print("子线程的名字是:", t.getName())

def main_task():
    for i in range(15):
        print("主线程中的i=", i)
        time.sleep(1)

main_task()
print("子线程的状态是:", t.is_alive())
t.join()  # 等待回收线程资源
print("join后的子线程的状态是:", t.is_alive())

print("-------主线程执行结束---------")


