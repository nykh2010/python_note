# shm_value.py


# 此示例示意共享内存对象数据冲突的问题

from multiprocessing import Value
from multiprocessing import Process
import time

# 创建一个整数的共享内存值对象,初始值是10000
# 不加锁会引起逻辑混乱

shm_v = Value('i', 10000)

def process_task2():
    for _ in range(1000000):
        v = shm_v.value  # 获取共享内存的值对象的值
        v += 1
        shm_v.value = v  # 修改共享内存值对象

p = Process(target=process_task2)
p.start()

for _ in range(1000000):
    v = shm_v.value
    v -= 1
    shm_v.value = v

print("共享内存的值是:", shm_v.value)  # 10000

p.join()
print("程序正常退出")

