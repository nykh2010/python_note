# mythread.py

# 此实例示意自定义线程类
import threading

class MyThread(threading.Thread):
    def __init__(self, times, *, info="无信息"):
        super().__init__()
        self.times = times
        self.info = info

    def run(self):
        '''此方法将覆盖父类的run,此方法退出，则线
        程执行结束'''
        import time
        for i in range(self.times):
            print("线程信息:", self.info, 'i=', i)
            time.sleep(1)

t1 = MyThread(10, info="线程1")
t2 = MyThread(5, info='线程2')
t1.start()  # 启动线程，父类中的方法
t2.start()

t1.join()  # 线程回收
t2.join()  # 此方法继承父类的方法 
print('主线程退出!!!')


