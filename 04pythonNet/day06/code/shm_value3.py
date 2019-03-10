# shm_value.py


# 此示例示意共享内存对象数据冲突的问题

from multiprocessing import Value
from multiprocessing import Process
import time
from multiprocessing import Lock

# 创建一个整数的共享内存值对象,初始值是10000

# 用多进程锁实现互斥操作
# 创建一个锁用来保护对共享值对象的操作
shm_lock = Lock()  # 创建锁

shm_v = Value('i', 10000)

def process_task2():
    for _ in range(1000000):
        with shm_lock:
            v = shm_v.value  # 获取共享内存的值对象的值
            v += 1
            shm_v.value = v  # 修改共享内存值对象

p = Process(target=process_task2)
p.start()

for _ in range(1000000):
    with shm_lock:
        v = shm_v.value
        v -= 1
        shm_v.value = v

print("共享内存的值是:", shm_v.value)  # 10000

p.join()
print("程序正常退出")

