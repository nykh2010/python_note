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

    def __abs__(self):
        L = [abs(x) for x in self.data]
        new = MyList(L)  # 再创建一个新的MyList对象
        print('id(new)=', id(new))
        return new

myl = MyList([1, -2, 3, -4])
myl3 = abs(myl)  # myl3 = MyList([1, 2, 3, 4])
print('myl=', myl)
print('myl3=', myl3)
print("id(myl3)=", id(myl3))
myl2 = MyList(range(10))
# print(myl)   # 等同于print(str(myl))
# print(myl2)  

# print(len(myl))  # 出错
# print(len(myl2))
# print(len(myl3))