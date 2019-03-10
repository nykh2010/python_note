# pipe.py

from multiprocessing import Process
from multiprocessing import Pipe
import os
import time

# 创建管理
conn1, conn2 = Pipe()  # 建一个双向管理

def task_fun():
    '''子进程的任务处理函数
       用conn1, 来接收发父进程的数据
    '''
    conn2.close()  # 关闭管道IO对象
    while True:
        obj = conn1.recv()  # 从conn1收数据
        print(os.getpid(), "收到信息:", obj)
        if obj == 'exit':
            break  # 让进程函数结束退出子进程
        send_obj = '====' + obj + '===='
        # 将send_obj 送回给主进程
        conn1.send(send_obj)
    conn1.close()  # 关闭管道

p = Process(target=task_fun)
p.start()

# 主进程做的事情,用conn2来收发数据
conn1.close()
while True:
    s = input("请输入发送给子进程的数据: ")
    conn2.send(s)
    if s == 'exit':
        break  # 准备结束主进程
    obj = conn2.recv()
    print('子进程给父进程的数据是:', obj)

conn2.close()  # 主进程关闭管理两端
p.join()  # 等待回收子进程
print("程序正常退出")


