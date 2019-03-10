# message_queue.py


# 进程间通信之消息队列 
import multiprocessing as mp
from multiprocessing import Queue
from multiprocessing import Process
import time
import os

# 创建消息队列:
queue = Queue(5)

def process_task(q):  # q绑定传入的消息队列
    while True:
        s = q.get()  # 从消息队列中获取消息
        print("子进程收到消息:", s)
        if not s:
            break
        time.sleep(5)  # 每五秒收一个次消息队列中的消息
    print("子进程退出")

p = Process(target=process_task, args=(queue,) )
p.start()  # 启动子进程

# 主进程发送消息
while True:
    s = input("请输入要发送给子进程的消息: ")
    queue.put(s)
    if not s:  # 如果用户没有输入数据,则直接退出
        break
p.join()
print('主进程退出')