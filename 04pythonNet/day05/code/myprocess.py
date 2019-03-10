# myprocess.py

# 此示例示意自定义一个进程类MyProcess. 用此类的对象
# 来创建子进程
import multiprocessing as mp
import os
import time

class MyProcess(mp.Process):
    '''此类继承自Process类'''
    def __init__(self, value):
        self.value = value
        super().__init__()

    def run(self):
        '''此方法将覆盖父类中的run方法,此方法会在当前
        进程启动时自动调用,当此方法返回时,子进程结束运行'''
        for x in range(self.value, 0, -1):
            print("pid=", os.getpid(),
                  '的子进程x=', x)
            time.sleep(1)
        print("pid 为", os.getpid(), '的子进程退出')

p1 = MyProcess(100)
p2 = MyProcess(10)
p3 = MyProcess(30)

p1.start()
p2.start()
p3.start()

p1.join()
p2.join()
p3.join()

