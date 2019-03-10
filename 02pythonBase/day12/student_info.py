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
        a = int(input("请输入年龄: "))
        s = int(input("请输入成绩: "))
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


def show_menu():
    '''用于显示菜单'''
    print('+---------------------------------+')
    print('| 1)  添加学生信息                |')
    print('| 2)  显示学生信息                |')
    print('| 3)  删除学生信息                |')
    print('| 4)  修改学生成绩                |')
    print('| 5)  按学生成绩高-低显示学生信息 |')
    print('| 6)  按学生成绩低-高显示学生信息 |')
    print('| 7)  按学生年龄高-低显示学生信息 |')
    print('| 8)  按学生年龄低-高显示学生信息 |')
    print('| q)  退出程序                    |')
    print('+---------------------------------+')


def main():
    docs = []  # 用来保存学生信息的列表
    while True:
        show_menu()
        s = input("请选择: ")
        if s == 'q':
            return
        elif s == '1':
            docs += input_student()
        elif s == '2':
            output_student(docs)
        elif s == '5':
            print_score_by_desc(docs)

main()