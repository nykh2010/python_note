# 4. 实现带有界面的学生信息管理系统
#    要求有操作界面如下:
#    +-------------------------------+
#    | 1)  添加学生信息                |
#    | 2)  显示学生信息                |
#    | 3)  删除学生信息                |
#    | 4)  修改学生成绩                |
#    | 5)  按学生成绩高-低显示学生信息   |
#    | 6)  按学生成绩低-高显示学生信息   |
#    | 7)  按学生年龄高-低显示学生信息   |
#    | 8)  按学生年龄低-高显示学生信息   |
#    | q)  退出程序                   |
#    +-------------------------------+
#    请选择: 1
#      要求,每个功能写一个函数与之相对应
#      学生信息为:姓名,年龄,成绩,用字典的列表保存不变


def input_student():
    L = []  # 创建一个列表,准备存储学生的信息数据 
    d = {}
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
        # d = {'name': n, 'age': a, 'score': s}
        d = d.copy()
        d['name'] = n
        d['age'] = a
        d['score'] = s
        L.append(d)
    return L


def output_student(lst):
    print("+---------------+----------+----------+")
    print("|    name       |   age    |   score  |")
    print("+---------------+----------+----------+")
    for d in lst:
        n = d['name'].center(15)
        a = str(d['age']).center(10)
        s = str(d['score']).center(10)
        print("|%s|%s|%s|" %(n, a, s))

    print("+---------------+----------+----------+")


def print_score_by_desc(lst):
    def k(d):
        return d['score']
    L = sorted(lst, key=k, reverse=True)
    output_student(L)

def save_to_file(lst, filename="si.txt"):
    try:
        fw = open(filename, 'w')
        for d in lst:
            fw.write(d['name'])
            fw.write(',')
            fw.write(str(d['age']))
            fw.write(',')
            fw.write(str(d['score']))
            fw.write('\n')
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
            L.append(dict(name=n, age=a, score=s))

        fr.close()
        print("读取数据成功")
    except OSError:
        print("读文件文件")

    return L


