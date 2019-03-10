# 2. 输入任意个学生的姓名,年龄,成绩,每个学生的信息存入字典,然后放入到列表中,每个学生信息需要手动输入:
#   如:
#     请输入姓名: xiaozhang
#     请输入年龄: 20
#     请输入成绩: 100
#     请输入姓名: xiaoli
#     请输入年龄: 18
#     请输入成绩: 95
#     请输入姓名: <回车> # 直接回车结束输入
#  内部存储格式如下:
#    [{'name': 'xiaozhang', 'age': 20, 'score':100},
#     {'name': 'xiaoli', 'age': 18, 'score':95},
#    ]
#  先将上述信息存于列表L 中, 然后以表格形式打印如下:
#  +---------------+----------+----------+
#  |    name       |   age    |   score  |
#  +---------------+----------+----------+
#  |   xiaozhang   |    20    |   100    |
#  |     xiaoli    |    18    |    95    |
#  +---------------+----------+----------+

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

print(L)

print("+---------------+----------+----------+")
print("|    name       |   age    |   score  |")
print("+---------------+----------+----------+")
for d in L:
    n = d['name'].center(15)
    a = str(d['age']).center(10)
    s = str(d['score']).center(10)
    print("|%s|%s|%s|" %(n, a, s))

print("+---------------+----------+----------+")





