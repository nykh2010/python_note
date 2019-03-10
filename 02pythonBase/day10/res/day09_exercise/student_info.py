
# 5. 改写之前的学生信息管理程序.
#   1) 编写函数 input_student() 获取学生信息,以学生姓名为空结束,返回学生信息的列表(列表里是字典)
#     (学生信息依旧是: 姓名,年龄,成绩)

#   2) 编写函数 output_student(L) 以表格形式打印学生信息

#   如:
#     def input_student():
#         ...
#     def output_student(lst):
#         ...
#     L = input_student()  
#     print(L)  # 打印学生的信息的列表
#     output_student(L)  以列表形式打印学生信息


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


L = input_student()  
print(L)  # 打印学生的信息的列表
output_student(L)  # 以列表形式打印学生信息


