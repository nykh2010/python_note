# shm_value.py


# 此示例示意共享内存对象数据冲突的问题

from multiprocessing import Value
from multiprocessing import Process
import time
from multiprocessing import Semaphore

# 创建一个整数的共享内存值对象,初始值是10000
shm_v = Value('i', 10000)

# 此示例示意用信号量实现互斥,实现多进程锁同样的效果
alock = Semaphore(1)  # 初始值为1

def process_task2(lock):
    for _ in range(1000000):
        with lock:  # 进入with,调用alock.acquire()
            # alock.acquire()
            v = shm_v.value  # 获取共享内存的值对象的值
            v += 1
            shm_v.value = v  # 修改共享内存值对象
            # alock.release()
        # 退出with语句会调用alockc.release()

p = Process(target=process_task2, args=(alock,))
p.start()

for _ in range(1000000):
    with alock:
        # alock.acquire()
        # print("主进程", alock.get_value())
        v = shm_v.value
        v -= 1
        shm_v.value = v
        # alock.release()

p.join()  # 等待子进程退出

print("共享内存的值是:", shm_v.value)  # 10000
print("程序正常退出")

