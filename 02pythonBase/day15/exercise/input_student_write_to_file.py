# 1. 写一个程序 ,输入很多人的姓名,年龄,成绩, 把这些人的信息存入到文本文件'mydata.txt'中,格式为:
#   张三 20 100
#   李四 21 96
#   ...

def input_student():
    L = []
    while True:
        n = input('请输入学生姓名: ')
        if not n:
            break
        a = int(input('请输入学生年龄: '))
        s = int(input("请输入学生成绩: "))
        L.append(dict(name=n, age=a, score=s))
    return L


def write_to_file(L, filename='mydata.txt'):
    try:
        f = open(filename, 'w')
        for d in L:
            f.write(d['name'])
            f.write(' ')
            f.write(str(d['age']))
            f.write(' ')
            f.write(str(d['score']))
            f.write('\n')
        f.close()
    except OSError:
        print("保存失败!")



L = input_student()
print(L)
write_to_file(L)