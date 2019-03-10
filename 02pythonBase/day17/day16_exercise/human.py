# 练习:
#   有两个人
#     1. 姓名: 张三  年龄:36
#     2. 姓名: 李四  年龄:15
#   行为:
#     1. 教别人学东西 teach
#     2. 赚钱 work
#     3. 错钱 borrow
#     4. 显示人的信息show_info

#   class Human:
#       ...
#   事情:
#     zhang3 = Human("张三", 35)
#     li4 = Human("李四", 15)
#     # 张三 教 李四 学 python
#     zhang3.teach(li4, "python")
#     # 李四 教 张三 学 跳皮筋
#     li4.teach(zhang3, "跳皮筋")
#     # 张三 上班赚了 1000 元钱
#     zhang3.work(1000)
#     # 李四 向 张三 借了 200 元钱
#     li.borrow(zhang3, 200)
#     # 35 岁的 张三 有钱 800 元,它学会的技能是: 跳皮筋
#     zhang3.show_info()
#     # 15 岁的 李四 有钱 200 元,它学会的技能是: python
#     li4.show_info()

#   行为:
#     1. 教别人学东西 teach
#     2. 赚钱 work
#     3. 借钱 borrow
#     4. 显示人的信息show_info


class Human:
    def __init__(self, n, a):
        self.name = n  # 姓名
        self.age = a  # 年龄
        self.money = 0  # 每个对象的钱数
        self.skill = []  # 用来保存每个自己学到的技能

    def teach(self, other, subject):
        print(self.name, '教', other.name,
              '学', subject)
        other.skill.append(subject)

    def work(self, m):
        print(self.name, '上班赚了', m, '元钱')
        self.money += m

    def borrow(self, other, m):
        if other.money > m:
            print(self.name, '向', other.name,
                  '借了', m, '元钱')
            # 结果:
            self.money += m
            other.money -= m
            return True
        else:
            print(self.name, '向', other.name,
                '借钱失败')
            return False

    def show_info(self):
        print(self.age, '岁的', self.name,
              '有钱', self.money,
              '元,它学会的技能是',
              '、'.join(self.skill))


zhang3 = Human("张三", 35)
li4 = Human("李四", 15)
# 张三 教 李四 学 python
zhang3.teach(li4, "python")
# 李四 教 张三 学 跳皮筋
li4.teach(zhang3, "跳皮筋")
# 张三 上班赚了 1000 元钱
zhang3.work(1000)
# 李四 向 张三 借了 200 元钱
li4.borrow(zhang3, 200)
# 35 岁的 张三 有钱 800 元,它学会的技能是: 跳皮筋
zhang3.show_info()
# 15 岁的 李四 有钱 200 元,它学会的技能是: python
li4.show_info()
li4.teach(zhang3, '王者荣耀')
zhang3.show_info()

