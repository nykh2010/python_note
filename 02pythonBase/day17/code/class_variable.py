# class_variable.py


# 此示例示意类变量
class Human:
    total_count = 0  # 创建类变量
    def __init__(self, n):
        self.name = n


print(Human.total_count)  # 0
Human.total_count = 1
print(Human.total_count)  # 1

h1 = Human("小张")  # 创建实例对象
print(h1.name)  # 小张
print(h1.total_count)  # 1
h1.total_count = 100  # 为自己添加了实例变量，并不存修改类变量
print(h1.total_count)  # 100

print(Human.total_count)  # 1

h1.__class__.total_count = 200
print(Human.total_count)  # 200
