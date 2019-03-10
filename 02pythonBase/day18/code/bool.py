
# 此示例示意bool(x) 函数的重写

class MyList:
    def __init__(self, iterable):
        self.data = [x for x in iterable]

    def __repr__(self):
        return "MyList(%s)" % self.data

    def __len__(self):
        print("__len__方法被调用!")
        l = len(self.data)  # return self.data.__len__()
        return l

    def __bool__(self):
        print("__bool__方法被调用")
        for x in self.data:
            if bool(x) is False:
                return False
        return True

myl = MyList([1, -2, 3, -4])
# myl = MyList([0, 1, 2])

print("bool(myl)=", bool(myl))

if myl:
    print("myl是真值")
else:
    print("myl是假值")


