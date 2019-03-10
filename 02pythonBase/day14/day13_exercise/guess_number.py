# 2. 猜数字游戏:
#   随机生成一个0~100之间的整数，用变量x绑定
#   让用户输入一个数y,输出猜数字的结果
#      1) 如果y等于x，则提示"恭喜您猜对了"， 并退出程序
#      2) 如果y大于x,则提示"您猜的数字大了"
#      3) 如果y小于x,则提示"您猜的数字小了"
#   直到猜对为止，退出程序时显示用户猜数字的次数

import random
x = random.randrange(101)
times = 0  # 次数
while True:
    y = int(input('请输入您要猜的数: '))
    times += 1
    if y == x:
        print('恭喜您猜对了')
        print("您共猜了%d次" % times)
        break
    elif y > x:
        print("您猜大了")
    else:
        print("您猜小了")



