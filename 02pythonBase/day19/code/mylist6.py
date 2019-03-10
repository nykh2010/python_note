
# 此示例示意 切片 运算符的重载

class MyList:
    def __init__(self, iterable):
        self.data = list(iterable)

    def __repr__(self):
        return "MyList(%s)" % self.data

    def __getitem__(self, i):
        print("__getitem__: i=", i)
        if type(i) is int:
            print("正在进行索引取值")
        elif type(i) is slice:
            print("正在进行切片取值")
            print("起始值:", i.start)
            print("终止值:", i.stop)
            print("步长:", i.step)

        return self.data[i]

L1 = MyList(range(10))
print(L1)
a = L1[::2]  # L1.__getitem__(slice(None, None ,2))
print(a)

# L1[::2] = "ABCDE"
# 等同于 L1.__setitem__(slice(None,None, 2),
#                      "ABCDE")

