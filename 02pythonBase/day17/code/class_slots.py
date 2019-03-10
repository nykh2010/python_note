# class_slots.py

class Human:
    __slots__ = ['name', 'age']

    def __init__(self, n, a):
        self.name, self.age = n, a

    def show_info(self):
        print(self.name, '今年', self.age, '岁')


s1 = Human("小张", 18)
s1.show_info()  # ????
# s1.Age = 19  # 报错
# s1.show_info()  # ????
# print(s1.__dict__)  # 报错,__dict__ 不存在





