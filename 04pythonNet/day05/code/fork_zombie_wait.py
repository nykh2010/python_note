# fork_zombie.py

# 示例示意故意制造一个子进程,当子进程退出后,
# 父进程回收子进程的资源

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
    os._exit(99)
elif r > 0:
    print("父进程等待子进程退出,准备回收资源")
    pid, status = os.wait()
    print("PID为", pid, "的子进程已经退出")
    print("子进程退出的状态码是:", status)
    print("父进程进入死循环")
    while True:
        pass

