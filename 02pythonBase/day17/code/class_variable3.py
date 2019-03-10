# class_variable.py

# 此示例示意类变量
class Human:
    total_count = 0  # 创建类变量

    def __init__(self, n):
        self.name = n
        self.__class__.total_count += 1

    def __del__(self):
        self.__class__.total_count -= 1

h1 = Human("小张")
h2 = Human("小李")
# .....

# 程序在此处能否知道当前有几个Human类型的对象?

print(Human.total_count)  # 当前有两个Human对象存在
del h1
print(Human.total_count)  # 1 

