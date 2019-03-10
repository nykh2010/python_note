# class_method.py


class A:
    v = 0  # ???

    @classmethod
    def get_v(cls):
        return cls.v

    @classmethod
    def set_v(cls, value):
        cls.v = value

# print(A.v)  # 0
var = A.get_v()  # 用类来调用类方法
print(var)  # 0
a = A()
print(a.get_v())  # 0 用实例对象来调用类方法

A.set_v(100)
print(A.get_v())  # 100
a.set_v(200)
print(A.get_v())  # 200


