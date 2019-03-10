# shm_array.py


# 此示例示意共享数组的使用
# 此示例示意用共享数据自带的多进程锁进行互斥操作
from multiprocessing import Process
from multiprocessing import Array
import time

# 创建一个能存有100个字节的共享数组对象,初始值都为零
shm_a = Array('c', 100)

def process_task2():
    for i in range(100):
        with shm_a:
            shm_a[i] = b'A'  # 将共享数组的第i个字节改为b'A'
        time.sleep(1)

p = Process(target=process_task2)
p.start()

def process_task1():
    for _ in range(110):
        with shm_a:
            v = shm_a.value
        # v = shm_a.raw  # 返回原始数据，包括0
        print("数据长度是:", len(v), 'v=', v)
        time.sleep(1)

process_task1()
print("wait....")
p.join()
print('程序正常退出')

