# no_ipc.py

import multiprocessing as mp
from time import sleep
import os

myvar = 10000
 
def process_task():  # 子进程处理函数
    global myvar
    for _ in range(30):
        myvar -= 1
        sleep(1)
        print("PID为:", os.getpid(),
              '的子进程的myvar=', myvar)
p = mp.Process(target=process_task)
p.start()  # 启动子进程

for _ in range(50):
    myvar += 2
    sleep(1)
    print("PID为:", os.getpid(), '的父进程的myvar=',
            myvar)
p.join()  # 回收子进程资源:
print('myvar=', myvar)  # 请问此处值是多少 ?