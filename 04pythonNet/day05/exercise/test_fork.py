import os
print('开始创建子进程')
os.fork()
os.fork()
os.fork()
import time
time.sleep(20)
print('程序退出')
