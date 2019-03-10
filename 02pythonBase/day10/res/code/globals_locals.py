# globals_locals.py

# 此示例示意globals() 函数和locals()函数的用法
a = 1
b = 2
c = 3
def fn(c, d):
    e = 300
    print("locals()返回:", locals())
    print("globals() 返回:", globals())
    print('局部变量c=', c)  # 100
    print('全局变量c=', globals()['c'])  # 3

fn(100, 200)
