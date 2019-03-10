
from student import Student

def input_student():
    L = []  # 创建一个列表,准备存储学生的信息数据 
    while True:
        n = input("请输入姓名: ")
        # 如果姓名为空,则停止输入
        if not n:
            break
        try:
            a = int(input("请输入年龄: "))
            s = int(input("请输入成绩: "))
        except:
            print("输入错误,请重新输入")
            continue
        d = Student(n, a, s)
        L.append(d)
    return L


def output_student(lst):
    print("+---------------+----------+----------+")
    print("|    name       |   age    |   score  |")
    print("+---------------+----------+----------+")
    for d in lst:
        name, age, score = d.get_info()
        n = name.center(15)
        a = str(age).center(10)
        s = str(score).center(10)
        print("|%s|%s|%s|" %(n, a, s))

    print("+---------------+----------+----------+")


def print_score_by_desc(lst):
    def k(d):
        # return d['score']
        return d.get_score()
    L = sorted(lst, key=k, reverse=True)
    output_student(L)

def save_to_file(lst, filename="si.txt"):
    try:
        fw = open(filename, 'w')
        for d in lst:
            d.write_file(fw) #  把文件交给学生来写
        fw.close()
        print("保存成功")
    except OSError:
        print("保存失败")

def read_from_file(filename="si.txt"):
    L = []
    try:
        fr = open(filename)
        for line in fr:
            s = line.strip()  # 干掉'\n'
            lst = s.split(',')
            n = lst[0]  # 姓名
            a = int(lst[1])  # 年龄
            s = int(lst[2])  # 成绩
            L.append(Student(n, a, s))

        fr.close()
        print("读取数据成功")
    except OSError:
        print("读文件文件")

    return L


