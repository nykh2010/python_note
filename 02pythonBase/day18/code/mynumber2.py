# mynumber.py

# 此示例示意repr(x) 和 str(x) 的重写方法

class MyNumber:
    '''此类用于定义一个自类的数字类型，
    用于演示str/repr重写'''
    def __init__(self, value):
        self.data = value  # 此实例变量用于绑定自己的数据

    def __str__(self):
        print("__str__方法被调用!")
        return "自定义数字:%d" % self.data

    def __repr__(self):
        print("__repr__方法被调用!")
        return "MyNumber(%d)" % self.data

n1 = MyNumber(100)
print("str(n1) =", str(n1))  # 自定义数字：100
# print(n1)  # ???