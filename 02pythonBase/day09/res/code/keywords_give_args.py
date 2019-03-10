

# 关键字传参
def myfun1(a, b, c):
    '这是一个函数参数的示例'
    print('a的值是:', a)
    print('b的值是:', b)
    print('c的值是:', c)


myfun1(b=22, c=33, a=11)  # 11-->a, 22-->b, 33-->c
myfun1(c=3, b=2, a=1)


