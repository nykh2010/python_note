# mynumber3.py


class MyNumber:
    def __init__(self, v):
        self.data = v

    def __int__(self):
        return int(self.data)

n1 = MyNumber('100')

a = int(n1)  # 调用n1.__int__()
print(a)  # 100
print(bool(n1))  # True