# mysemaphore.py

# 此示例以抢手机为例,实现多进程互斥
from multiprocessing import Process
from multiprocessing import Semaphore
import os
import time
# 创建信号量
sem = Semaphore(0)  #初始值为0,所有进程初始都拿不到资源
def process_task():
    print("子进程 pid=", os.getpid(),
          '的进程正在等待抢手机....')
    sem.acquire()  # 等待信号量资源
    print("子进程 pid=", os.getpid(),
          '的进程已获取抢手机下单权限,正在操作中....')
    time.sleep(3)
    print("子进程 pid=", os.getpid(),'下单成功')

processes = []
for i in range(10):
    p = Process(target=process_task)
    processes.append(p)
    p.start()

count = int(input('请输入手机个数: '))
for i in range(count):
    sem.release()  # 每次增加一个信号量

for p in processes:
    p.join()

