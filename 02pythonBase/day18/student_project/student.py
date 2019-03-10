# student.py


class Student:
    # 用于描述学生对象
    def __init__(self, n, a, s):
        self.name = n
        self.age = a
        self.score = s

    def get_info(self):
        return (self.name, self.age, self.score)

    def get_score(self):
        return self.score

    def get_age(self):
        return self.age

    def write_file(self, file):
        file.write(self.name)
        file.write(',')
        file.write(str(self.age))
        file.write(',')
        file.write(str(self.score))
        file.write('\n')

