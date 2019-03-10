# static_method.py


class A:
    @staticmethod
    def myadd(a, b):
        return a + b

print(A.myadd(100, 200))  # 300
a = A()
print(a.myadd(30, 40))  # 70

myadd(10, 20)


