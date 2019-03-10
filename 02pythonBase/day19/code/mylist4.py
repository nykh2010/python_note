
# 此示例示意 in / not in 运算符的重载

class MyList:
    def __init__(self, iterable):
        self.data = list(iterable)

    def __repr__(self):
        return "MyList(%s)" % self.data

    def __contains__(self, ele):
        print("__contains__被调用")
        if ele in self.data:
            return True
        return False

L1 = MyList([1, -2, 3, -4, 5])
print(3 in L1)  # True
print(3 not in L1)
print(4 in L1)
print(4 not in L1)
