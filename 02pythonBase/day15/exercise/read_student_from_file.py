# read_student_from_file.py


def read_from_file(filename='mydata.txt'):
    L = []
    try:
        f = open(filename)
        while True:
            s = f.readline()
            if not s:
                break
            s = s.strip()  # 去掉两侧空白字符
            lst = s.split()  # L = ['xiaozhang', '20', '100']
            L.append(dict(name=lst[0],
                          age=int(lst[1]),
                          score=int(lst[2])))
        f.close()
    except OSError:
        print("读数据失败")
    return L


L = read_from_file()
# print(L)

for d in L:
    print(d['name'], '今年:', d['age'],
        '成绩是:', d['score'])