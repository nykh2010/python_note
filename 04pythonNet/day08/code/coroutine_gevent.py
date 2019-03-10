
# coroutine_gevent.py

import gevent  # 导入gevent协程模块

# 利用gevent实现协程
def task1(a, b):
    print("任务1开始运行... a=", a, 'b=', b)
    # 此处的事件需要处理5秒钟
    gevent.sleep(5)  # 让出cpu,切换到另一个协程
    print("任务1结束运行!!!")
    return 8888

def task2():
    print("任务2开始运行... ")
    # 此处的事件需要处理2秒钟
    gevent.sleep(2)
    print("任务2结束运行!!!")
    return 9999

t1 = gevent.spawn(task1, 100, 200)
t2 = gevent.spawn(task2)  # t2绑定greenlet对象?

L = [t1, t2]
result  = gevent.joinall(L)  # 让L中的两个协程对象运行

for grnlet in result:
    print(grnlet.get()) # 8888 或 99999

print("程序结束: result = ", result)

