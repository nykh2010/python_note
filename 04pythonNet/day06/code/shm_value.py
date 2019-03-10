# shm_value.py


# 此示例示意共享内存对象
from multiprocessing import Value
from multiprocessing import Process
import time

# 创建一个整数的共享内存值对象,初始值是10000
shm_v = Value('i', 10000)  

def process_task2():
    for _ in range(100):
        v = shm_v.value  # 获取共享内存的值对象的值
        v += 1
        shm_v.value = v  # 修改共享内存值对象
        time.sleep(1)
p = Process(target=process_task2)
p.start()

for _ in range(200):
    v = shm_v.value
    print("主进程中读取到的值是:", v)
    time.sleep(1)

p.join()
print("程序正常退出")

