# student.py


class Student:
    # 用于描述学生对象
    def __init__(self, n, a, s):
        self.__name = n
        self.__age = a
        self.__score = s

    def get_info(self):
        return (self.__name, self.__age, self.__score)

    def get_score(self):
        return self.__score

    def get_age(self):
        return self.__age

    def write_file(self, file):
        file.write(self.__name)
        file.write(',')
        file.write(str(self.__age))
        file.write(',')
        file.write(str(self.__score))
        file.write('\n')

