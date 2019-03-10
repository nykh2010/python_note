# thread_event.py

# 此示例示意线程事件Event的用法:
from threading import Event
from threading import Thread
import time

event = Event()  # 创建事件对象

def thread_task(info):
    while True:
        print(info, '进入等待....')
        event.wait()
        print(info, '解除等待!!!!')
        # event.clear()  # 设置为False状态

t1 = Thread(target=thread_task, args=('线程1',))
t2 = Thread(target=thread_task, args=('线程2',))
t1.start()
t2.start()

for i in range(10):
    time.sleep(5)
    print("主进程将事件设置为True")
    event.set()  # 将event设置为True
    time.sleep(3)
    event.clear()

t1.join()
t2.join()
print("=======主线程结束=======")