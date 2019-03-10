# closure.py


# 此示例示意闭包的定义和调用

def make_power(y):
    def fn(x):
        return x ** y
    return fn


pow2 = make_power(2)  # pow2绑定一个闭包函数
print('5的平方是:', pow2(5))

pow3 = make_power(3)
print('6的立方是:', pow3(6))

