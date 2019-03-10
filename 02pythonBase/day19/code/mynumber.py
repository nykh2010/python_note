# mynumber.py

class MyNumber:
    '''此类用于定义一个自定义的数字类,
    用于示意运算符重载'''
    def __init__(self, value):
        self.data = value  # 用data来保存数据

    def __repr__(self):
        return "MyNumber(%d)" % self.data

    def __add__(self, other):
        print("__add__方法被调用")
        # 此方法要制定 self + other的规则
        v = self.data + other.data
        r = MyNumber(v)  # 创建新的对象
        return r

n1 = MyNumber(100)
n2 = MyNumber(200)
# n3 = n1.__add__(n2)  # 等同于 n3 = n1 + n2
n3 = n1 + n2  # 请问这样的操作可以吗?
# print(n3)  # MyNumber(300)
print(n1, '+', n2, '=', n3)

