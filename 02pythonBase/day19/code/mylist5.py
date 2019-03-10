
# 此示例示意 索引和切片 运算符的重载

class MyList:
    def __init__(self, iterable):
        self.data = list(iterable)

    def __repr__(self):
        return "MyList(%s)" % self.data

    def __getitem__(self, i):
        print("i =", i)
        return self.data[i]

    def __setitem__(self, i, value):
        print('__setitem__: i = ', i, 'v=', value)
        self.data[i] = value

L1 = MyList([1, -2, 3, -4, 5])
v = L1[2]  # v = 3
print(v)

L1[1] = 2.22222  # L1.__setitem__(1, 2.22222)
print(L1)  # MyList([1, 2.22222, 3, -4, 5])
# print(L1[100])  # 越界

del L1[3]  # 调用 L1.__delitem__(3)


