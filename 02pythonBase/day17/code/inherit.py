# inherit.py


class Human(object):
    def say(self, what):  # 说话
        print("说:", what)

    def walk(self, distance):  # 走路
        print("走了", distance, '公里')


class Student(Human):
    def study(self, subject):
        print("学习:", subject)


class Teacher(Student):
    def teach(self, subject):
        print("教:", subject)

h1 = Human()
h1.walk(5)
h1.say('现在天气凉快了')

s1 = Student()
s1.walk(4)
s1.say("快点回家")
s1.study("python")

t1 = Teacher()
t1.teach("面向对象")
t1.walk(20.5)
t1.say("终于到家了")
t1.study("转魔方")
