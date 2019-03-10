
# 此示例示意将MyList变为可迭代对象且能用
# for 语句进行迭代访问

class MyList:
    def __init__(self, iterable):
        self.data = [x for x in iterable]

    def __repr__(self):
        return "MyList(%s)" % self.data

    def __iter__(self):
        '''此方法是要将MyList对象变为可迭代对象
        此方法必须返回迭代器
        '''
        print("__iter__方法被调用")
        return MyListIterator(self.data)  # 自定义的迭代器　

class MyListIterator:
    '''此类用于描述能够访问MyList对象的迭代器'''
    def __init__(self, data):
        # 在迭代器内加一个实例变量data来用绑定可迭代对象的数据
        self.data = data
        self.current = 0 # 当前需要返回的数据的索引


    def __next__(self):
        print("MyListIterator里的__next__方法被调用")
        if self.current >= len(self.data):
            raise StopIteration
        r = self.data[self.current]
        self.current += 1
        return r

myl = MyList([1, -2, 3, -4])

# it = iter(myl)  # 等同于 it = myl.__iter__()
# while True:
#     try:
#         x = next(it)  # 等同于 x = it.__next__()
#         print(x)
#     except StopIteration:
#         break

# 以上等同于如下:
for x in myl:
    print(x)  # 1, -2    3   -4

myset = {x for x in myl}
print("myset=", myset)  # {1, -2, 3, -4}

