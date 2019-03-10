# process1.py


# 此示例示意用multiprocessingn 的Process类
# 来创建子进程

import multiprocessing as mp
import time
import os

def process_fun(m, n):
    for x in range(m, n):
        print("x=", x)
        time.sleep(1)
    print("PID为", os.getpid(),
          '的子进程即将退出')

# 创建进程对象
p = mp.Process(target=process_fun,
               name="自定义进程1",
               args=(20, 50))

print("PID为", os.getpid(), '的父进程即将创建子进程')
p.start()  # 创建子进程并开始运行process_fun

print("父进程进入死循环")
while True:
    pass