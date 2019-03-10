# process_pool.py

# 此示例示意进程池的用法:
from multiprocessing import Pool # 导入进程池类
from time import sleep, asctime
import random
import os

def task_fun(arg):
    print("开始:", arg)
    sleep(random.randint(1, 10))
    print("结束:", arg)
    return asctime()  # 返回一个结束时间的字符串

# 创建进程池,进程数量默认
pool = Pool()

result = []  # 用来保存任务结果
# 创建10个任务交给进程池中的进程计算
for i in range(10):
    s = "任务 %d" % (i+1)
    # 此处用apply 同步执行任务
    # 同步时直接返回值对象
    r = pool.apply(func=task_fun,
                         args=(s,))
    result.append(r) # 存储函数事件对象

# 关闭进程池
pool.close()
# 回收子进程
pool.join()
for i in result:
    # 获取进程事件函数的返回值:
    print(i)



