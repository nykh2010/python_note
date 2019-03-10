# process_pool_map.py

# 此示例示意用进程池实现多任务的计算

from multiprocessing import Pool
import time
import random

def task_fun(n):
    print("开始计算:", n, '的平方')
    time.sleep(random.randint(1, 10))
    # for x in range(50000000 * random.randint(1, 10)):
    #     pass
    print("结束计算:", n, '的平方')
    return n * n

# 创建进程池
pool = Pool()
r = pool.map(task_fun, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(r)
pool.close()  # 关闭进程池
pool.join()   # 回收僵尸进程
