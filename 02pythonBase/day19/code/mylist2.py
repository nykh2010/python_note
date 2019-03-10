
# 此示例示意复合赋值算术运算符的重载
# x *= y    # x = x * y
class MyList:
    def __init__(self, iterable):
        self.data = list(iterable)

    def __repr__(self):
        return "MyList(%s)" % self.data

    def __mul__(self, rhs):
        print("__mul__被调用")
        r=  MyList(self.data * rhs)
        print('id(r)=', id(r))
        return r

    def __imul__(self, rhs):
        print("__imul__被调用")
        self.data *= rhs
        return self

L1 = MyList([1, 2, 3])
print(id(L1))  # ??
L1 *= 3  # 1) L1.__imul__(3)  2) L1 = L1 * 3
print(id(L1))  # ??
print(L1)

# L5 = L1 * 2  # 调用L1.__mul__(2)
# print(L5)

# L1 = MyList([1, 2, 3])
# L2 = MyList([1, 3, 2])
# if L1 < L2:
#     print(L1, "<", L2)
# else:
#     print(L1, ">=", L2)

