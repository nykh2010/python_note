# def2.py


# 此示例示意带有参数的函数的定义和调用
def mymax(a, b):
    print("a的值是:", a)
    print("b的值是:", b)
    c = a + b
    print('c的值是:', c)
    if a > b:
        print("最大值是:", a)
    else:
        print("最大值是:", b)


mymax(100, 200)
# print("函数外部c的值是:", c)  # 报错
# print("a=", a)  # 报错 



