# enclosure.py

# 此示例示意用私有属性和私有方法实现封装
class A:
    def __init__(self):
        self.__p1 = 100  # 私有属性

    def __m(self):
        print("A类对象的私有实例方法被调用")

class B(A):
    def mytest(self):
        self.__m()  # 也会出错，

b = B()
b.mytest()
# b.__m()  # 错!
