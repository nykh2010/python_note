# enclosure.py

# 此示例示意用私有属性和私有方法实现封装
class A:
    def __init__(self):
        self.__p1 = 100  # 私有属性

    def __m(self):
        print("A类对象的私有实例方法被调用")

    def test(self):
        '''此对象的方法可以访问自己的私有属性和
        私有方法'''
        print("test里self.__p1=", self.__p1)  # 访问私有属性
        # 调用自己的私有方法
        self.__m()
        return self.__p1

a = A()
# print(a.__p1)  #  出错
a.__p1 = 200  # 在类的外部不能修改私有属性

v = a.test()
print("拿到的a里的私有属性__p1的值是:", v)

# a.__m()  # 调用A类的私有方法会出错