# 1. 写一个程序，输入你的生日
#   1) 算出你已经出生多少天
#   2) 算出你出生那天是星期几
#     用: time模块

import time

year = int(input('请输入您出生的年: '))
month = int(input('请输入您出生的月: '))
day = int(input('请输入您出生的日: '))

# 算出出生时，计算内时间的秒数(计算机元年开始的秒数)
birth_second = time.mktime((year, month, day,
                            0, 0, 0, 0, 0, 0))

cur_second = time.time()  # 得到现在的秒数
life_second = cur_second - birth_second
days = life_second / 60 / 60 // 24
print("您出生了%d天" % days)

# 得到出生那天的时间元组
t = time.localtime(birth_second)
print("您出生那天是星期:", t[6] + 1)


