

# 序列传参
def myfun1(a, b, c):
    '这是一个函数参数的示例'
    print('a的值是:', a)
    print('b的值是:', b)
    print('c的值是:', c)


s1 = [11, 22, 33]
s2 = (44, 55, 66)
s3 = 'ABC'

myfun1(*s1)
myfun1(*s2)
myfun1(*s3)

# myfun1(s1[0], s1[1], s1[2])

