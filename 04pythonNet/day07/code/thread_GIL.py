# thread_GIL.py

from threading import Thread
import time
#  此示例示意GIL 引起的效率问题:
def task():
    for i in range(100000000):
        pass

tasks = []
for _ in range(10):
    t = Thread(target=task)
    tasks.append(t)
    t.start()

print("开始计算的时间是:", time.time())
begin = time.time()
while tasks:
    tasks[0].join()
    del tasks[0]
print("结束计算的时间是:", time.time())
print("总用时:", time.time() - begin)
