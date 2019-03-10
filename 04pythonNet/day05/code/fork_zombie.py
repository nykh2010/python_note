# fork_zombie.py

# 示例示意故意制造一个僵尸进程
import os
import time

print("当前进程ID为", os.getpid(),
      "的进程准备创建子进程")

r = os.fork()
if r == -1:
    print("创建子进程失败")
elif r == 0:
    print("子进程已经创建,pid=", os.getpid())
    time.sleep(15)
    print("子进程退出")
elif r > 0:
    print("父进程进入死循环")
    while True:
        pass

