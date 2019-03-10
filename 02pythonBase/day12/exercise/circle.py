# 练习:
#   输入一个圆的半径,打印出这个圆的面积
#   输入另一个圆的面积,打印出这个圆的半径
#   (要求用math模块内的函数和数据)


import math


def test_math_module():
    r = float(input('请输入一个圆的半径: '))
    area = math.pi * r ** 2
    print("面积是: ", area)

    area = float(input("请输入另一个圆的面积: "))
    r = math.sqrt(area / math.pi)
    print("圆的半径是:", r)


test_math_module()

