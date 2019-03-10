# property.py


# 此示例示意特性属性
class Student:
    def __init__(self, s):
        self.__score = s

    @property
    def score(self):
        '''getter'''
        print("get_score被调用")
        return self.__score

    @score.setter
    def score(self, s):
        '''setter'''
        print("set_score 被调用")
        assert 0 <= s <= 100, "报错"
        self.__score = s

s1 = Student(50)

print(s1.score)  # 没及格
s1.score = 70
# s1.score = 10000
print(s1.score)  # 等同于在调用s1.get_score()