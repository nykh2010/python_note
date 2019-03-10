# len_overwrite.py

# 此示例示意内建函数len,和abs函数的重写方法
class MyList:
    '''这是一个自定义的列表类，其中内部用data实例变量
    绑定一个内建列表，用内建列表来存储数据'''
    def __init__(self, iterable):
        self.data = [x for x in iterable]

    def __repr__(self):
        '''返回能表达这个对象的表达式字符串'''
        return "MyList(%s)" % self.data

    def __len__(self):
        '''重写len(x) 函数,此方法必须返回整数'''
        # return 9999
        l = len(self.data)  # return self.data.__len__()
        return l

myl = MyList([1, -2, 3, -4])
myl2 = MyList(range(10))
print(len(myl))  # 4
print(len(myl2))  # 10

