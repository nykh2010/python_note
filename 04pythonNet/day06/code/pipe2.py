# pipe.py

from multiprocessing import Process
from multiprocessing import Pipe
import os
import time

# 创建管理
conn1, conn2 = Pipe(False)  # 建一个单向管理

def task_fun():
    '''子进程的任务处理函数
       用conn1, 来接收发父进程的数据
    '''
    conn2.close()  # 关闭管道IO对象
    print('PID为', os.getpid(), "正在等待收消息...")
    # b = 收到的字节串, s = b.decode(), obj=eval(s)
    obj = conn1.recv()  # 从conn1收数据
    print(os.getpid(), "收到信息:", obj)
    conn1.close()  # 关闭管道

p = Process(target=task_fun)
p.start()

# 主进程做的事情,用conn2来收发数据
conn1.close()


input("请输入回车键发送消息 ")
L = [1, 2, 3, "ABC"]
conn2.send(L)  # s=repr(L), b = s.encode() 发送--> b

conn2.close()  # 主进程关闭管理两端
p.join()  # 等待回收子进程
print("程序正常退出")


