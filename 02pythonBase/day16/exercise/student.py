# 练习:
#   写一个学生类Student,此类用于描述学生对象,
#      学生信息有:
#        姓名,年龄,成绩(默认为0)
#     1) 为该类添加初始化方法,实现在创建对象时自动设置: "姓名",'年龄', '成绩'属性
#     2) 添加set_score方法能为学生修改成绩信息
#     3) 添加show_info方法,打印学生对象的信息
#     如:
#       class Student:
#           def __init__(...):
#               ....
#           def set_score(self, score):
#               ...
#           def show_info(self):
#               ...
#       L = []
#       L.append(Student("小张", 20, 100))
#       L.append(Student("小李", 18, 95))
#       L.append(Student("小赵", 19))
#       for s in L:
#           s.show_info()




class Student:
    def __init__(self, n, a, s=0):
        self.name = n
        self.age = a
        self.score = s

    def set_score(self, score):
        print("set_score被调用: score=", score)
        if 0 <= score <= 100:
            self.score = score
            print(self.name, "的成绩修改为", score)
        else:
            print(self.name, "修改成绩失败!")

    def show_info(self):
        print("姓名:", self.name,
              '年龄:', self.age,
              '成绩:', self.score)

L = []
L.append(Student("小张", 20, 100))
L.append(Student("小李", 18, 95))
L.append(Student("小赵", 19))
for s in L:
    s.show_info()

L[-1].set_score(90)

for s in L:
    s.show_info()
