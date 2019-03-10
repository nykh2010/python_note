# fork.py

import os  # fork函数在os模块中
import time

def task1():
    i = 0
    while True:
        print('i=', i)
        i += 1
        time.sleep(1)

def task2():
    a = 100
    while True:
        print('a=', a)
        a -= 1
        time.sleep(2)

print("当前进程的PID:", os.getpid())

r = os.fork()  # 此函数会让此程序创建一个子进程
if r == -1:  # fork失败返回-1
    print("创建子进程失败")
elif r == 0:
    print("进程PID为", os.getpid(), '的程序正运行')
    task1()
elif r > 0:
    print("父进程PID为:", os.getpid())
    print("子进程的PID为:", r)
    task2()

print("程序退出")

