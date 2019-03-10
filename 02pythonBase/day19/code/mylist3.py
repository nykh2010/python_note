
# 此示例示意一元运算符的重载

class MyList:
    def __init__(self, iterable):
        self.data = list(iterable)

    def __repr__(self):
        return "MyList(%s)" % self.data

    def __neg__(self):
        L = [-x for x in self.data]
        return MyList(L)  # 新建一个列表返回

    def __pos__(self):
        return self

L1 = MyList([1, -2, 3, -4, 5])
L2 = -L1  # L1.__neg__()  L2=[-1, 2, -3, 4, -5]
print(L2)
L3 = +L1  # 等同于 L3 = L1
print(L3)

