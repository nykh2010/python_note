# override.py


# 此示例示意覆盖的用法
class A:
    def work(self):
        print("A.work被调用")

class B(A):
    "B类继承自A类"
    def work(self):
        print("B.work被调用")

    def super_work(self):
        # 1. 调用当前类的方法work
        self.work()
        # 2. 调用A类的方法work
        super(B, self).work()
        super().work()  # super(B, self)


b = B()
b.super_work()
# b.work()  # B.work被调用
# super(B, b).work()  # A.work被调用
super().work()  # 报错



