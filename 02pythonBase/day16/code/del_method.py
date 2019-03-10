# del_method.py


# 此例示意析构方法的定义和使用
class Car:
    def __init__(self, info):
        self.info = info
        # self.f = open("xxxx.py")
        print("汽车", info, "被创建")

    def __del__(self):
        print("汽车", self.info, '对象将被销毁')
        # self.f.close()


c1 = Car("BYD E6")
c2 = c1
del c1
while True:
    pass