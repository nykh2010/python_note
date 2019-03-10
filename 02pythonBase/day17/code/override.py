# override.py


# 此示例示意覆盖的用法
class A:
    def work(self):
        print("A.work被调用")


class B(A):
    "B类继承自A类"
    def work(self):
        print("B.work被调用")


b = B()
b.work()  # ???

a = A()
a.work()  # ????
