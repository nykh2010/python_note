# 3. 编写一个闹钟程序，启动时设置定时时间，到时间后打印一句
# "时间到"，然后退出程序

def alarm(hour, minute):
    '''此函数传入小时和分钟，当前时间如果等于传入时间时
    则打印'时间到', 然后退出程序'''
    import time
    while True:
        t = time.localtime()  # 得到当前时间元组
        # if (hour, minute) == t[3:5]:
        print("%02d:%02d:%02d" % t[3:6], end='\r')
        if hour == t[3] and minute == t[4]:
            print("时间到...")
            break
        time.sleep(1)




h = int(input('请输入小时:'))
m = int(input('请输入分钟:'))
alarm(h, m)