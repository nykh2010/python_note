# 2. 写一个程序，以电子时钟格式打印当前时间:
#    格式为:
#      HH:MM:SS 
#      最好每隔一秒打印一次
#    提示:
#      time.sleep(x)

import time

while True:
    # 每隔一秒，把当前时间拿出来显示一次
    t = time.localtime()  # 得到当前的本地时间
    print("%02d:%02d:%02d" % t[3:6], end='\r')  # 回退光标
    time.sleep(1)



