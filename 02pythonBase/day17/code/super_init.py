# super_init.py

# 此示例示意用super显式调用基类的初始化方法
class Human:
    def __init__(self, n, a):
        self.name, self.age = n, a
        print("Human.__init__被调用")

    def infos(self):
        print("姓名:", self.name)
        print("年龄:", self.age)


class Student(Human):
    def __init__(self, n, a, s):  # s 代表成绩
        # super(Student, self).__init__(n, a)
        super().__init__(n, a)
        self.score = s
        print("Student.__init__被调用")

    def infos(self):
        super().infos()
        print("成绩:", self.score)


s1 = Student("小李", 18, 100)
s1.infos()

h1 = Human("小张", 20)
h1.infos()


